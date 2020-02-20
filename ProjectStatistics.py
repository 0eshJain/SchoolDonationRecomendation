# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importing all the required libraries
#pymongo library will help in writing data directly to mongodb
import os
import pandas as pd
#import numpy as np
import json
import pymongo
from bson import json_util
#def replaceComma(x):
  #  a = x.replace(",","|")
  #  return a

#Function to convert in json format  
def rowToJSON(x):
    a = json.loads(x.to_json())
    return a

#Connectivity code for mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["donor"]
mycol = mydb["ProhectStats"]
#Setting the location of folder, from where all the csv files will be read
os.chdir(r'C:\Users\19799\Desktop\ProjectStats\ProjectStats\file1')

#Loop to read all the files in the folder, manipulate them in dataframe and write to mongodb
for f in os.listdir():
	#Reading the file into dataframe 
    dfProjectStats = pd.read_csv(f, sep='|', index_col=False)
    #file_name, file_ext = os.path.splittext(f) 
    #dfProjectStats['Words']=dfProjectStats['Words'].apply(lambda line:replaceComma(line))
    #Deleting the index
	del dfProjectStats['index']
	#Putting ProjectID as _id which is the primary key
    dfProjectStats.rename(columns = {'ProjectID':'_id'}, inplace = True)
    newlist=[]
	#Applying the function rowToJSON to whole dataframe and storing in newlist
    dfProjectStats.apply(lambda x: newlist.append(rowToJSON(x)), axis=1)
	#Writing the data to mongodb
    x = mycol.insert_many(newlist)
    


