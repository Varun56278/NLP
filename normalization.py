# 1. Normalizing Text
text = "An essay is, generally, a piece of writing that gives the author's own argument, but the definition is vague, overlapping with those of a letter, a paper, an article, a pamphlet, d a hort story. Essays have traditionally been sub-classified as formal and informal. Formal essays are"

text = text.lower()

print(text)

# 2. Removing Unicode Characters

import re

text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)

print(text)

# 3. Removing Stopwords
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords

stop = stopwords.words('english')
text = "my package from amazon never arrived fix this asap"
text = " ".join([word for word in text.split() if word not in (stop)])

print(text)


