import  nltk
from nltk.tokenize import word_tokenize

train = [("this  is a good boy.","pos"),
           ("python is a good program.","neg"),
           ("python is not secure.","pos")
         ]

dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))

t = [({word:(word in word_tokenize(x[0]))for word in dictionary},x[1])for x in train]

classifier = nltk.NaiveBayesClassifier.train(t)
test_data ="Manchurian was hot and spicy"
test_data_features = {word.lower():(word in word_tokenize(test_data.lower()))for word in dictionary}
print(classifier.classify(test_data_features))
