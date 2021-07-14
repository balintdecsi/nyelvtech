import spacy

nlp = spacy.load("en_core_web_md")  # make sure to use larger package!
doc1 = nlp("A deficiency of folate increases blood levels of homocysteine.")
doc2 = nlp("Fasting blood samples for serum homocysteine and serum folate analysis were taken initially, after 3 months of supplementation, and 3 months after folic acid use was discontinued.")
span1 = doc1[3:5]

# Similarity of two documents
print(doc1, "<->", doc2, doc1.similarity(doc2))
# Similarity of tokens and spans
french_fries = doc1[2:4]
burgers = doc1[5]
print(french_fries, "<->", burgers, french_fries.similarity(burgers))

print(span1)



exit()

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_md")
doc = nlp("50 percent of patients exposed to radiation have activated markers of mesenchymal stem cells.")
for token in doc:
    print(token.text, token.pos_, token.tag_)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


exit()

nlp = spacy.load("en_core_web_md")
doc = nlp("50 percent of patients exposed to radiation have activated markers of mesenchymal stem cells.")
# for token in doc:
#     print(token.text, token.has_vector, token.vector_norm, token.is_oov)

exit()

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a hand-on example from the U.K. spaCy site. This is Google. Google it if you dare.")
for token in doc:
    print(token.text, token.pos_, token.tag_)


for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

displacy.serve(doc, style="ent")

exit(0)

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a hand-on example from the U.K. spaCy site. Google it if you dare.")
for token in doc:
    print(token.text)