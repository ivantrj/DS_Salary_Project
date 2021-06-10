# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:38:37 2021

@author: ivan.trajanovski
"""

import sys
sys.path.append(".")

import glassdoor_scraper as gs
import pandas as pd
path = "E:/Developer/DS_Salary_Project/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)