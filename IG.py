import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from i import mahadi
 
        mahadi()
 
 
 
elif bit == "32bit":
 
        from INSTA import mahadi
 
 
        mahadi()
 
