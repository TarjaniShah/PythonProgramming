import pandas as pd
import numpy as np

df = pd.read_csv("Austin_Animal_Center_Intakes.csv")
#Dataset: https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Intakes/wter-evkm

#sneak peak of the data
df.head()

#All the details of the data
df.info()

#To find the number of rows and columns
df.shape

#To check for null values in the data
df.isnull()

#DATA CLEANING
#1: Replace all the spaces in the column heading by underscore
df.rename(columns=lambda x: x.replace(" ","_"), inplace=True)
df.columns

df['Name'].isnull().sum()   #gets the count of null values

#2: To replace null values of the NAME column to 'NoName'
df['Name'].fillna('NoName', inplace = False)
df.head()

#3: To remove asterick from the name as it does not make sense
df['Name']=df['Name'].apply(lambda x:str(x).replace('*',''))
df.head()
 
#4: There are 2 columns that has similar enteries of date and time but in different format; hence dropping 1 column to remove redundancy
df.drop('MonthYear', axis=1, inplace=True)
df.head()

#Correcting DataTypes
#Check the datatypes of all the columns
df.dtypes
#5: To convert from object data type to date datatype
df['DateTime'] =  pd.to_datetime(df['DateTime'])
df.dtypes

#6: To further remove time as it is of no use for the analysis
df['DateTime'] = df['DateTime'].apply(lambda x: x.date())
df.head()

#Since we removed the time, the data type has changed to Object again and hence again changing back the datatype
df['DateTime'] =  pd.to_datetime(df['DateTime'])
df.dtypes

#7: To just get the year from the date; to perform analysis on yearly basis
df['year'] = df['DateTime'].dt.year
df['year']
df.head()

#8: Converted years to months to maintain uniformity in the data.
#Step1: Created a new numpy array
split = np.array(df['Age_upon_Intake'].str.split(' '))
split
#Step2: Converted years to months
for i in split:              #iterated over split to multiply years value by 12 to convert in months
    if i[1] == "year":
        i[0] = int(i[0])*12
        i[1] = 'months'    
        
print(split)
p = []                      #created empty list to store just the values in months
for y in split:
    p.append(y[0])
    
print(p)
#Step3: Converted the numpy array to dataframe and concatenated with the original data.
df1 = pd.DataFrame(p)
newDf = pd.concat([df,df1], axis = 1) #axis = 1 as concatenating along the column
newDf.rename(columns={0:"Age_In_Months"}, inplace=True) #renamed the default value given to the new column
newDf

#DATA ANALYSIS
#Since the data has more categorical attributes, the analysis has frequency distribution
#1: For type of Animals
pd.crosstab(index=newDf["Animal_Type"], columns="count")

#2: For year vise count
pd.crosstab(index=newDf["year"], columns="count")

#3: For Intake condition
pd.crosstab(index=newDf["Intake_Condition"], columns="count")

#4: For different intake types
pd.crosstab(index=newDf["Intake_Type"], columns="count")

