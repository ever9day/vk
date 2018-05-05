import requests

userID = 'id235945509'
apiURL = 'https://api.vk.com/method/'


def getUser(name):
    data = requests.get(apiURL + 'users.get',{'fields':'photo_max_orig',
                                              'user_ids':name,
                                              'v':'5.74'})
    return data.json()


def getFriends(name):
    data = requests.get(apiURL + 'friends.get',{'user_id':name,
                                                'v':'5.74'})
    return data.json()


f1 = set(getFriends('219408095')['response']['items'])
f2 = set(getFriends('235945509')['response']['items'])

f3 = f1 & f2


for i in f3:
    print(getUser(i))





print(f1 & f2)

