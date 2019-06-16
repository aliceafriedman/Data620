import time
from twython import Twython

def get_followers_json(username):
    try:
        # Load Twitter API credentials from json file
        with open("twitter_credentials.json", "r") as file:  
            creds = json.load(file)

        # Instantiate an object and provide Twitter credentials
        twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET_KEY'], creds['ACCESS_TOKEN'], creds['ACCESS_SECRET_TOKEN'])# create empty dictionary to accept data
    
        dict_fol = {'screen_name': [], 'verified': [], 'followers_count': []}  
    
        #create loop to page through API results
        next_cursor = -1
        timeout = time.time() + 10 #creates a hard end time for the script to run

        while(next_cursor):
            if time.time() > timeout:
                break #ends loop after timeout period
            get_followers = twitter.get_followers_list(screen_name = username, count=5000, cursor=next_cursor)
            for user in get_followers['users']:  
                dict_fol['screen_name'].append(user['screen_name'])
                dict_fol['verified'].append(user['verified'])
                dict_fol['followers_count'].append(user['followers_count'])
                time.sleep(2)
    
        filename=username + "_followers.json"
    
        with open(filename, "w") as file:
            json.dump(dict_fol, file)
    
    except:
        time.sleep(900) #Twitter API rate limits reset after 15 minutes
        get_followers_json(username)

get_followers_json('Abigail963')
