from textblob import TextBlob
import matplotlib.pyplot as plt
import tweepy 

class SentimentAnalyzer:
    def __init__(self,tag=""):
        self.tag=tag
        self.noOfTweets=100
        self.__consumerKey = '4EZTwa0fDcUOdXMyoPzV0Symi'
        self.__consumerSecret = 'IG1rv7vIAhsqmp1HvYWuaqaNHqF0o0l0nAXwqwkFnQaIidlrXz'
        self.__accessToken = '153345272-q0iVqlZwxOEfXkLQWFfe6icWauYZALD7nqmJu3o5'
        self.__accessTokenSecret = 'LX0G6skTYIdqpTb6Mh4ciuM5kfUa67PXAMvdheKkfL5e7'
        self.neutral = 0
        self.positive = 0
        self.negative = 0
        self.perNeu = 0
        self.perPos =0
        self.perNeg = 0
    def authenticate(self):
        self.auth = tweepy.OAuthHandler(self.__consumerKey,self.__consumerSecret)
        self.auth.set_access_token(self.__accessToken,self.__accessTokenSecret)
        self.api = tweepy.API(self.auth)
    def calculatePolarity(self):
        self.tweets = tweepy.Cursor(self.api.search, q=self.tag).items(self.noOfTweets)
        for tweet in self.tweets:
            a = TextBlob(tweet.text)
            if(a.sentiment.polarity==0):
                self.neutral+=1
            elif (a.sentiment.polarity>0):
                self.positive+=1
            elif (a.sentiment.polarity<0):
                self.negative+=1
        self.__percentage()
    def __percentage(self):
        self.perNeu = format(100 * self.neutral/self.noOfTweets,'.2f')
        self.perNeg = format(100 * self.negative/self.noOfTweets,'.2f')
        self.perPos = format(100 * self.positive/self.noOfTweets,'.2f')
    def generateGraph(self):
        labels = ['Positive '+str(self.perPos)+'%','Neutral '+str(self.perNeu)+'%','Negative '+str(self.perNeg)+'%']
        size = [self.perPos,self.perNeu,self.perNeg]
        colors = ['lightskyblue','yellowgreen','red']
        patches, texts = plt.pie(size, colors=colors, shadow=True, startangle=90)
        plt.title('Twitter\'s Reaction on '+self.tag.upper())
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()


