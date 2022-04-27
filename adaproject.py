
import pandas as pd
u = pd.read_json("/Users/emileabi/Documents/HEC Master/second semester/ADA/Projet Ada/hec-project/data/hec-project-data-sample.json")


# # Task description
#
#
# Talent has millions of users who are searching for jobs. We store all user interactions to improve relevance of the content shown to user.
# These interaction are in the dataset sample hec-project-data-sample.json in columns job_search, job_click and job_ioa.
#
# Given a user profile (which is a row in the below table) we want to know the following:
#
# 1. What would be the next activity date of the user?
# 2. How many more action this user is likely to accomplish?
#
# One or both of the questions could be taken as a project.
#
# The approach we recommend is the following:
#
# 1. Split each profile in time by event date, so that 1-2 events are used for prediction and the rest is to predict.
# 2. Use something like CountVectoriser to embed textual fields of the events.
# 3. Use the following to embed the soc_code: 49-1011.00 is transformed to integer 49101100
# 4. Predicting date of the activity is rather predicting a range of dates like "soon" (3-10 days), "later" (11-30 days), "long term" (30-90 days), "never" (90-360 days). Concrete split is to be decided based on the dates available in actual dataset, but the idea is to try to make it a classification problem rather then regression.
# 5. Same approach is recommended for question # 2. "no action", "few" (1-3 actions), "some" (4-10 actions), "many" (10-50 actions), "a lot" (50+ actions)
#


u.head()

for event in u.loc[0].job_click:
    print(event["keyword"], event["eventDate"])


u.sort_index(axis = 0, inplace=True )

u['job_click'][0][0]['empname']
u['job_click'][0][1]
x=0
for i in range(len(u['job_click'][0][0])):
    x += 1
print(x)

x=0
for i in range(len(u['job_click'][0][1])):
    x += 1
print(x)

u['job_click'][0][1]

u['job_click'][2][0]['']