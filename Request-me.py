#!/usr/bin/python

import requests
#Somthing Wrong in This Challenge

'''
PUT >> I couldn't steal your credentials! Where did you hide them?
GET >> <p>WRONG <a href="https://lmgtfy.com/?q=http+request+options">FLAG</a></p>
POST >> Could not verify your access level for that URL. You have to login with proper credentials

OPTIONS : 
GET, POST, PUT, DELETE, OPTIONS
username, password
Some methods require HTTP Basic Auth  <user:password> 
'''

url = "https://request_me.tjctf.org/"
session = requests.Session()

Data = {"username":"test","password":"test"}

res = requests.put(url , data=Data)
print  res.text   
print "#"*80
res = requests.post(url , data=Data)
print  res.text   
print "#"*80
res = requests.delete(url , auth=('admin','admin'))
print  res.text   
print "#"*80
#tjctf{wHy_4re_th3r3_s0_m4ny_Opt10nS}