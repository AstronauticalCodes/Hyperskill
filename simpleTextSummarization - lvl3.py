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
for index in range(len(headValList)):
    print('HEADER:', headValList[index].text)
    sentToken = sent_tokenize(textValList[index].text)
    sentCount = round((len(sentToken)) ** (1 / 2))
    lemmatizedList = []
    for sentIndex, sent in enumerate(sentToken):
        wordToken = word_tokenize(sent)
        for oneindex, word1 in enumerate(wordToken):
            wordToken[oneindex] = word1.lower()
        newWordToken = []
        for twoindex, word2 in enumerate(wordToken):
            if word2 in stopwords or word2 in vectorPunct:
                continue
            else:
                newWordToken.append(word2)
        for threeindex, word in enumerate(newWordToken):
            newWordToken[threeindex] = wnl.lemmatize(word, pos='n')
        lemmatizedList.append(' '.join(newWordToken))
    # print(lemmatizedList)
    # print(sentToken)
    #     wordToken = word_tokenize(sent)
    #     # for oneindex, word1 in enumerate(wordToken):
    #     #     wordToken[oneindex] = word1.lower()
    #     newWordToken = []
    #     for twoindex, word2 in enumerate(wordToken):
    #         if word2 in stopwords or word2 in punct or word2.lower() in stopwords or word2.lower() in punct:
    #             continue
    #         else:
    #             newWordToken.append(word2)
    #     for threeindex, word in enumerate(newWordToken):
    #         newWordToken[threeindex] = wnl.lemmatize(word, pos='n')
    #     lemmatizedList.append(' '.join(newWordToken))
    # print(lemmatizedList)
    # for sent in sentToken:
    # sentList = [sentToken[10]]
    vectorizer = TfidfVectorizer(lowercase=False, tokenizer=word_tokenize)
    tfIdfMatrix = vectorizer.fit_transform(lemmatizedList)

    aray = tfIdfMatrix.toarray()
    # print(aray)
    # print(dict(zip(vectorizer.get_feature_names_out(), tfIdfMatrix.toarray()[0])))
    meanDict = {}
    for lineNum, lineArray in enumerate(aray):
        actualArray = []
        for val in lineArray:
            if val != 0:
                actualArray.append(val)
        # print(actualArray)
        valArray = np.array(actualArray)
        # print(valArray)
        mean = statistics.mean(valArray)
        # mean = np.mean(valArray)
        # print(mean, mean2)
        # print(mean)
        meanDict.update({mean: lineNum})
    # print(meanDict)

    vectorList = []
    for sentIndex, sent in enumerate(sentToken):  # to lemmatize, tokenize every line
        # # for sentIndex, sent in enumerate(sentToken[:sentCount]):
        newLst = []
        for index, char in enumerate(sent):
            if char in punct:
                continue
            newLst.append(char)
        sentToken[sentIndex] = ''.join(newLst)

    lineMeanDict = {}
    for x in range(sentCount):
        maxMean = max(meanDict.keys())
        lineNum = meanDict.get(maxMean)
        lineMeanDict.update({lineNum: maxMean})
        # print(maxMean, lineNum)
        del meanDict[maxMean]
    # print(lineMeanDict)
    for z in range(len(lineMeanDict)):
        minLine = min(lineMeanDict.keys())

        # kentinew = False
        # for z in sentToken[lineNum]:
        #     if z in string.ascii_letters:
        #         kentinew = True
        #         break
        # if kentinew:
        # print(sentToken[lineNum])
        if z == 0:
            print('TEXT:', sentToken[minLine])
        else:
            print(sentToken[minLine])
        del lineMeanDict[minLine]
        # kentinew = False
    print()
#     # exit()
# print('''HEADER: Brain Disconnects During Sleep
# TEXT: Early neuroscientists assumed that consciousness wanes during sleep because the cortex simply shuts off.
# That left neuroscientists with a puzzle: If the brain is still active, why does consciousness wane?
# Tononi has spent years developing a theory that equates consciousness with the integration of information.
# 'We would predict a pattern which is much more similar to wakefulness,' he says.
#
# HEADER: New Portuguese skull may be an early relative of Neandertals
# TEXT: But which ones has been the subject of intense debate.
# A newly discovered partial skull is offering another clue to help solve the mystery of the ancestry of Neandertals.
#
# HEADER: Living by the coast could improve mental health
# TEXT: According to scientists, living near the sea could support better mental health in England's poorest communities.
# Researchers from the University of Exeter used survey data from 25,963 respondents in their investigations into the wellbeing effects of being by the coast.
# The research used data from the Health Survey for England and compared people's health to their proximity to the coast.
# Researchers say their findings add to the growing evidence that access to blue spaces-particularly coastal environments-might improve health and wellbeing.
#
# HEADER: Did you knowingly commit a crime? Brain scans could tell
# TEXT: But how is a judge or jury to know for sure?
# In some cases, the people knew for certain they had contraband in a suitcase.
# But there was an unexpected twist.
# 'I'm a scientist, so I was like, 'This is the most interesting part of what we've found.
# We don't know what to do with this,'' Montague says.
#
# HEADER: Computer learns to detect skin cancer more accurately than doctors
# TEXT: 'Most dermatologists were outperformed by the CNN, the research team wrote in a paper published in the journal Annals of Oncology.
# On average,human dermatologists accurately detected 86.6% of skin cancers from the images, compared to 95% for the CNN.
# The dermatologists' performance improved when they were given more information of the patients and their skin lesions.
# There are about 232,000 new cases of melanoma, and 55,500 deaths, in the world each year, they added.
#
# HEADER: US economic growth stronger than expected despite weak demand
# TEXT: The improvement dispelled concerns the US economy was heading into recession as early as the summer, as some analysts had feared,after a slowdown last year.
# Growth in consumer spending, which accounts for more than two-thirds of US economic activity, was also weak, growing by just 1.2% from the previous 2.5%.
# Business investment slowed sharply, rising at only at a 0.2% rate, the slowest since the third quarter of 2016.
# In April, British factories have stockpiled at the fastest pace since records began in the 1950s amid reports they were increasingly downbeat about their prospects.
#
# HEADER: Microsoft becomes third listed US firm to be valued at $1tn
# TEXT: The boost for Microsoft came after it reported a 14% increase in revenue in its third quarter to $30.6bn.
# Net income rose 19% to $8.8bn.
# Apple is worth around $970bn and Amazon is close behind at $940bn.
# Stifel has raised its price target for Microsoft to $150 from $130.
#
# HEADER: Apple's Siri is a better rapper than you
# TEXT: The producers who worked with Siri said they were thrilled with her performance.
# When I asked her to read them out, well that was when the real ROFL-ing started.
# Tears and everything.
# X Factor, watch out.
#
# HEADER: Netflix viewers like comedy for breakfast and drama at lunch
# TEXT: For night owls - 15% of Netflix viewing occurs between midnight and 6am - documentaries are popular.
# In that period there is a 24% surge in the viewing of documentaries such as Making a Murderer and Planet Earth.
# 'Gone are the days of every household waking up to the same breakfast TV programming on their screens,' the company said.
# 'When viewing schedules are set by people and not programmers, lunchtime becomes no bingeing exception.'
#
# HEADER: Loneliness May Make Quitting Smoking Even Tougher
# TEXT: This type of analysis is called Mendelian randomization.
# Treur is a visiting research associate from Amsterdam UMC.
# The report was published June 16 in the journal Addiction.''')
