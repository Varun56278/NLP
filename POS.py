import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

sw = set(stopwords.words("english"))

quote = "An essay is generally a piece of writing that gives the authors own argument but the definition is vague overlapping with those of a letter a paper an article a pamphlet ort story. Essays have traditionally"
tokenized = sent_tokenize(quote)
print(tokenized)

for i in tokenized:
    word_list = nltk.word_tokenize(i)
    word_list = [w for w in word_list if not w in sw]
    tagged = nltk.pos_tag(word_list)
    print(tagged)