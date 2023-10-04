import shutil
from cryptography.fernet import Fernet

COPYFOLDER = 'C:\\Users\\orour\\Desktop'
SOURCEFOLDER = 'C:\\Users\\orour\\Desktop\\code\\a.exe'

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

def main():
    copy_file(SOURCEFOLDER, COPYFOLDER)
    encrypt_file(SOURCEFOLDER, generate_key())

main()