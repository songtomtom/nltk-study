import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')  # For tokenization

def pos_tagging(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    return tagged_words


text = "Despite the hardships and challenges, he did not give up on his dreams."
text = "The sun rises up in the east and sets down in the west."
text = "He climbed up the stairs to reach the rooftop terrace."
text = "I'm up for whatever."
text = "There are flights to Seoul."
text = "He tends to worry too much about the small details."
text = "I waited about for an hour, but they didn't come."
text = "They enter into an agreement with their rivals."
text = "Could you put me through to extension 259 please."

tagged_words = pos_tagging(text)

print(tagged_words)
