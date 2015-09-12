import pandas as pd
import time

t1=time.time()

college_url="https://s3.amazonaws.com/ed-college-choice-public/Most+Recent+Cohorts+(Scorecard+Elements).csv"
salary_url="https://s3.amazonaws.com/ed-college-choice-public/Most+Recent+Cohorts+(Treasury+Elements).csv"
#Data not included in repository because of github's file size limitation, hosting it locally
#is better for speed, if not possible load it through the url
try:
    college_data=pd.read_csv('college_data.csv')
except:
    college_data=pd.read_csv(url)
    
try:
    salary_data=pd.read_csv('salary_data.csv')
except:
    salary_data=pd.read_csv(salary_url)


t2=time.time()
print t2-t1
print "Done"

