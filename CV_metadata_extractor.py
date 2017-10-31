#!/usr/bin/python

import sys
from os import path
from glob import glob

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

from bs4 import BeautifulSoup
import json
import requests
import re

from CV_constants import *



#PDF to HTML
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = HTMLConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


def html_parser(CV_page):
    #Parse HTML
    soup=BeautifulSoup(CV_page, "lxml")

    #remove BR tags
    for e in soup.findAll('br'):
        e.extract()
	
    #Parse CV header
    CV_header=[]	
    for fields in soup.body.div.next_sibling.next_element.contents:
        CV_header.append(fields.contents)
		
    CV_name=CV_header[0][0].strip()
    CV_prof_label=CV_header[1][0].strip()
    CV_email=CV_header[1][1].strip()

    #Parse CV body
    CV_body=[]
    for sp in soup.body.find_all('span', {"style" : "font-family: Times-Roman; font-size:13px"}):
        CV_body.append(sp.get_text())
	
    #CV text for Watson request
    CV_text=CV_prof_label+' '+' '.join(CV_body)
    return CV_name, CV_email, CV_text

#Create JSON for Watson request
def watson_data_creator(CV_text):
    #Preprocessing
    regex=r'Contact .*? on LinkedIn'
    CV_text=re.sub(regex,'',CV_text)
    #Insert CV_text into JSON
    nlu_json= { "text": CV_text, "features": { "categories": {} } }
    #Create headers
    nlu_headers = {'Content-type': 'application/json', 'Accept' : 'application/json'}
    return nlu_json, nlu_headers

#Parse JSON of Watson NLU
def watson_response_parser(r):
    nlu_response=r.json()
    #Find CV classification
    CV_categories=[]
    for categories in nlu_response['categories']:
        CV_categories.append(categories['label'])
    #Find CV language
    CV_language=nlu_response['language']   
    return CV_categories, CV_language


#Filter PDF files in dir
def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))


### MAIN PROGRAM ###
def metadata_finder (CV_directory):
    #Filter PDF files in directory path
    CV_files=find_ext(CV_directory,"pdf")
    
    CV_json={}
    CV_response=[]
    
    #For each CV_file in CV_files folder...
    for CV_file in CV_files:
        #Convert CV: PDF to HTML
        CV_page=convert(CV_file)
        #Parse HTML CV
        CV_name, CV_email, CV_text = html_parser(CV_page)
        #IBM Watson -- Natural Language Understanding API
        nlu_url=WATSON_URL
        #Insert CV text into JSON
        nlu_json, nlu_headers=watson_data_creator(CV_text)
        #Request to Watson NLU
        r=requests.post(nlu_url,headers=nlu_headers,json=nlu_json)
        #Get informations from Watson NLU response
        CV_categories, CV_language = watson_response_parser(r)
        #Create a dict: CV_name, CV_email, CV_file, CV_language, CV_categories
        CV_metadata={"name": CV_name, "contact": CV_email, "cv":{"filename": CV_file,"language": CV_language, "skills": CV_categories}}
        #Add CV_metadata to response
        CV_response.append(CV_metadata)
    
    CV_json['candidates']=CV_response
    return CV_json


