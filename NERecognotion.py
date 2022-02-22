import spacy
nlp = spacy.load("en_core_web_sm")
fact = "An essay is, generally, a piece of writing that gives the author's own argument, but the definition is vague"

doc = nlp(fact)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)