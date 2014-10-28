from nltk.corpus import stopwords 

text= 'hello a world'

stopwordslist = set(stopwords.words('english'))
#text  = [i for i in text.split() if i not in stopwordslist]
text = [word for word in text.split() if word not in(stopwordslist)]

print text