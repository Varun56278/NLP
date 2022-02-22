import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
import re
import nltk


messages = pd.read_csv('SMSSpamCollection.tsv', sep='\t',
                           names=["label", "message"])

print(messages.head(8))
print(messages.info())
print(messages.describe())
messages['Length'] = messages['message'].apply(len)
print(messages.head(8))
print(messages.groupby('label').count())
print(messages['Length'].describe())

ps = PorterStemmer()
corpus = []
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    
    
# Creating the Bag of Words model

cv = CountVectorizer(max_features=2500)
X = cv.fit_transform(corpus).toarray()

y=pd.get_dummies(messages['label'])
y=y.iloc[:,1].values


# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Training model using Naive bayes classifier





NB = MultinomialNB()
print(NB)
spam_detect_model = NB.fit(X_train, y_train)



y_pred=spam_detect_model.predict(X_test)
print(y_pred)


accuracyScore = accuracy_score(y_test,y_pred)*100
print("Prediction Accuracy :",accuracyScore)

msg = input("Enter Message: ")
msgInput = cv.transform([msg])
print(msgInput)
predict = NB.predict(msgInput)
if(predict[0]==0):
    print("NotSpam")
else:
    print("spam")
    
