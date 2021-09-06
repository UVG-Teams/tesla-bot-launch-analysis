import tweepy, json, xlsxwriter

try:
    access_token = '723857363392851969-43F1DgxrLdiEfaMn5KubWt1VI7FkRHa'
    access_token_secret = 'gmCABAHGF07eZ5cibLcYcNZ1xWO2GLpIZta4sdzfJRfd2'
    consumer_key = 'kjLXsYD27YLPR4r5KWP4GeHLT'
    consumer_secret = 'UqzQyqnf8u6TPVGPQo9pwJZJHzs63GXmfkjpP9nrfgW0ZqASrD'

    auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
except:
    raise "Error de autenticacion"

tweet_list=[]
class MyStreamListener(tweepy.StreamListener):
    def __init__(self,api=None):
        super(MyStreamListener,self).__init__()
        self.num_tweets=0
        self.file=open("tweet.txt","w")
    def on_status(self,status):
        workbook = xlsxwriter.Workbook('tweets.xlsx')
        worksheet = workbook.add_worksheet()
        tweet=status._json
        self.file.write(json.dumps(tweet)+ '\n')
        worksheet.write(json.dumps(tweet))
        tweet_list.append(status)
        self.num_tweets+=1
        if self.num_tweets<3000:
            return True
        else:
            return False
        self.file.close()
        workbook.close()


l = MyStreamListener()
stream =tweepy.Stream(auth,l)
stream.filter(track=['teslabot, TeslaBot, Teslabot, TeslaAIBot, teslaAI'])

