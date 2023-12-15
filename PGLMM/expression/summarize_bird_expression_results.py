# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:07:49 2022

@author: Mark Hibbins
"""

### This script takes the significant results generated by 
### bird_expression_fdr_correction.py and counts the number of genes
### significant for each model term. 

import csv

result_lines = [] 
summary_dict = {"nesting_stratob_cavity": [0, 0],
                "nesting_stratob_cavity:sexM": [0,0],
                "nesting_stratopen": [0, 0],
                "nesting_stratopen:sexM": [0, 0],
                "sexM": [0,0],
                "attrate": [0,0],
                "nesting_stratob_cavity:attrate":[0,0],
                "nesting_stratob_cavity:sexM:attrate":[0,0],
                "nesting_stratopen:attrate":[0,0],
                "nesting_stratopen:sexM:attrate":[0,0],
                "sexM:attrate":[0,0]}

with open("C:/Users/18126/OneDrive - University of Toronto/Projects/bird_expression/results/bird_expression_agg_models_fdr_results.csv", "r") as model_results:
    for line in model_results:
       result_lines.append(line.split(","))
      
for line in result_lines[1:]:
    if float(line[4]) < 0:
        summary_dict[line[3]][0] += 1
    else:
        summary_dict[line[3]][1] += 1

        
print(summary_dict)