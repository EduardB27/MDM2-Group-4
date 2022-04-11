import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
def common_words(l_ist):
    c_word=["the","The","was","to","and","a","room","in","not","of","very","for","I","is","it","hotel","no","t","on","were","but","we","had","with","at","that","my","as","this","have","so","No","Room","there","too","rooms","bit","could","from","they","be","you","all","poor","are","out","one","night"]
    for x in l_ist[:]:
        if x in c_word:
            l_ist.remove(x)
i=0
# Takes the data of Tier4 in the format of hotel, review, score with each review in its own row
# Needs to be changed for each tier
excel="Tier4_SA.csv"
df=pd.read_csv(excel)
print(df)

# lists to append to
review_scores=[]
score_1=[]
score_2=[]
score_3=[]
score_4=[]
review_1=[]
review_2=[]
review_3=[]
review_4=[]
while i!=len(df):
    review_scores.append([df.iloc[i,2],df.iloc[i,3]])
    i+=1
# Appends to review_scores in form review,score

# splits review into 4 tiers based on score. Tier 4 is least negative, tier 1 is most negative
for y,x in review_scores:
    if -0.25<x<=0:
        score_4.append(x)
        review_4.append(y)
    elif -0.5<x<=-0.25:
        score_3.append(x)
        review_3.append(y)
    elif -0.75<x<=-0.5:
        score_2.append(x)
        review_2.append(y)
    elif -1<=x<=-0.75:
        score_1.append(x)
        review_1.append(y)
        
# each set of sentiment organised scores is put together 
r4="".join(review_4)
r3="".join(review_3)
r2="".join(review_2)
r1="".join(review_1)


# 4 paragraphs of code split the combined code into a list then removes most common words
# Using func from top. Then finds most common words
r4=r4.split()
common_words(r4)
r4=Counter(r4)
r4=r4.most_common(5)
print(r4)

r3=r3.split()
common_words(r3)
r3=Counter(r3)
r3=r3.most_common(5)
print(r3)

r2=r2.split()
common_words(r2)
r2=Counter(r2)
r2=r2.most_common(5)
print(r2)

r1=r1.split()
common_words(r1)
r1=Counter(r1)
r1=r1.most_common(5)
print(r1)

# =============================================================================
# Final part of code puts things into a format which can be plotted as a bar chart
# =============================================================================

x4=[]
y4=[]
x3=[]
y3=[]
x2=[]
y2=[]
x1=[]
y1=[]
for i in r4:
    x4.append(i[0])
    y4.append(i[1])

for i in r3:
    x3.append(i[0])
    y3.append(i[1])
    
for i in r2:
    x2.append(i[0])
    y2.append(i[1])
    
for i in r1:
    x1.append(i[0])
    y1.append(i[1])
    
    
fig, ax=plt.subplots(2,2)


ax[0,0].bar(x4,y4)
ax[0,0].set_title("Most common words in Tier4 reviews")
ax[0,0].set_xlabel("words")
ax[0,0].set_ylabel("frequency")

ax[0,1].bar(x3,y3)
ax[0,1].set_title("Most common words in Tier3 reviews")
ax[0,1].set_xlabel("words")
ax[0,1].set_ylabel("frequency")

ax[1,0].bar(x2,y2)
ax[1,0].set_title("Most common words in Tier2 reviews")
ax[1,0].set_xlabel("words")
ax[1,0].set_ylabel("frequency")

ax[1,1].bar(x1,y1)
ax[1,1].set_title("Most common words in Tier1 reviews")
ax[1,1].set_xlabel("words")
ax[1,1].set_ylabel("frequency")

plt.show()