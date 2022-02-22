import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

paragraph = """An essay is, generally, a piece of writing that
gives the author's own argument, but the definition is vague,
overlapping with those of a letter, a paper, an article, a pamphlet,
and a short story. Essays have traditionally been sub-classified as
formal and informal. Formal essays are characterized by serious purpose,
dignity, logical organization, length, whereas the informal essay is
characterized by the personal element (self-revelation, individual
tastes and experiences, confidential manner), humor, graceful style,
rambling structure, unconventionality or novelty of theme Essays are
commonly used as literary criticism, political manifestos, learned
arguments, observations of daily life, recollections, and reflections
of the author. Almost all modern essays are written in prose, but works
in verse have been dubbed essays. While brevity usually defines an essay,
voluminous works like John Locke's An Essay Concerning Human Understanding
and Thomas Malthus's An Essay on the Principle of Population are counter
examples. In some countries, essays have become a major part of formal
education. Secondary students are taught structured essay formats to
improve their writing skills; admission essays are often used by universities
dfain selecting applicants, and in the humanities and social sciences essays
are often used as a way of assessing the performance of students during
final exams. The concept of an "essay" has been extended to other media
beyond writing. A film essay is a movie that often incorporates documentary
filmmaking styles and focuses more on the evolution of a theme or idea.
A photographic essay covers a topic with a linked series of photographs
that may have accompanying text or captions."""


sentences = nltk.sent_tokenize(paragraph)
#print(sentence)


#words = nltk.word_tokenize(paragraph)
#print(words)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words =[stemmer.stem(word)for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ''.join(words)
    print(sentences[i])



for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words =[lemmatizer.lemmatize(word)for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ''.join(words)
    print(sentences[i])
