import string
import nltk
from nltk import WordNetLemmatizer
from nltk import word_tokenize
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

nltk.download('wordnet')
nltk.download('stopwords')
stopwords = stopwords.words('english')
punct = string.punctuation
wnl = WordNetLemmatizer()
xmlFile = open(r'C:\Users\upend\PycharmProjects\Simple Text Summarization\Simple Text Summarization\task\news.xml').read()
soup = BeautifulSoup(xmlFile, 'xml')
headValList = soup.find_all('value', {'name': 'head'})
textValList = soup.find_all('value', {'name': 'text'})
for index in range(len(headValList)):
    print('HEADER:', headValList[index].text)
    sentToken = sent_tokenize(textValList[index].text)
    sentCount = round((len(sentToken)) ** (1 / 2))
    for sentIndex, sent in enumerate(sentToken[:sentCount]):
        wordToken = word_tokenize(sent)
        for oneindex, word1 in enumerate(wordToken):
            wordToken[oneindex] = word1.lower()
        newWordToken = []
        for twoindex, word2 in enumerate(wordToken):
            if word2 in stopwords or word2 in punct:
                continue
            else:
                newWordToken.append(word2)
        for threeindex, word in enumerate(newWordToken):
            newWordToken[threeindex] = wnl.lemmatize(word, pos='n')
        if sentIndex == 0:
            print('TEXT:', ' '.join(newWordToken))
        else:
            print(' '.join(newWordToken))
    print()
