# CV App 

CV app is an AI tool for curriculum screening and people recruiting. 

  - **Purpose:** get skills of my candidates from CV screening (*/metadata*) or find best candidate for my job position (*/candidate*).
  - **Input & Output:** it is implemented as a REST web-service (JSON).
  - **Info:** this service uses Watson IBM Natural Language Understanding API.

Please read the API documentation below to get informations about each endpoint.

## Installation
Install python 2.7 on a Linux distribution (tested on Ubuntu 16.04).
Download package and unzip it.
Run the following commands:

```sh
$ cd CV_app
$ sudo ./install_CVapp.sh requirements.txt
$ sudo python CV_server.py
```
To activate/deactivate the virtual enviroment, use:

```sh
$ source ~/dlenv/bin/activate
$ deactivate
```
## POST: [ /candidate ]
  - **Purpose:** Find best candidate for my job position.
  - **Input:** 
       -  Folder path of my CV (directory)             --> Required
       - Required skills for my job position (skills) --> Insert skills or label. Or both.
       - A label for this cluster of skills (label)   --> Insert skills or label. Or both.
   - **Output:** 
        - Job offer label (position)
        - Candidate info (best_candidates)
            - Candidate Name (name)
            - Candidate Email (contact)
            - CV info (cv):
                    - CV name (filename)
                    - CV language (language)
                    - CV skills (skills)

### Request example (PYTHON):
```py
import requests
import json

## HTTP DATA
my_headers={'Content-type' : 'application/json'}
my_url='http://127.0.0.1:80/candidate'

## INPUT DATA (JSON)
#Standard INPUT DATA (skills & label)
my_data={ "skills" : [ "science;computer science;artificial intelligence;;", "science;computer science;cryptography;;", "science;computer science;distributed systems;;", "science;computer science;information science;;", "technology and computing;operating systems;linux;;", "technology and computing;programming languages;java;;", "technology and computing;;;;", "technology and computing;technological innovation;;;", "technology and computing;software;databases;;", "technology and computing;operating systems;linux;;", "technology and computing;operating systems;unix;;", "technology and computing;programming languages;;;" ], "directory": "./pdf/", "label": "AI"  }

#Other type of INPUT DATA (no skills)
my_data={ "skills" : "", "directory": "./pdf/", "label": "AI"  }

#Other type of INPUT DATA (no label)
my_data={ "skills" : [ "science;computer science;artificial intelligence;;", "science;computer science;cryptography;;", "science;computer science;distributed systems;;", "science;computer science;information science;;", "technology and computing;operating systems;linux;;", "technology and computing;programming languages;java;;", "technology and computing;;;;", "technology and computing;technological innovation;;;", "technology and computing;software;databases;;", "technology and computing;operating systems;linux;;", "technology and computing;operating systems;unix;;", "technology and computing;programming languages;;;" ], "directory": "./pdf/", "label": ""  }

## HTTP REQUEST
r=requests.post(my_url,data=json.dumps(my_data), headers=my_headers)
r.json()
```

### Output (JSON):
```json
{u'best_candidates': [{u'contact': u'martina.manfrin87@gmail.com',
   u'cv': {u'filename': u'./pdf/MartinaManfrinProfile.pdf',
    u'language': u'it',
    u'skills': [u'/technology and computing/software/databases',
     u'/technology and computing',
     u'/science/computer science/artificial intelligence']},
   u'name': u'Martina Manfrin'}],
 u'position': u'AI'}
```
## POST: [ /metadata ]

  - **Purpose:** get skills of my candidates from CV screening.
  - **Input:** folder path of my CV (directory) --> Required
  - **Output:** metadata of all CVs in my path:
    - Candidate info (candidates):
        - Candidate Name (name)
        - Candidate Email (contact)
        - CV info (cv):
                - CV name (filename)
                - CV language (language)
                - CV skills (skills)

### Request example (PYTHON):
```py
import requests
import json

## HTTP DATA
my_headers={'Content-type' : 'application/json'}
my_url='http://127.0.0.1:80/metadata'

## INPUT DATA (JSON)
my_data={"directory": "./pdf/"}

## HTTP REQUEST
r=requests.post(my_url,data=json.dumps(my_data), headers=my_headers)
r.json()
```
### Output (JSON):
```json
{u'candidates': [{u'contact': u'andreagiordanodev@yahoo.it',
   u'cv': {u'filename': u'./pdf/AndreaGiordanoProfile.pdf',
    u'language': u'it',
    u'skills': [u'/technology and computing/software',
     u'/technology and computing/consumer electronics/telephones/mobile phones/smart phones',
     u'/business and industrial/business operations/management/business process']},
   u'name': u'Andrea Giordano'},
  {u'contact': u'martina.manfrin87@gmail.com',
   u'cv': {u'filename': u'./pdf/MartinaManfrinProfile.pdf',
    u'language': u'it',
    u'skills': [u'/technology and computing/software/databases',
     u'/technology and computing',
     u'/science/computer science/artificial intelligence']},
   u'name': u'Martina Manfrin'},
  {u'contact': u'archbonni@gmail.com',
   u'cv': {u'filename': u'./pdf/IrriveRender Arch. Bonn\xec Learning 3DProfile.pdf',
    u'language': u'it',
    u'skills': [u'/art and entertainment/visual art and design/architecture',
     u'/technology and computing/software/graphics software/animation',
     u'/technology and computing/software']},
   u'name': u'IrriveRender Arch. Bonn\xec Learning 3D'}]}
```

## License & Troubleshooting
This is a Manfrina web-app, released under GPL license. 
If it doesn't work is because server is being attacked by rebel robots. 
In that case, please fell free to contact me at: manfrina87ATgmail.com


