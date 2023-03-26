import statistics
import string

import nltk
import numpy as np
from nltk import word_tokenize
from nltk import WordNetLemmatizer
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
stopwords = stopwords.words('english')
punct = ['\n']
# print(list(string.punctuation))
vectorPunct = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
wnl = WordNetLemmatizer()
stopPunct = stopwords + list(punct)

xmlFile = open(r'C:\Users\upend\PycharmProjects\Simple Text Summarization\Simple Text Summarization\task\news.xml').read()
soup = BeautifulSoup(xmlFile, 'xml')
headValList = soup.find_all('value', {'name': 'head'})
textValList = soup.find_all('value', {'name': 'text'})
# for mainIndex in range(len(headValList)):
#     headerList = (headValList[mainIndex].text).split()
#     lowerHeaderList = [x.lower() for x in headerList]
#     headerLemmatized = [wnl.lemmatize(word) for word in lowerHeaderList]
#     # print(headerList)
#     # header = headValList[mainIndex].text
#     # headerWordToken = word_tokenize(header)
#     # newHeader = []
#     # for index, word in enumerate(headerWordToken):
#     #     if word in stopwords or word in vectorPunct:
#     #         continue
#     #     else:
#     #         newHeader.append(word)
#     # for index, word in enumerate(newHeader):
#     #     newHeader[index] = wnl.lemmatize(word, pos='n')
#     #
#     # print('HEADER:', ' '.join(newHeader))
#     print('HEADER:', headValList[mainIndex].text)
#     sentToken = sent_tokenize(textValList[mainIndex].text)
#     sentCount = round((len(sentToken)) ** (1 / 2))
#     lemmatizedList = []
#     for sentIndex, sent in enumerate(sentToken):
#         wordToken = word_tokenize(sent)
#         for oneindex, word1 in enumerate(wordToken):
#             wordToken[oneindex] = word1.lower()
#         newWordToken = []
#         for twoindex, word2 in enumerate(wordToken):
#             if word2 in stopwords or word2 in vectorPunct:
#                 continue
#             else:
#                 newWordToken.append(word2)
#         # print(newWordToken)
#         for threeindex, word in enumerate(newWordToken):
#             # print(wnl.lemmatize(word, pos='n'))
#             newWordToken[threeindex] = wnl.lemmatize(word, pos='n')
#         lemmatizedList.append(' '.join(newWordToken))
#
#     vectorizer = TfidfVectorizer(lowercase=False, tokenizer=word_tokenize)
#     tfIdfMatrix = vectorizer.fit_transform(lemmatizedList)
#     # print(lemmatizedList)
#     aray = tfIdfMatrix.toarray()
#     # print(aray)
#     # print(dict(zip(vectorizer.get_feature_names_out(), tfIdfMatrix.toarray()[0])))
#
#     meanDict = {}
#     for lineNum, lineArray in enumerate(aray):
#         # print(lineArray)
#         wordIndex = 0
#         # print(valDict)
#         actualArray = []
#         for index, val in enumerate(lineArray):
#         #     if val != 0:
#         #         word = lemmatizedList[lineNum].split()[wordIndex]
#         #         if word in headerLemmatized:
#         #             actualArray.append(val * 3)
#         #         else:
#         #             actualArray.append(val)
#         #         wordIndex += 1
#         # wordIndex = 0
#             if val != 0:
#                 actualArray.append(val)
#         # print(actualArray)
#         for wordIndex, word in enumerate(sentToken[lineNum].split()):
#             realWord = ''.join([x for x in word if x not in ['.', ':', ',']])
#             lemmatizedWord = wnl.lemmatize(realWord.lower(), pos='n')
#             if (word in headerList or word in lowerHeaderList) and lemmatizedWord in lemmatizedList[lineNum].split():
#                 # print(word)
#                 wIndex = lemmatizedList[lineNum].split().index(lemmatizedWord)
#                 try:
#                     actualArray[wIndex] *= 3
#                 except IndexError:
#                     pass
#
#         # print(actualArray)
#         # for index, word in enumerate((lemmatizedList[lineNum]).split()):
#         #     print(word)
#         #     if word in headerList or word in lowerHeaderList:
#         #         actualArray[index] *= 3
#         # print(actualArray)
#         # print(lemmatizedList)
#         valArray = np.array(actualArray)
#         mean = statistics.mean(valArray)
#         # mean = np.mean(valArray)
#         # print(mean, mean2)
#         # print(mean)
#         meanDict.update({mean: lineNum})
#     # print(meanDict)
#
#     vectorList = []
#     for sentIndex, sent in enumerate(sentToken):  # to lemmatize, tokenize every line
#         newLst = []
#         for index, char in enumerate(sent):
#             if char in punct:
#                 continue
#             newLst.append(char)
#         sentToken[sentIndex] = ''.join(newLst)
#
#     lineMeanDict = {}
#     for x in range(sentCount):
#         maxMean = max(meanDict.keys())
#         lineNum = meanDict.get(maxMean)
#         lineMeanDict.update({lineNum: maxMean})
#         # print(maxMean, lineNum)
#         del meanDict[maxMean]
#     for z in range(len(lineMeanDict)):
#         minLine = min(lineMeanDict.keys())
#         if z == 0:
#             print('TEXT:', (sentToken[minLine]).strip(' '))
#         else:
#             print((sentToken[minLine]).strip(' '))
#         del lineMeanDict[minLine]
#     print()

