import tweepy
import time

class Twit():
    def __init__(self):
        auth = tweepy.OAuthHandler(, )
        auth.set_access_token(, )    
        self.api = tweepy.API(auth)
               

    def extract_followers_dict(self, user_id,friends=False):
        
      
        #open extraction of followers or friends with a given id
        if (friends): items = tweepy.Cursor(self.api.friends_ids, user_id).items()
        else: items = tweepy.Cursor(self.api.followers_ids, user_id).items()
       
        followers  = {}
       
        while (True):
            try:
                item = next(items)
                followers[item] = True
                
            except tweepy.TweepError as e:
                print e
                
                #user does not exist
                try:
                    #not Authorized, if is closed
                    if (e.response.status== 401):
                        followers[-1] = True
                        
                        return followers
                    
                    #user is deleted
                    if (e[0][0]['code'] == 34):
                            followers[-1] = True
                            
                            return followers
                except:
                    print 'Not standart error.' 
                while True:
                    try:
                        #wait for the extract limit
                        #rate limited
                        rate_info = self.api.rate_limit_status()['resources']
                        reset_time = rate_info['followers']['/followers/ids']['reset']
                        cur_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
                        
                        #wait min time plus ten seconds
                        try_again_time = reset_time - cur_time + 10
                        
                        #wait
                        print 'Wait '+ str(try_again_time)
                        if (try_again_time < 1):
                            try_again_time = 5
                        time.sleep(try_again_time)
                        
                        break
                    except:
                        time.sleep(10)
    
            except StopIteration:
                return followers   