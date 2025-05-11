# Python tool for uploading chrome data to your github repo

This is a simple python tool that : 
1. reads the chrome Local State file and generate the secret key for decryption
2. reads the chrome Login Data file(s)
3. upload the Local State, secret key (as a .txt file) and Login Data files to the given github account 

# questions 
1. so what is this used for?
  . can be used for pentest and osint stuff 
2. how can we decrypt the Login Data file(s) using secret key?
  . https://github.com/kiryano/chrome-password-decryptor
  . https://github.com/ohyicong/decrypt-chrome-passwords
3. why .py file and not an .exe file?
  . anyone has the right to see the clean code
  . anyone do the obfuscation in a different way ... so do it yourself ;)
  . as i have to mention i tried the exe version (using pyinstaller) with no obfuscation and both windows defender and kaspersky didn't detect that as a malware
   
