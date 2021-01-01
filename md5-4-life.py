#!/usr/bin/env python3

#takeaways : putting the URL into a variable & making a GET request in another would be faster.

import requests
import re
import hashlib

req = requests.session()
url = "http://206.189.17.51:32142"

rget = req.get(url)
content = rget.text

#stripped HTML tags
nicer_content = re.sub('<[^<]+?>', '', content)

#getting the string
##splits the word 'string' from the actual string we want to hash
string = nicer_content.split('string')[1].rstrip()

# because 'TypeError: Unicode-objects must be encoded before hashing'
string = string.encode('utf-8')

#emdee5sum it

md5 = hashlib.md5(string).hexdigest()

# send POST of the hash
data = dict(hash=md5)
rpost = req.post("http://206.189.17.51:32142",data=data)
post_content = rpost.text
nicer_post_content = re.sub('<[^<]+?>', '', post_content)
try:
    nicer_post_content = nicer_post_content.split('HTB')[1].rstrip()
    print("HTB" + nicer_post_content)
except:
    print("Too slow :( Try again!")