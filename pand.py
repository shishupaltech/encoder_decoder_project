import pandas as pd
#numpy error with version = pip install numpy == 1.19.3
# pip install openpyxl
# element tree

data = pd.read_excel("Mailex.xlsx" ,engine='openpyxl')
# print(data['City'],type(data['City']))# series me ek column means whole data of same series in one field whole data is called dataframe

if 'Email' in data.columns:
    # print("Exist")
    emails=list(data['Email'])
    # print(emails)
    c=[]
    for i in emails:
    # print(i)
        if pd.isnull(i)==False:
            # print(i)
            c.append(i)
    emails=c
    print(emails)
else:
    print("Not Exist")


