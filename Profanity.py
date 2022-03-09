from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import pandas as pd

# Assuming a given text file containing tweets, as "tweets.txt"
file = open('tweets.txt', 'r')
Lines = file.readlines()

# Assuming a list containing racial slurs as 'slurs'
slurs = []

stop_words = set(stopwords.words('english'))

# Initiating a list "ans" which will contain the degree of profanity, ordered as tweets.
ans = []

for i in Lines:

    # Removing all special character and integers and converting to lowercase.
    line = re.sub('[^A-Za-z ]+', '', i.lower())

    # Tokenizing into words and removing stopwords
    word_tokens = word_tokenize(line)
    sentence = [i for i in word_tokens if not i in stop_words]

    n = len(sentence)
    score = 0

    for j in sentence:
        if j in slurs:
            score+=1

    # Degree defines degree of profanity
    degree = score/n
    ans.append(degree)

# Creating a dataframe to visualize and store calculated degree of profanity along with respective tweets,
# with columns as "tweets" and "degree".
df = pd.DataFrame({'tweets': Lines , 'degree': ans})

# Saving the dataframe in CSV format.
df.to_csv('proanity.csv')
print(df)
