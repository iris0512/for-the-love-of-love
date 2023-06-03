import nltk
from nltk.corpus import webtext
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import pandas as pd
import os
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('webtext')
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

path = 'YOUR PATH HERE'

def readFile(name):
    with open(file_path,'r',encoding='utf-8') as f:
        lines = str(f.readlines())
        file_cleaned = re.findall('\w+',lines)
        file_new = " ".join(file_cleaned)
        script = word_tokenize(file_new)
    return script

def getWords(script,row_words):
    words = []
    sw = nltk.corpus.stopwords.words('english')
    for s in script:
        words.append(s.lower())
    words_final = []
    for word in words:
        if word in list(rom_words['words']):
            words_final.append(word)
    return words_final


def wordAnalysis(words,title):
    data_analysis = nltk.FreqDist(words)
    df_temp = pd.DataFrame(list(data_analysis.items()),columns = ['words','word_freq'])
    df_temp['movie'] = title
    return df_temp


def getMovieAnalysis(files_list,rom_words):
    sid = SentimentIntensityAnalyzer()
    scores_data = []
    movies_freq = pd.DataFrame(columns=['words','word_freq','movie'])
    for n in range(len(files_list)):
        scores_row = []
        movie = path+files_list[n]
        title = files_list[n].replace('.html.txt','').replace('-',' ')
        print(title)
        scores_row.append(title)
        script = readFile(movie)
        words = getWords(script,rom_words)
        df_temp = wordAnalysis(words,title)
        pol_scores = sid.polarity_scores(" ".join(words))
        for key in pol_scores.keys():
            scores_row.append(pol_scores[key])
        movies_freq = movies_freq.append(df_temp)
        scores_data.append(scores_row)
    return movies_freq, scores_data


files_list = [f for f in os.listdir(path)]
rom_words = pd.read_csv(path+'words.csv')
list_words = rom_words['words']

movies_freq, scores_data = getMovieAnalysis(files_list,rom_words)
movies_freq.head()
col_names = ['Name','Negative','Neutral','Positive','Compound']
scores_df = pd.DataFrame(data=scores_data,columns=col_names)
movies_freq.to_csv(path+'movies_freq.csv')
scores_df.to_csv(path+'scores_sentiment.csv')