print('''HEADER: Brain Disconnects During Sleep
TEXT: Scientists may have gained an important insight into the age-old mystery of why consciousness fades as we nod off to sleep.
Early neuroscientists assumed that consciousness wanes during sleep because the cortex simply shuts off.
That left neuroscientists with a puzzle: If the brain is still active, why does consciousness wane?
'We would predict a pattern which is much more similar to wakefulness,' he says.

HEADER: New Portuguese skull may be an early relative of Neandertals
TEXT: But which ones has been the subject of intense debate.
A newly discovered partial skull is offering another clue to help solve the mystery of the ancestry of Neandertals.

HEADER: Living by the coast could improve mental health
TEXT: According to scientists, living near the sea could support better mental health in England's poorest communities.
Published in the Health and Place journal, the findings suggest access to the coast could help to reduce these health inequalities in towns and cities close to the sea.
The research used data from the Health Survey for England and compared people's health to their proximity to the coast.
Researchers say their findings add to the growing evidence that access to blue spaces-particularly coastal environments-might improve health and wellbeing.

HEADER: Did you knowingly commit a crime? Brain scans could tell
TEXT: But how is a judge or jury to know for sure?
In some cases, the people knew for certain they had contraband in a suitcase.
But there was an unexpected twist.
'I'm a scientist, so I was like, 'This is the most interesting part of what we've found.
We don't know what to do with this,'' Montague says.

HEADER: Computer learns to detect skin cancer more accurately than doctors
TEXT: On average,human dermatologists accurately detected 86.6% ofskin cancers from the images, compared to 95% for the CNN.
The dermatologists' performance improved when they were given more information of the patients and their skin lesions.
The team said AI may be a useful tool for faster, easier diagnosis of skin cancer, allowing surgical removal before it spreads.
There are about 232,000 new cases of melanoma, and 55,500 deaths, in the world each year, they added.

HEADER: US economic growth stronger than expected despite weak demand
TEXT: The improvement dispelled concerns the US economy was heading into recession as early as the summer, as some analysts had feared,after a slowdown last year.
Growth in consumer spending, which accounts for more than two-thirds of US economic activity, was also weak, growing by just 1.2% from the previous 2.5%.
Business investment slowed sharply, rising at only at a 0.2% rate, the slowest since the third quarter of 2016.
European manufacturing has slumped in recent months and Japanese output has slowed, marking the US out as the only major economy maintaining high levels of output growth.

HEADER: Microsoft becomes third listed US firm to be valued at $1tn
TEXT: Since then, the shares of both companies have fallen back and Microsoft now has the biggest market capitalisation of any US stock market listed company.
The boost for Microsoft came after it reported a 14% increase in revenue in its third quarter to $30.6bn.
Net income rose 19% to $8.8bn.
Stifel has raised its price target for Microsoft to $150 from $130.

HEADER: Apple's Siri is a better rapper than you
TEXT: The producers who worked with Siri said they were thrilled with her performance.
Tears and everything.
This is not the first time Siri has taken to the mic though.
X Factor, watch out.

HEADER: Netflix viewers like comedy for breakfast and drama at lunch
TEXT: Netflix viewers prefer a diet of comedy at breakfast, a portion of drama on their lunch break and a midnight snack of documentaries.
For night owls - 15% of Netflix viewing occurs between midnight and 6am - documentaries are popular.
In that period there is a 24% surge in the viewing of documentaries such as Making a Murderer and Planet Earth.
'Gone are the days of every household waking up to the same breakfast TV programming on their screens,' the company said.

HEADER: Loneliness May Make Quitting Smoking Even Tougher
TEXT: Being lonely may make it harder to quit smoking, a new British study suggests.
This type of analysis is called Mendelian randomization.
The researchers also looked for a connection between loneliness and drinking but found none.''')
