from cryptography.fernet import Fernet


key = Fernet.generate_key()
cipher_suite = Fernet(key)

message = input("Enter your message: ")

cipher_text = cipher_suite.encrypt(message.encode())  # Encode the message to bytes
print(f"Encrypted message: {cipher_text}")

choice = input("Do you want to decrypt it? Yes or No: ")

if choice.lower() == "yes":
    
    plain_text = cipher_suite.decrypt(cipher_text).decode()  # Decode to string
    print(f"Decrypted message: {plain_text}")
else:
    print("No decryption!")

