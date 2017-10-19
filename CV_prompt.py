#!/usr/bin/python

import csv

from CV_best_candidate import bestcandidate_finder


# Print CSV with selected skills
def csv_writer(my_skills, my_position_label='candidate_requirements'):
    with open(my_position_label, 'w') as csvfile:
        for s in my_skills:
            line=s+"\n"
            csvfile.write(line)
    return my_position_label


## MAIN PROGRAM ##


# Print CSV of selected skills
def candidate_getter(CV_directory, my_skills, my_position_label):
    # If not exists my_position_label
    if not my_position_label:
        skills_csv=csv_writer(my_skills)
    # If  not exists my_skills
    elif not my_skills:
        skills_csv=my_position_label
    # If we have both params
    else:
        skills_csv=csv_writer(my_skills, my_position_label)
    # Find best candidate
    my_candidates=bestcandidate_finder(skills_csv, CV_directory)
    # Create JSON response with: my_candidates, my_position_label
    my_candidates.update({"position": skills_csv})
    return my_candidates
