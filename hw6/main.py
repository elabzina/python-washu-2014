from twit import *

a=Twit()


#determining the activity of the friends
#I define activity as the number of the favourited posts

friends=a.extract_followers_dict('littvay',True)

amax=0
auser=-1

for f in friends:
    u = a.api.get_user(f)
    if u.favourites_count>amax:
        amax=u.favourites_count
        auser=f

str = "Most active on the first level of the friends: " + amax + " of user " + auser
print str

#most active friend: user : 42553 , number of favourited posts: 4882

#determining the maximum number of the followers on two levels
#this may take a while

followers1=a.extract_followers_dict('littvay') 
max1=0
user1=-1
max2=0
user2=-1
fmax1=0
fuser1=-1
fmax2=0
fuser2=-1

for f1 in followers1:
    u = a.api.get_user(f1)
    if u.favourites_count>fmax1:
        fmax1=u.favourites_count
        fuser1=f1
    if u.followers_count>max1:
        max1 = u.followers_count
        user1 = f1
    followers2=a.extract_followers_dict(f1)
    for f2 in followers2:
        u = a.api.get_user(f2)
        if u.followers_count>max2:
            max2 = u.followers_count
            user2=f2
        if u.favourites_count>fmax2:
            fmax2=u.favourites_count
            fuser2=f2
#max 

if (max2<max1):
    max2=max1
    user2=user1

if (fmax2<fmax1):
    fmax2=max1
    fuser2=user1
   
str = "Most favourites on the first level of the followers: " + max1 + " of user " + user1
print str
 
str = "Most favourites on the second level of the followers: " + max2 + " of user " + user2
print str   
   
str = "Most active on the first level of the followers: " + fmax1 + " of user " + fuser1
print str
 
str = "Most active on the second level of the followers: " + fmax2 + " of user " + fuser2
print str   

#user with maximum followers on both levels : 60486 , number of followers: 18382184
#most active follower: user : 60486 , number of favourited posts: 8397

