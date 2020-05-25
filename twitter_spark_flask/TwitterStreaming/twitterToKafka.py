from kafka import SimpleProducer, KafkaClient
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler


access_token = '1063944351724662784-MVTRTpJk2JdoFTOl3UeVt04orBjSUJ'
access_token_secret =  'GgwSxgkQVrXfnsQXxbuon3CDmV9GERKz0H8EYfv3Db76p'
consumer_key =  'EL9bP53IKTBWsmNVkXeBaTLH0'
consumer_secret = 'URuSzNfTCFBq7nPyaSqAjqksECbD2vUFUMq2RfhYSjoloWPQbq'

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("twitterStream", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="twitterStream")
