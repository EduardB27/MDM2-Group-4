# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:31:49 2022

@author: sm20698
"""

import pandas as pd
import nltk
#import seaborn as sns
#import pickle
#import re
#import string
from sklearn.feature_extraction.text import CountVectorizer
#from IPython import embed 
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#we firstly have to create a file path to access our spreadsheet
excel_file_path = 'Hotel_Reviews.csv'

#printing the names of all the columns from our excel spreadsheet
df = pd.read_csv(excel_file_path)
#print(df.columns)    

#general information about data frame (how many rows we have and what type of data is in each data frame)
#df_info = df.info()
#print(df_info)

#this gives specific info about individual columns (min, max etc)
#print(df.describe()['Reviewer_Score'])

#getting more specific and obtaining all the rows where the reviewer score is equal to 5
#print(df[df['Reviewer_Score']==5]) 


#creating a spreadsheet where the scores are in a specific range
#reviewer_score = df[(df['Reviewer_Score']>= 6) & (df['Reviewer_Score'] <= 7)]
#reviewer_score.to_excel('output.xlsx')


#if we want to group two columns together - all the hotels that have the same score
#grouped_df = df['Hotel_Name'].groupby(df['Average_Score'])
#grouped_df.to_excel('Unique_Score.xlsx')

#Pairing up a particular row with a particular column 
#this gives negative reviews for a particular hotel
#tier4_hotel = df.loc[df.Hotel_Name == 'Hotel Cavendish', 'Negative_Review'] 
#print(tier4_hotel)

#what if we want to pair multiple rows with the same column
#this gives all the negative reviews for our group of lowest tier hotels
tier4_hotel = df.loc[df['Hotel_Name'].isin(['Bloomsbury Palace Hotel', 'Hotel Cavendish','The Tophams Hotel']),['Hotel_Name', 'Negative_Review']]
tier4_hotel.to_excel('Tier4_Hotels.xlsx',index=False )
excel_file_path_4 = 'Tier4_Hotels.xlsx'
df4 = pd.read_excel(excel_file_path_4)
#now we merge all the negative reviews into a single row for each hotel
df4['Negative_Review'] = df4.groupby(['Hotel_Name'])['Negative_Review'].transform(lambda x : ' '.join(x))
df4 = df4.drop_duplicates(subset=['Hotel_Name', 'Negative_Review'])   
#df4.to_csv('Tier_4_Negative.csv')


########### REPEAT FOR THE OTHER TIERS

tier3_hotel = df.loc[df['Hotel_Name'].isin(['Park Lane Mews Hotel', 'Kube Hotel Ice Bar','Hilton London Olympia','Mercure London Paddington Hotel','Le Meridien Piccadilly']),['Hotel_Name', 'Negative_Review']]
tier3_hotel.to_excel('Tier3_Hotels.xlsx',index=False)
excel_file_path_3 = 'Tier3_Hotels.xlsx'
df3 = pd.read_excel(excel_file_path_3)
df3['Negative_Review'] = df3.groupby(['Hotel_Name'])['Negative_Review'].transform(lambda x : ' '.join(x))
df3 = df3.drop_duplicates(subset=['Hotel_Name', 'Negative_Review'])
#df3.to_excel('Tier_3_Negative.xlsx')

tier2_hotel = df.loc[df['Hotel_Name'].isin(['The Principal London', 'The Park Tower Knightsbridge a Luxury Collection Hotel','Park Plaza County Hall London','Novotel London Tower Bridge',' Park Grand London Lancaster Gate']),['Hotel_Name', 'Negative_Review']]
tier2_hotel.to_excel('Tier2_Hotels.xlsx',index=False)
excel_file_path_2 = 'Tier2_Hotels.xlsx'
df2 = pd.read_excel(excel_file_path_2)
df2['Negative_Review'] = df2.groupby(['Hotel_Name'])['Negative_Review'].transform(lambda x : ' '.join(x))
df2 = df2.drop_duplicates(subset=['Hotel_Name', 'Negative_Review']) 
#df2.to_excel('Tier_2_Negative.xlsx')

tier1_hotel = df.loc[df['Hotel_Name'].isin(['The Nadler Soho', 'Staybridge Suites London Vauxhall',' Covent Garden Hotel','Haymarket Hotel','Ritz Paris']),['Hotel_Name', 'Negative_Review']]
tier1_hotel.to_excel('Tier1_Hotels.xlsx',index=False)
excel_file_path_1 = 'Tier1_Hotels.xlsx'
df1 = pd.read_excel(excel_file_path_1)
df1['Negative_Review'] = df1.groupby(['Hotel_Name'])['Negative_Review'].transform(lambda x : ' '.join(x))
df1 = df1.drop_duplicates(subset=['Hotel_Name', 'Negative_Review'])  
#df1.to_excel('Tier_1_Negative.xlsx')
#print(df1.loc[df1.Hotel_Name == 'Ritz Paris' ])

#DATA CLEANING
#REMOVING ALL SPECIAL CHARACTERS
spec_chars = ["!",'"',"#","%","&","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–", "No Negative", "Nothing"]
for char in spec_chars:
    df1['Negative_Review'] = df1['Negative_Review'].str.replace(char, ' ')
    df2['Negative_Review'] = df2['Negative_Review'].str.replace(char, ' ')
    df3['Negative_Review'] = df3['Negative_Review'].str.replace(char, ' ')
    df4['Negative_Review'] = df4['Negative_Review'].str.replace(char, ' ')

#MAKING EVERYTHING LOWERCASE
df1['Negative_Review'] = df1['Negative_Review'].map(lambda x: x.lower() if isinstance(x,str) else x)
df2['Negative_Review'] = df2['Negative_Review'].map(lambda x: x.lower() if isinstance(x,str) else x)
df3['Negative_Review'] = df3['Negative_Review'].map(lambda x: x.lower() if isinstance(x,str) else x)
df4['Negative_Review'] = df4['Negative_Review'].map(lambda x: x.lower() if isinstance(x,str) else x)

#Remove numbers
df1['Negative_Review'] = df1['Negative_Review'].str.replace('\w*\d\w*', '')
df2['Negative_Review'] = df2['Negative_Review'].str.replace('\w*\d\w*', '')
df3['Negative_Review'] = df3['Negative_Review'].str.replace('\w*\d\w*', '')
df4['Negative_Review'] = df4['Negative_Review'].str.replace('\w*\d\w*', '')

df1.to_excel('Tier_1_Negative.xlsx',index=False)
df2.to_excel('Tier_2_Negative.xlsx',index=False)
df3.to_excel('Tier_3_Negative.xlsx',index=False)
df4.to_excel('Tier_4_Negative.xlsx',index=False)


#CREATE CORPUS
#embed() 




stop_words = nltk.corpus.stopwords.words('english')
new_words=("bit","didn","like","good","did","just","wasn",
                  "did","could","would","also","get","us",
                  "even","really","one","everything","nothing",
                  "needs","work","next","quite","think","asked","got","need")
for i in new_words:
    stop_words.append(i)

cv = CountVectorizer(stop_words=stop_words)
data_cv1= cv.fit_transform(df1['Negative_Review'])
data_dtm1 = pd.DataFrame(data_cv1.toarray(), columns=cv.get_feature_names_out())
data_dtm1.index = df1.index
data_dtm1.to_excel('new_data1.xlsx')

cv = CountVectorizer(stop_words=stop_words)
data_cv2= cv.fit_transform(df2['Negative_Review'])
data_dtm2 = pd.DataFrame(data_cv2.toarray(), columns=cv.get_feature_names_out())
data_dtm2.index = df2.index
data_dtm2.to_excel('new_data2.xlsx')

cv = CountVectorizer(stop_words=stop_words)
data_cv3= cv.fit_transform(df3['Negative_Review'])
data_dtm3 = pd.DataFrame(data_cv3.toarray(), columns=cv.get_feature_names_out())
data_dtm3.index = df3.index
data_dtm3.to_excel('new_data3.xlsx')

cv = CountVectorizer(stop_words=stop_words)
data_cv4= cv.fit_transform(df4['Negative_Review'])
data_dtm4 = pd.DataFrame(data_cv4.toarray(), columns=cv.get_feature_names_out())
data_dtm4.index = df4.index
data_dtm4.to_excel('new_data4.xlsx')


#ATTEMPTED TO USE LOOP FOR FREQUENCY ANALYSIS BUT FAILED 
#N = 35
#for i in [data_dtm1,data_dtm2,data_dtm3,data_dtm4]:
#    print(i.sum().nlargest(N).rename_axis('word').reset_index(name='count'))
    

#FREQUENCY ANALYSIS WITHOUT LOOP
#TOP 35 WORDS FOR EACH TIER/ NOT INDIVIDUAL HOTEL
N=40
top_dict1 = {}
top_1= data_dtm1.sum().nlargest(N).rename_axis('word').reset_index(name='count')
top_dict1 = top_1.set_index('word').to_dict()['count']

top_dict2 = {}
top_2= data_dtm2.sum().nlargest(N).rename_axis('word').reset_index(name='count')
top_dict2 = top_2.set_index('word').to_dict()['count']

top_dict3 = {}
top_3= data_dtm3.sum().nlargest(N).rename_axis('word').reset_index(name='count')
top_dict3 = top_3.set_index('word').to_dict()['count']

top_dict4 = {}
top_4= data_dtm4.sum().nlargest(N).rename_axis('word').reset_index(name='count')
top_dict4 = top_4.set_index('word').to_dict()['count']

#print(top_dict1)
#print(top_dict2)
#print(top_dict3)
#print(top_dict4)

#N = 30
#for i in [data_dtm1,data_dtm2,data_dtm3,data_dtm4]:
#    print(i.sum().nlargest(N).rename_axis('word').reset_index(name='count'))

wc1 = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42, width=800, height=400, max_words=200).generate_from_frequencies(top_dict1)
plt.rcParams['figure.figsize'] = [16, 6]
plt.imshow(wc1, interpolation="bilinear")
plt.axis("off")
plt.show()


wc2 = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42, width=800, height=400, max_words=200).generate_from_frequencies(top_dict2)
plt.rcParams['figure.figsize'] = [16, 6]
plt.imshow(wc2, interpolation="bilinear")
plt.axis("off")
plt.title('Top words Tier 2')    
plt.show()


wc3 = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42, width=800, height=400, max_words=200).generate_from_frequencies(top_dict3)
plt.rcParams['figure.figsize'] = [16, 6]
plt.imshow(wc3, interpolation="bilinear")
plt.axis("off")
plt.title('Top words Tier 3')
plt.show()


wc4 = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42, width=800, height=400, max_words=200).generate_from_frequencies(top_dict4)
plt.rcParams['figure.figsize'] = [16, 6]
plt.imshow(wc4, interpolation="bilinear")
plt.axis("off")
plt.title('Top words Tier 4')    
plt.show()






