#!/usr/bin/python

import sys
from os import path

import csv
import re

from CV_metadata_extractor import metadata_finder

#CSV preprocessing
def csv_skills_preproc(csv_skills):
    best_candidate_skills=[]
    with open(csv_skills, 'r') as csvfile:
        myreader= csv.reader(csvfile, delimiter=';')
        for row in myreader:
            skill='/'.join(row)
            skill=re.sub(r'(.*?)/+$',r'/\g<1>',skill)
            best_candidate_skills.append(skill)
        return best_candidate_skills



#Match candidate skills with best_candidate_skills
def best_candidate_match(best_candidate_skills,candidates):
    best_candidates=[]
    #For each candidate in candidates...
    for candidate in candidates['candidates']:
        name=candidate['name']
        skills=candidate['cv'].values()[0]
        #If match, print candidate info
        for skill in skills:
            if skill in best_candidate_skills:
                best_candidates.append(candidate)
    return best_candidates



## MAIN PROGRAM
def bestcandidate_finder(skills_csv, CV_directory):
    candidates=metadata_finder(CV_directory)
    best_candidate_skills=csv_skills_preproc(skills_csv)
    my_candidate=best_candidate_match(best_candidate_skills,candidates)
    candidate_list=[i for n, i in enumerate(my_candidate) if i not in my_candidate[n + 1:]]
    candidate_dict={"best_candidates": candidate_list}
    return candidate_dict

