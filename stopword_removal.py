import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')


def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text)

    filtered_sentence = [word for word in word_tokens if not word in stop_words]

    return filtered_sentence


text = "This is a sample sentence, showing off the stop words filtration."

print(remove_stopwords(text))
