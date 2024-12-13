#People Say You Can't Make A Telegram Username Checker With Only Requests So I Will Show Them How
from requests import get as g

#Some Cute Vars
usernames_file='users.txt'
good_users='good.txt'
bad_users='bad.txt'

#Chack If Username Is Vaild
def check_username(username):
    #Get Username Request
    r = g(f'https://t.me/{username}')
    #Get The Html Page
    html_code = r.text
    #Check If Username Is Used
    if f'<meta property="twitter:title" content="Telegram: Contact @{username}">' in html_code:
        return True
    else:
        return False
    
#Chack If Username In Fragment
def check_fragment(username):
    #Get Username Request
    r = g(f'https://fragment.com/username/{username}')
    #Get The Html Page
    html_code = r.text
    #Check If Username Is NFT or Onaction
    if "Unavailable" in html_code:
        return True
    else:
        return False

#Test The Username
try:
    #Open The Usernames File
    with open(usernames_file, 'r') as file:
        #Get Every Username In File One By One
        for username in file:
            #Delete Spaces
            username=username.strip()
            #You Can Call It Debug
            print(f'Testing Username {username}')
            #Check That Username Is Not On Fragment And Available On Telegram
            if check_username(username) and check_fragment(username):
                print(f'This Username {username} Is Available')
                #Save The Good Usernames
                with open(good_users, 'a') as good:
                    good.write(username+'\n')
            else:
                #Save The Bad Usernames (Idk Why Don't Ask Me)
                print(f'This Username {username} Is Unavailable')
                with open(bad_users, 'a') as bad:
                    bad.write(username+'\n')
#Error Handling
except Exception as e:
    print(e)
    
