import tweepy
from textblob import TextBlob #text/tweet parse
import re # regular expression
import pandas as pd


ck="Jm6WDXZuiwlwUnT9mFbPdSpcg"
cs="Wp4Gbf74R6MZWjXvj0ifKrCobwWbchhn53Mv8L7VMLbIUi6Wnd"
at="919434545924935681-wFjVVTbs0pmyB2VwSoj4VwGb7tBYCyr"
ats ="RaPfxU0rSMjkS3MSI9N0ztXu4I2iLMecXg79OerNHw4Ly"

auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(at, ats)

api = tweepy.API(auth)


print(api,' login success')

post = api.user_timeline(screen_name = 'NarendraModi', tweet_mode='extended')

print('Show the 5 recent tweets : \n')

i = 1

for tweet in post[0:5]:
    print(str(i) + ')' + tweet.full_text + '\n')
    i = i + 1



df = pd.DataFrame( [tweet.full_text for tweet in post] , columns=['Tweets'])
print(df.head())

def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+' , '', text)
    text = re.sub(r'#' , '', text)
    text = re.sub(r'RT[\s]+' , '', text)
    text = re.sub(r'https?:\/\/\S+' , '', text)

    return text

df['Tweets'] = df['Tweets'].apply(cleanTxt)

print(df)



def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getpolarity(text):
    return TextBlob(text).sentiment.polarity

df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['polarity'] = df['Tweets'].apply(getpolarity)

print(df)





def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

df['Analysis'] = df['polarity'].apply(getAnalysis)
print(df)





j = 1
sortedDF = df.sort_values(by=['polarity'])
for i in range(0, sortedDF.shape[0]):
    if(sortedDF['Analysis'][i] == 'Positive'):
        print(str(j) + ')'+sortedDF['Tweets'][i])
        print()
        j = j + 1



