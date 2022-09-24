import requests
import json
import os
from pathlib import Path

BASE_URL = 'http://pretest-qa.dcidev.id'
beartoken = '603ca6498c742060b629dff7275abf4714d26eaf29f9120215d82eacd1d12ca1'
user_id = 'd05aa6fe-bfed-4466-9e7b-4a776df1dba6'

profile_path = Path(__file__).with_name('dummy.png')
profile_image = {'image': open(profile_path, 'rb')}

cover_path = Path(__file__).with_name('dummy.png')
cover_image = {'image': open(cover_path, 'rb')}

# get bearer_token------------------------------------------------------------------------
data_cred = {
    'user_id': 'd05aa6fe-bfed-4466-9e7b-4a776df1dba6', 
    'otp_code': '0351'
    }

response_token = requests.post(f"{BASE_URL}/api/v1/register/otp/match", data= data_cred)
beartoken = response_token.json()['data']['user']['access_token']
header = {'Authorization': beartoken}

# update profile info---------------------------------------------------------------------
data_profile_info = {
    'name': 'Frisco Kharisma',
    'gender': 0,
    'birthday': '1998-03-25',
    'hometown': 'yogyakarta',
    'bio': 'Test'
    }

response_profile_info = requests.post(f"{BASE_URL}/api/v1/profile", headers= header, data= data_profile_info)
print('POST /api/v1/profile                 : ' + str(response_profile_info.status_code))

# update profile career-------------------------------------------------------------------
data_profile_career = {
    'position': 'sqa',
    'company_name': 'utest',
    'starting_from': '2021-03-25',
    'ending_in': '2022-03-25'
    }

response_profile_career = requests.post(f"{BASE_URL}/api/v1/profile/career", headers= header, data= data_profile_career)
print('POST /api/v1/profile/career          : ' + str(response_profile_career.status_code))

# update profile education----------------------------------------------------------------
data_profile_education = {
    'school_name': 'UGM',
    'graduation_time': '2020-03-25'
    }

response_profile_education = requests.post(f"{BASE_URL}/api/v1/profile/education", headers= header, data= data_profile_education)
print('POST /api/v1/profile/education       : ' + str(response_profile_education.status_code))

# get profile information-----------------------------------------------------------------

response_profile = requests.get(f"{BASE_URL}/api/v1/profile/me", headers= header)
# responsejson = response_profile.json()

print('GET /api/v1/profile/me               : ' + str(response_profile.status_code))
# print(beartoken) #get bear token
# print(responsejson["data"]["user"]["name"]) #get name for validation

# upload cover----------------------------------------------------------------------------
response_upload_cover = requests.post(f"{BASE_URL}/api/v1/uploads/cover", headers= header, files=cover_image)
print('POST /api/v1/uploads/cover           : ' + str(response_upload_cover.status_code))

# delete default photo--------------------------------------------------------------------
response_delete_photo = requests.delete(f"{BASE_URL}/api/v1/uploads/profile", headers= header)
print('DELETE /api/v1/uploads/profile       : ' + str(response_delete_photo.status_code))
# print(response_delete_photo.json())

# post profile photo----------------------------------------------------------------------
response_upload_profile = requests.post(f"{BASE_URL}/api/v1/uploads/profile", headers= header, files= profile_image)
print('POST /api/v1/uploads/profile         : ' + str(response_upload_profile.status_code))
photo_id = response_upload_profile.json()['data']['user_picture']['id']

# upload profile default------------------------------------------------------------------
data_default_profile = {
    'id' : photo_id
    }

response_default_profile = requests.post(f"{BASE_URL}/api/v1/uploads/profile/default", headers= header, data= data_default_profile)
print('POST /api/v1/uploads/profile/default : ' + str(response_default_profile.status_code))

# send message----------------------------------------------------------------------------
data_sm = {
    'user_id': user_id,
    'message': 'Test'
    }

response_sm = requests.post(f"{BASE_URL}/api/v1/message/send", headers= header, data= data_sm)
print('POST /api/v1/message/send            : ' + str(response_sm.status_code))

# send_time = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
# print(send_time)

#read message------------------------------------------------------------------------------
response_rm = requests.get(f"{BASE_URL}/api/v1/message/" + user_id, headers= header)

print('GET /api/v1/message/user_id          : ' + str(response_rm.status_code))
# print(response_rm.json()['data']['chat']['created_at'])

# sign in oauth----------------------------------------------------------------------------
data_signin_oauth = {
    'phone': '6282281020471', 
    'password': 'Testqa123', 
    'latlong': '12345', 
    'device_token': '12345', 
    'device_type': '1'
    }

response_signin_oauth = requests.post(f"{BASE_URL}/api/v1/oauth/sign_in", data= data_signin_oauth)
print('POST /api/v1/oauth/sign_in           : ' + str(response_signin_oauth.status_code))

new_beartoken = response_signin_oauth.json()['data']['user']['access_token']

# open credential oauth--------------------------------------------------------------------
response_see_cred = requests.get(f"{BASE_URL}/api/v1/oauth/credentials?access_token=" + str(new_beartoken))

print('GET /api/v1/oauth/credentials        : ' + str(response_see_cred.status_code))

# print('beartoken        : ' + str(beartoken))
# print('new beartoken    : ' + str(new_beartoken))



# Minus : Verification per item + delete photo profile

# checklist --------------------------------------------------------------------------------
# GET /api/v1/message/{user_id}---x
# POST /api/v1/message/send---x
# POST /api/v1/notification/{grub_id}/{token} -> out of scope
# GET /api/v1/oauth/credentials---x
# POST /api/v1/oauth/sign_in---x
# POST /api/v1/oauth/revoke -> out of scope
# POST /api/v1/profile/career---
# POST /api/v1/profile/education---
# POST /api/v1/profile---
# GET /api/v1/profile/me---x
# POST /api/v1/register/remove -> out of scope
# POST /api/v1/register/otp/request -> out of scope
# POST /api/v1/register/otp/match---x
# POST /api/v1/register -> out of scope
# POST /api/v1/uploads/cover---
# POST /api/v1/uploads/profile/default---
# DELETE /api/v1/uploads/profile---
# POST /api/v1/uploads/profile---