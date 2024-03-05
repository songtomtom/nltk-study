import nltk

nltk.download('punkt')  # For tokenization
nltk.download('averaged_perceptron_tagger')  # For POS tagging
nltk.download('wordnet')  # For lemmatization

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


# Original text
# text = "This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."
# text = "they are built up over time from their past uses in particular contexts by particular groups of participants in the accomplishment of particular goals that, in turn, are shaped by myriad cultural, historical and institutional forces."
# text = "However, human reasoning is still notoriously prone to confusion and error when causal questions become sufficiently complex, such as when it comes to assessing the impact of policy interventions across society."
text = "Children, men, women, and people walked with their feet, showing their teeth as they laughed at the geese, mice, and sheep."# Tokenization
tokenized_text = word_tokenize(text)

# POS tagging
pos_tagged = nltk.pos_tag(tokenized_text)

# Lemmatization with POS tagging
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tagged]

# Print the lemmatized text
print(" ".join(lemmatized))
