import requests

#I am creating room and writting token 
access_token = 'MTE4ZWY4NzEtZWQzZi00YzllLWIyOWYtMjkzMDllZjk1YjY2OWE4NGQ5NjAtYWJi_PF84_consumer'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'Netacad_Devasc_Skills_RP'}
res = requests.post(url, headers=headers, json=params)

#I am adding YR to the room
room_id = res.json()['id']
person_email = 'yvan.rooseleer@biasc.be'
url = 'https://webexapis.com/v1/memberships'
param = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=param)

#I am sending the message 
message = 'Rasa Pikiene Skills Exam: \n https://github.com/Rasapiki/Devasc_Skills.git'
url = 'https://webexapis.com/v1/messages'
para = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=para)
