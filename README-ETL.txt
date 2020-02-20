The data was available in csv format from Kaggle 
https://www.kaggle.com/donorschoose/io

The files are the used to integrate different tables data to create an aggregated JSON 
and load the JSON objects in mongoDB using the pymongo library.
The data is aggregated by clubbing donors and donotion tables with the DonorMerge File
and projects, donation table are merged to create ProjectStatistics aggregate.