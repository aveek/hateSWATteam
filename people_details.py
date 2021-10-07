import pandas as pd 
import ast
import json




tweet_details_df=pd.read_csv("iStandWithAssamPolice_timestamp.csv")#, low_memory=False)
## Remove this line and use the one below if you get an error
## You will get an error for a big csv spreadsheet file 
## with close to 1 lakh rows 
## USE THIS: (Remove # infront of next line when using it)

#tweet_details_df=pd.read_csv("iStandWithAssamPolice_timestamp.csv", low_memory=False)



list_of_parameters=['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile', 'profile_image_url', 'profile_image_url_https', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image', 'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'follow_request_sent', 'notifications', 'translator_type', 'withheld_in_countries']
user_details_df=pd.DataFrame(columns=list_of_parameters)



l=tweet_details_df.shape[0]

for i in range(0,l):
    
    useri=tweet_details_df['user'].iloc[i]


    useri_dict=ast.literal_eval(useri)

   
    
    user_details_df = user_details_df.append(useri_dict,ignore_index=True)
    

second_list_of_parameters=['name', 'handle', 'verified','followers_count','bio','tweet_text','retweet_count','favorite_count','tweeted_at','location','account_created_on','following_count', 'listed_count', 'url', 'favourites_count', 'tweet_count', 'contributors_enabled']
people_details_df=pd.DataFrame(columns=second_list_of_parameters)


people_details_df['name']=user_details_df['name']

people_details_df['handle']=user_details_df['screen_name']

people_details_df['verified']=user_details_df['verified']

people_details_df['followers_count']=user_details_df['followers_count']

people_details_df['bio']=user_details_df['description']

people_details_df['location']=user_details_df['location']

people_details_df['account_created_on']=user_details_df['created_at']

people_details_df['following_count']=user_details_df['friends_count']

people_details_df['listed_count']=user_details_df['listed_count']

people_details_df['url']=user_details_df['url']

people_details_df['favourites_count']=user_details_df['favourites_count']

people_details_df['tweet_count']=user_details_df['statuses_count']

people_details_df['contributors_enabled']=user_details_df['contributors_enabled']









people_details_df['tweet_text']=tweet_details_df['text']

people_details_df['tweeted_at']=tweet_details_df['created_at']

people_details_df['retweet_count']=tweet_details_df['retweet_count']

people_details_df['favorite_count']=tweet_details_df['favorite_count']






people_details_df.to_csv('iStandWithAssamPolice_RTers.csv', encoding='utf-8', index=False)
#This csv spreadsheet file is what will be looked at.
#It contains details of users, like verified or not, number of followers,etc 
#& which tweet they have tweeted or RTed 

# Tutorial video guides on what to look at & how to analyse it 



dropped_duplicates_RTers = people_details_df.drop_duplicates(subset='handle')

dropped_duplicates_RTers.to_csv('iStandWithAssamPolice_unique_RTers.csv', encoding='utf-8', index=False)


print(people_details_df.shape)
#This gives total number of tweets made. An account can have tweeted more than 1 tweet

print(dropped_duplicates_RTers.shape)
#This gives the unique number of accounts making the tweets.
#For explainer, watch tutorial video
