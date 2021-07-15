"""
Created on Mon July 12 2021

@author: Avoracity
@desc: Print a discord message every hour.

"""

import requests
from time import time

payload = {
  'content' : "text to be outputted"    # i.e. "hello world" would input hello world from your discord 
}

header = {
  'token_key' : 'your_token_key_for_script_to_use_account'  # i.e. 'NTI5MzT3N24YWGSDI.GEOOOYYNAM'
}

"""
1 minute = 60 seconds
30 minutes = 1800 seconds
1 hour = 3600 seconds

"""

while True:
  r = requests.post("the_channel_url",   data=payload, headers=header) # replace "the_channel_url", i.e. 'https://discord.com/channels/847617933940228096/8476330228099'
  # sleep() delays code when executed
  # time() returns the number of seconds passed server time
  # time.sleep() delays code based on server time
  time.sleep(3600)  # in seconds