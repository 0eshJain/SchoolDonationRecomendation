#Importing all the required libraries
#pymongo library will help in writing data directly to mongodb
import os
import pandas as pd
#import numpy as np
import json
import pymongo
from bson import json_util

#Function to convert in json format  

def rowToJSON(x):
    a = json.loads(x.to_json())
    return a
	
def main():
	#Location from where donors csv will be read
	os.chdir('G:\ADV DATABASE PROJECT\io')
	#Reading Donors.csv into dataframe donors
	donors=pd.read_csv('Donors.csv')
	#Connectivity code for mongodb
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["donor"]
	mycol = mydb["DonorStats"]
	#Location to the folder which has all DonorStats
	os.chdir(r'G:\ADV DATABASE PROJECT\io\DonorStats')

	#Loop to read all the files in the folder, manipulate them in dataframe, merge with donors and write to mongodb
	for f in os.listdir():
		#Reading the file into dataframe 
		donorStats=pd.read_csv(f,sep='|', index_col=0)
		#Merging the file with donors
		merged_donorStats = pd.merge(donors, donorStats, on='Donor ID')
		#Renaming the columns
		merged_donorStats.rename(columns={"Donor ID": "DonorId", "Donor City": "City","Donor State":"State","Donor Is Teacher":"IsTeacher","Donor Zip":"Zip","Project Resource Category":"ProjectResourceCategory","sum":"DonationSum","count":"DonationCount"})
		newlist=[]
		#Applying the function rowToJSON to whole dataframe and storing in newlist
		merged_donorStats.apply(lambda x: newlist.append(rowToJSON(x)), axis=1)
		#Writing the data to mongodb
		x = mycol.insert_many(newlist)
    
if __name__ == '__main__':
    main()