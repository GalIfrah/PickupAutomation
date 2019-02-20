import base64
import json
import jwt
import requests
from Crypto.Cipher import AES
from App.PageObjects import *


USERS_ENDPOINT = "https://the-test.mycheckapp.com/users"
AUDIENCE = "TEST"
GET_VERIFY_CODE_BY_PSW = "KRJfHeXpKIXksryv51wkYjYwOxEuWAv5/QGy8F10UL0="


def sendSMS():

   request = {

       "phone": "+972542567405",
       "publishableKey": "pk_xb0tQerFtExKhYLbUMz8bkhhlpkuL"
   }

   response = requests.post(USERS_ENDPOINT + '/api/v1/user/metadata/guest', data=request)

   verifyToken = response.json()

   return verifyToken['tokens']['phone']



def decodeSmsCode(verify_token):

    token = jwt.decode(verify_token, 'example_key', audience=AUDIENCE, algorithms=['HS256'])

    print(token)

    secret = base64.b64decode(GET_VERIFY_CODE_BY_PSW)

    encrypted_code = json.loads(base64.b64decode(token['sub']['code_e']))

    cipher = AES.new(secret, AES.MODE_CBC, base64.b64decode(encrypted_code['iv']))

    decoded = cipher.decrypt(base64.b64decode(encrypted_code['value']))

    return decoded[5:11]
