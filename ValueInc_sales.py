#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:07:11 2023

@author: nestorfernandez
"""

import pandas as pd

#file_name = pd.read_csv('file.csv') <---- format of read csv
data = pd.read_csv('transaction2 (1).csv')

data = pd.read_csv('transaction2 (1).csv', sep=';')

#summary of the data
data.info()

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem


ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased


#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Adding new column to a dataframe
data['CostPerTransaction'] = CostPerTransaction

#Sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#ProfitCalculation = Sales - Cost
data['ProfitPerTransaction'] =  data['SalesPerTransaction'] - data['CostPerTransaction']
#Markup = (Sales - Cost) / Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']



#Rounding Marking
roundmarkup = round(data['Markup'], 2)
data['Markup'] = roundmarkup

#combining data fields
myName = 'Nestor' + 'Fernandez'

my_date = 'Day' + '-' + 'Month' + '-' + 'Year'

#checking columns data type
print(data['Day'].dtype)

#Change columns type
day = data['Day'].astype(str)
print(day.dtype)
new_date = data['Day'].astype(str)+'-'+data['Month']+'-'+data['Year'].astype(str)

data['date'] = new_date


#using iloc to view specific columns/rows
data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3
data.iloc[-5:] #last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows with 2nd column
data.iloc[4,2] #brings in 4th row and 2nd column


#using split to split client keyword field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand = True)


#creatig new columns for split columns in client keyword
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')


#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()


#how to merge files
#bringing in a new data set

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

# df = df.drop('columnname, axis = 1)

data = data.drop('ClientKeywords', axis =1)
data = data.drop('Day', axis =1)
data = data.drop(['Year', 'Month'], axis =1)


#Export into CSV file

data.to_csv('ValueInc_Cleaned.csv', index = False)













