# This program can be used to find who all RTed a tweet,
# tweeted on a hashtag # or keyword

#Run on an IDE like VS Code, PyCharm or command prompt/terminal by typing: python3 RTers.py

#No programming knowledge or tech knowledge is required. Just enter search terms as instucted in
#unhighlighted portions below. Make no changes elsewhere

import tweepy
import pandas as pd
import all_keys

from tweepy import TweepError
from tweepy import RateLimitError
import json

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
# Paste your Twitter API keys between quotes. To get Twitter API keys,
# apply for a Twitter developer account. Gets done quickly  


set_limit = 200000 #Stops pulling tweets at the limit set 


tweet = ["#iStandWithAssamPolice"]
#This is ont of the only changes to be made. Replace portion within quotes to search term
#More examples on it at the bottom
#This can not just be used to find people who tweet on a hashtag or keyword but also
#who all RT 1 given tweet. The search term for it is explained at the last section at bottom



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

all_results = []
try:
    for i in tweet:

        for tweets in tweepy.Cursor(api.search, q =i).pages():
            results = tweets
            all_results.extend(results)
            #print(type(results))
            print(len(all_results))
            if len(all_results) > set_limit:
                break

except:
        print("exception")




tweet_list = []
for user in all_results:
    tweet_list.append(user._json)


df = pd.DataFrame(tweet_list)

df.to_csv('iStandWithAssamPolice_timestamp.csv', index = False, encoding='utf-8') 
#The file name within quotes 'iStandWithAssamPolice_timestamp.csv'. Change this for search
#This will help you from mixing up the data

#Also remember to search within 7 days of the tweet(s) being posted. Otherwise they 
#cannot be searched for free and requires the Twitter paid premium API






#Here are some examples of what can be searched and how----

#tweet = ["As per our information, they (Mizoram Govt) have distributed arms and ammunition to civilians. Many of them are former militants. Hence, they are trained. They are aggressively forwarding towards us so we have to stop them at some point: Cachar DC Keerthi Jalli (30.07)","twitter.com/ANI/status/1421243385344532488"]

##Note that the first past within quotes has the text of the ANI tweet. This gives who all RTed the tweet
##Same copy-paste tweets are often used in hate campaigns. To understand how to know 
##which tweet is by whom, watch video tutorial.

##The second part in quotes after comma has the link to the tweet
##This gives the list of who have RTed tweets quoting the ANI tweet
##To understand who all RTed quoted tweets to amplify hate speech or counter it, 
##look at the csv spreadheet's tweet text column. Explained in video tutorial




# tweet = ["In the last few years, many \"Mizo social organisations\" have demanded \"complete expulsion\" of Buddhist Chakmas and Hindu Bru Tribals from the state. This was AFTER Mizoram Peace Accord was signed. Was peace not jeopardized then?","twitter.com/BharadwajSpeaks/status/1421380232385220614"]

## In case the tweet has quotation marks "" in text, add slashes in this manner
## "Mizo social organisations" has to be changed to \"Mizo social organisations\"



#tweet = ["What led to #AssamMizoramBorder tension? Here is relation btw CM @himantabiswa's hot pursuit against #drug mafias/ betel nut smugglers n #Mynamar #Mizoram based smugglers which r aggrieved due to @CMOfficeAssam @assampolice's crackdown on internatl cartel. Thread #ShameOnMizoram+","twitter.com/LegalLro/status/1420277641911799819"]





