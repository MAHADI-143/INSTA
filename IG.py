import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from IG64 import login_kamu
 
        login_kamu()
 
 
 
elif bit == "32bit":
 
        from MT32 import login
 
 
        login()
 
 
