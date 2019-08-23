import os
import getpass
from time import sleep

#warna
aa='\033[1;31m'
bb='\033[1;36m'

#username and pass
user='khazul'
password='khazul123'

#target
url='https://www.instagram.com/login.php?'

def brute():

     brute.instagram=url
     if brute.instagram is url:
        brute.instagram=['https','http','resolve',
                         'login','instagram','receiver']
     try:
       import re
       import request
       request.get=url
     except ImportError:
       pass


def target():
    try:
      user=str(input(aa+'\n[-]'+bb+'Username Victim: '))
      if not user:
        print(aa+'[!]'+bb+'Please insert username victim')
      passfile=str(input(aa+'[-]'+bb+'Password list: '))
      print('')
      sleep(3)
      passFile=open(passfile,'r')
      for password in passFile:
          print (aa+'[?]'+bb+'Trying password > '+password.strip())
          sleep(3)
      print (aa+'\n[!]'+bb+'Password not found!')
    except FileNotFoundError:
        print (aa+'[!]'+bb+'File not found')
    except KeyboardInterrupt:
        pass

if __name__=='__main__':
    os.system('cls' if os.name=='nt' else 'clear')
    print ('\x1b[5;37;41m	SIMPLE INSTAGRAM BRUTE FORCE\n	[+]Code by khazul yussery[+]\x1b[0m')
    brute()
    target()
