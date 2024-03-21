import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')  # For tokenization


def pos_tagging(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    return tagged_words


texts = ["Despite the hardships and challenges, he did not give up on his dreams.",
         "The sun rises up in the east and sets down in the west.",
         "He climbed up the stairs to reach the rooftop terrace.",
         "I'm up for whatever.",
         "There are flights to Seoul.",
         "He tends to worry too much about the small details.",
         "I waited about for an hour, but they didn't come.",
         "They enter into an agreement with their rivals.",
         "Could you put me through to extension 259 please."]

# colors
highlights = {'VB': '\033[92m', 'IN': '\033[93m', 'RP': '\033[91m'}
end_color = '\033[0m'

for text in texts:
    tagged_words = pos_tagging(text)

    highlighted_sentence = []

    for word, tag in tagged_words:
        # here all tags starting from 'VB', 'IN' and 'RP' tags will be colored
        tag_start = tag[:2]
        if tag_start in highlights.keys():
            word = highlights[tag_start] + word + end_color

        highlighted_sentence.append(word)

    print(' '.join(highlighted_sentence))
