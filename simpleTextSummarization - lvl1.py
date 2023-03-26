from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

xmlFile = open('news.xml', 'r').read()
soup = BeautifulSoup(xmlFile, 'xml')
headValList = soup.find_all('value', {'name': 'head'})
textValList = soup.find_all('value', {'name': 'text'})
for index in range(len(headValList)):
    print('HEADER:', headValList[index].text)
    token = sent_tokenize(textValList[index].text)
    textValRange = round((len(token)) ** (1 / 2))
    print('TEXT:', token[0])
    for textIndex in range(1, textValRange):
        print(token[textIndex])
    print()
