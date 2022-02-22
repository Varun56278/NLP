import  nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

reviews = ['this  is a good boy','python is a good program','python is not secure']

sid=SentimentIntensityAnalyzer()

for sentence in reviews:
    print(sentence)

ss = sid.polarity_scores(sentence)
for k in ss:
    print('{0}:{1},'.format(k,ss[k]), end= '')
print()




