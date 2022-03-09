Profanity.py is the script we can use in order to assign a degree of profanity 
to the tweets provided in the form of tweets.txt file

This script takes tweet.txt and a list containing slur words as inputs and returns a dataframe and a csv file having degree of profaninty assigned to each individual tweet
as the output

Work flow of profanity.py is given below.

- We are reading the file containing tweets, line by line.
- We are cleaning the tweets by:
      > Removing special characters and integers
      > Converting everything into lowercase
      > Removing stopwords (Prepositions, Articles, etc)
- We are removing stopwords by tokenizing the tweets into a list of words (relevant).
- We are Calculating degree of profanity with the given approach.
      > For each tweet, We are counting number of slur words present in the tweet by taking reference from slur list.
      > Then we divide the count of slur words with total number of relevant words (after removing stopword) present in the tweet
      > The outcome will give us an idea about the degree of profanity in the tweet.
- We are storing these degrees for each tweet in a CSV file along with the original tweets.



