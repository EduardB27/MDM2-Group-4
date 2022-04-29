# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 00:32:32 2022

@author: sm20698
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:31:49 2022

@author: sm20698
"""
import spacy


import pandas as pd
import nltk
import pickle
from sklearn.feature_extraction.text import CountVectorizer
#from IPython import embed 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt 
from gensim import matutils, models
import scipy.sparse
from nltk import word_tokenize, pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction import text
import spacy 
from nltk.corpus import stopwords


#we firstly have to create a file path to access our spreadsheet
excel_file_path = 'Hotel_Reviews.csv'

df = pd.read_csv(excel_file_path)

#this gives all the negative reviews for our group of lowest tier hotels
tier4_hotel = df.loc[df['Hotel_Name'].isin(['Bloomsbury Palace Hotel', 'Hotel Cavendish','The Tophams Hotel']),['Hotel_Name', 'Positive_Review']]
tier4_hotel.to_excel('Tier4_Hotels.xlsx',index=False )
excel_file_path_4 = 'Tier4_Hotels.xlsx'
df4 = pd.read_excel(excel_file_path_4)
#now we merge all the negative reviews into a single row for each hotel
df4['Positive_Review'] = df4.groupby(['Hotel_Name'])['Positive_Review'].transform(lambda x : ' '.join(x))
df4 = df4.drop_duplicates(subset=['Hotel_Name', 'Positive_Review'])   


########### REPEAT FOR THE OTHER TIERS
tier3_hotel = df.loc[df['Hotel_Name'].isin(['Park Lane Mews Hotel', 'Kube Hotel Ice Bar','Hilton London Olympia','Mercure London Paddington Hotel','Le Meridien Piccadilly']),['Hotel_Name', 'Positive_Review']]
tier3_hotel.to_excel('Tier3_Hotels.xlsx',index=False)
excel_file_path_3 = 'Tier3_Hotels.xlsx'
df3 = pd.read_excel(excel_file_path_3)
df3['Positive_Review'] = df3.groupby(['Hotel_Name'])['Positive_Review'].transform(lambda x : ' '.join(x))
df3 = df3.drop_duplicates(subset=['Hotel_Name', 'Positive_Review'])

tier2_hotel = df.loc[df['Hotel_Name'].isin(['The Principal London', 'The Park Tower Knightsbridge a Luxury Collection Hotel','Park Plaza County Hall London','Novotel London Tower Bridge',' Park Grand London Lancaster Gate']),['Hotel_Name', 'Positive_Review']]
tier2_hotel.to_excel('Tier2_Hotels.xlsx',index=False)
excel_file_path_2 = 'Tier2_Hotels.xlsx'
df2 = pd.read_excel(excel_file_path_2)
df2['Positive_Review'] = df2.groupby(['Hotel_Name'])['Positive_Review'].transform(lambda x : ' '.join(x))
df2 = df2.drop_duplicates(subset=['Hotel_Name', 'Positive_Review']) 

tier1_hotel = df.loc[df['Hotel_Name'].isin(['The Nadler Soho', 'Staybridge Suites London Vauxhall',' Covent Garden Hotel','Haymarket Hotel','Ritz Paris']),['Hotel_Name', 'Positive_Review']]
tier1_hotel.to_excel('Tier1_Hotels.xlsx',index=False)
excel_file_path_1 = 'Tier1_Hotels.xlsx'
df1 = pd.read_excel(excel_file_path_1)
df1['Positive_Review'] = df1.groupby(['Hotel_Name'])['Positive_Review'].transform(lambda x : ' '.join(x))
df1 = df1.drop_duplicates(subset=['Hotel_Name', 'Positive_Review'])  

#DATA CLEANING
#REMOVING ALL SPECIAL CHARACTERS
spec_chars = ["!",'"',"#","%","&","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–", "No Positive", "Nothing"]
for char in spec_chars:
    df1['Positive_Review'] = df1['Positive_Review'].str.replace(char, ' ')
    df2['Positive_Review'] = df2['Positive_Review'].str.replace(char, ' ')
    df3['Positive_Review'] = df3['Positive_Review'].str.replace(char, ' ')
    df4['Positive_Review'] = df4['Positive_Review'].str.replace(char, ' ')

#MAKING EVERYTHING LOWERCASE
df1['Positive_Review'] = df1['Positive_Review'].map(lambda x: x.lower() if isinstance(x,str) else x)
df2['Positive_Review'] = df2['Positive_Review'].map(lambda x: x.lower() if isinstance(x,str) else x)
df3['Positive_Review'] = df3['Positive_Review'].map(lambda x: x.lower() if isinstance(x,str) else x)
df4['Positive_Review'] = df4['Positive_Review'].map(lambda x: x.lower() if isinstance(x,str) else x)

#Remove numbers
df1['Positive_Review'] = df1['Positive_Review'].str.replace('\w*\d\w*', '')
df2['Positive_Review'] = df2['Positive_Review'].str.replace('\w*\d\w*', '')
df3['Positive_Review'] = df3['Positive_Review'].str.replace('\w*\d\w*', '')
df4['Positive_Review'] = df4['Positive_Review'].str.replace('\w*\d\w*', '')

df1.to_excel('Tier_1_Positive.xlsx',index=False)
df2.to_excel('Tier_2_Positive.xlsx',index=False)
df3.to_excel('Tier_3_Positive.xlsx',index=False)
df4.to_excel('Tier_4_Positive.xlsx',index=False)


#CREATE CORPUS



stop_words = nltk.corpus.stopwords.words('english')
new_words=("bit","didn","like","good","did","just","wasn", 

                  "did","could","would","also","get","us", 

                  "even","really","one","everything","nothing", 

                  "needs","work","next","quite","think","asked","got","need", 

                  "well", "stay","ok”, ""however" ,"rather","anything","although","though", 

                  "find","time","thing")
for i in new_words:
    stop_words.append(i)

cv = CountVectorizer(stop_words=stop_words)
data_cv1= cv.fit_transform(df1['Positive_Review'])
data_dtm1 = pd.DataFrame(data_cv1.toarray(), columns=cv.get_feature_names_out())
data_dtm1.index = df1.index
data_dtm1.to_excel('new_positive_data1.xlsx')
 
cv = CountVectorizer(stop_words=stop_words)
data_cv2= cv.fit_transform(df2['Positive_Review'])
data_dtm2 = pd.DataFrame(data_cv2.toarray(), columns=cv.get_feature_names_out())
data_dtm2.index = df2.index
data_dtm2.to_excel('new_positive_data2.xlsx')

cv = CountVectorizer(stop_words=stop_words)
data_cv3= cv.fit_transform(df3['Positive_Review'])
data_dtm3 = pd.DataFrame(data_cv3.toarray(), columns=cv.get_feature_names_out())
data_dtm3.index = df3.index
data_dtm3.to_excel('new_positive_data3.xlsx')

cv = CountVectorizer(stop_words=stop_words)
data_cv4= cv.fit_transform(df4['Positive_Review'])
data_dtm4 = pd.DataFrame(data_cv4.toarray(), columns=cv.get_feature_names_out())
data_dtm4.index = df4.index
data_dtm4.to_excel('new_positive_data4.xlsx')


N=70
top_dict1 = {}
top_1= data_dtm1.sum().nlargest(N).rename_axis('word').reset_index(name='count')
top_dict1 = top_1.set_index('word').to_dict()['count']
# create list of strings
list_of_strings = [ f'{key} : {top_dict1[key]}' for key in top_dict1 ]
# write string one by one adding newline
with open('Tier 1 Total Count Most Positive.txt', 'w') as my_file:
    [ my_file.write(f'{st}\n') for st in list_of_strings ]
    
    
top_dict2 = {}
top_2= data_dtm2.sum().nlargest(N).rename_axis('word').reset_index(name='count')
top_dict2 = top_2.set_index('word').to_dict()['count']
# create list of strings
list_of_strings = [ f'{key} : {top_dict2[key]}' for key in top_dict2 ]
# write string one by one adding newline
with open('Tier 2 Total Count Most Positive.txt', 'w') as my_file:
    [ my_file.write(f'{st}\n') for st in list_of_strings ]
    
    
    
top_dict3 = {}
top_3= data_dtm3.sum().nlargest(N).rename_axis('word').reset_index(name='count')
top_dict3 = top_3.set_index('word').to_dict()['count']
# create list of strings
list_of_strings = [ f'{key} : {top_dict3[key]}' for key in top_dict3 ]
# write string one by one adding newline
with open('Tier 3 Total Count Most Positive.txt', 'w') as my_file:
    [ my_file.write(f'{st}\n') for st in list_of_strings ]
    
    
top_dict4 = {}
top_4= data_dtm4.sum().nlargest(N).rename_axis('word').reset_index(name='count')
top_dict4 = top_4.set_index('word').to_dict()['count']
# create list of strings
list_of_strings = [ f'{key} : {top_dict4[key]}' for key in top_dict4 ]
# write string one by one adding newline
with open('Tier 4 Total Count Most Positive.txt', 'w') as my_file:
    [ my_file.write(f'{st}\n') for st in list_of_strings ]
    

wc1 = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42, width=800, height=400, max_words=200).generate_from_frequencies(top_dict1)
plt.rcParams['figure.figsize'] = [16, 6]
plt.imshow(wc1, interpolation="bilinear")
plt.axis("off")
font = {'family':'cursive','color':'black','size':20}
plt.title('Tier 1 Hotels', fontweight='bold', fontdict = font, pad=20) 
plt.savefig('Top Positive Words Tier 1.jpeg')
plt.show()


wc2 = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42, width=800, height=400, max_words=200).generate_from_frequencies(top_dict2)
plt.rcParams['figure.figsize'] = [16, 6]
plt.imshow(wc2, interpolation="bilinear")
plt.axis("off")
font = {'family':'cursive','color':'black','size':20}
plt.title('Tier 2 Hotels', fontweight='bold', fontdict = font, pad=20) 
plt.savefig('Top Positive words Tier 2.jpeg')
plt.show()


wc3 = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42, width=800, height=400, max_words=200).generate_from_frequencies(top_dict3)
plt.rcParams['figure.figsize'] = [16, 6]
plt.imshow(wc3, interpolation="bilinear")
plt.axis("off")
font = {'family':'cursive','color':'black','size':20}
plt.title('Tier 3 Hotels', fontweight='bold', fontdict = font, pad=20) 
plt.savefig('Top Positive Words Tier 3.jpeg')
plt.show()


wc4 = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42, width=800, height=400, max_words=200).generate_from_frequencies(top_dict4)
plt.rcParams['figure.figsize'] = [16, 6]
plt.imshow(wc4, interpolation="bilinear")
plt.axis("off")
font = {'family':'cursive','color':'black','size':20}
plt.title('Tier 4 Hotels', fontweight='bold', fontdict = font, pad=20) 
plt.savefig('Top Positive Words Tier 4.jpeg')
plt.show()
