# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>
consumer_key = '5jcnRj0UhqnbPKFTNXrZqW3gC'
consumer_secret = 'DjdqO7NaH06K1JlZIjqgv0YRJvbSwldilELmVbIigCv6FLK6n8'
access_token = '1244626213-dmBFlzAPuIq6UBpjwf8GrRz0VKpT3EfTOcxnDob'
access_token_secret = 'TP82QfyCpBec6M0xSCpakAhIei78RBArxjuN9UrVaKJ9V'


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

test_list= api.user_timeline(screen_name='realDonaldTrump', count=5)
test = test_list[0]

user_timeline= open('usertimeline.json', 'w')
test_dump = json.dumps(test._json)
user_timeline.write(test_dump)
user_timeline.close()

def part1(user, tweet_number):
    status=api.user_timeline(screen_name=user, count=tweet_number, tweet_mode='extended')
    original_count=0
    for tweet in status:
        retweet = tweet._json['retweeted']
        if retweet == False:
            original_count=original_count+1
    texts_all=[]
    for tweets in status:
        text = tweets._json['full_text']
        tagged_words=nltk.word_tokenize(text)
        tagged_text = nltk.pos_tag(tagged_words)
        texts_all.extend(tagged_text)
    nouns = {}
    for tuple in texts_all:
        for tuple in texts_all:
            if "NN" in tuple[1] and 'RT' not in tuple[0] and 'http' not in tuple[0] and 'https' not in tuple[0] and '//' not in tuple[0] and '@' not in tuple[0] and tuple[0][0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and tuple[0] not in nouns:
                nouns[tuple[0]]=1
            elif "NN" in tuple[1] and 'RT' not in tuple[0] and 'http' not in tuple[0] and 'https' not in tuple[0] and '//' not in tuple[0] and '@' not in tuple[0] and tuple[0][0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                nouns[tuple[0]] = nouns[tuple[0]] +1
        nouns_tuple = nouns.items()
        nouns_sorted2=sorted(nouns_tuple, key=lambda x: x[0], reverse = False)
        nouns_sorted = sorted(nouns_sorted2, key = lambda x: x[1], reverse=True)
    verbs= {}
    for tuple in texts_all:
        if "VB" in tuple[1] and 'RT' not in tuple[0] and 'http' not in tuple[0] and '//' not in tuple[0] and '@' not in tuple[0] and tuple[0][0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and tuple[0] not in verbs:
        #I know you can use .isaplha() but this makes the for loops easy to find
            verbs[tuple[0]]=1
        elif "VB" in tuple[1] and 'RT' not in tuple[0] and 'http' not in tuple[0] and '//' not in tuple[0] and '@' not in tuple[0] and tuple[0][0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            verbs[tuple[0]] = verbs[tuple[0]] +1
    verbs_tuple = verbs.items()
    verbs_sorted2=sorted(verbs_tuple, key=lambda x: x[0], reverse = False)
    verbs_sorted = sorted(verbs_sorted2, key = lambda x: x[1], reverse=True)
    adjectives= {}
    for tuple in texts_all:
        if "JJ" in tuple[1] and 'RT' not in tuple[0] and 'http' not in tuple[0] and '//' not in tuple[0] and '@' not in tuple[0] and tuple[0][0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and tuple[0] not in adjectives:
            adjectives[tuple[0]]=1
        elif "JJ" in tuple[1] and 'RT' not in tuple[0] and 'http' not in tuple[0] and '//' not in tuple[0] and '@' not in tuple[0] and tuple[0][0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            adjectives[tuple[0]] = adjectives[tuple[0]] + 1
    adjectives_tuple = adjectives.items()
    adjectives_sorted2=sorted(adjectives_tuple, key=lambda x: x[0], reverse = False)
    adjectives_sorted = sorted(adjectives_sorted2, key = lambda x: x[1], reverse=True)
    def common_words(words):
        output=[]
        for word in words:
            output.append(" " + word[0]+ '(' + str(word[1]) +')')
        return ''.join(output)
    five_nouns=nouns_sorted[0:5]
    five_verbs=verbs_sorted[0:5]
    five_adjectives=adjectives_sorted[0:5]
    favorites = 0
    for tweet in status:
        retweet = tweet._json['retweeted']
        if retweet == False:
            favorites = favorites + tweet._json['favorite_count']
    retweets = 0
    for tweet in status:
        retweet = tweet._json['retweeted']
        if retweet == False:
            retweets = retweets + tweet._json['retweet_count']
    noun_data=open('noun_data.csv','w')
    writ=noun_data.write('Noun,Number\n{},{}\n{},{}\n{},{}\n{},{}\n{},{}'.format(five_nouns[0][0],five_nouns[0][1],five_nouns[1][0],five_nouns[1][1],five_nouns[2][0],five_nouns[2][1],five_nouns[3][0],five_nouns[3][1],five_nouns[4][0],five_nouns[4][1]))
    noun_data.close()
    output='USER:{}\nTWEETS ANALYZED:{}\nVERBS:{}\nNOUNS:{}\nADJECTIVES:{}\nORIGINAL TWEETS:{}\nTIMES FAVORITED (ORIGINAL TWEETS ONLY): {}\nTIMES RETWEETED (ORIGINAL TWEETS ONLY): {}'.format(user,tweet_number,common_words(five_verbs),common_words(five_nouns),common_words(five_adjectives),original_count,favorites,retweets)
    return print(output)

if __name__=="__main__":
    part1(sys.argv[1],sys.argv[2])
