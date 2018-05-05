import requests

userID = 'id417243154'

apiURL = 'https://api.vk.com/method/'

def getUser(name):
    data = requests.get(apiURL + 'users.get',{'fields':'photo_max_orig',
                                              'user_ids':name,
                                              'v':'5.74'})
    return data.json()



user = getUser(userID)
urlIm = user['response'][0]['photo_max_orig']
image = requests.get(urlIm)

photo = open('image.jpg','wb')

photo.write(image.content)

photo.close()

print(user)
