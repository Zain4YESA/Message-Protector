from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)
message = input("Enter your message: ")
choice = input("If you want to encode your message, type 1 or to decode enter 2: ")

if choice == '1':
    # Encrypt a message
    cipher_text = cipher_suite.encrypt(message.encode())  # Encode the message to bytes
    print(f"Encrypted message: {cipher_text}")
elif choice == '2':
    # Ensure there's a cipher text to decrypt
    try:
        plain_text = cipher_suite.decrypt(cipher_text).decode()  # Decode to string
        print(f"Decrypted message: {plain_text}")
    except NameError:
        print("Error: No encrypted message found. Please encrypt a message first.")
else:
    print("Invalid choice. Please enter 1 to encode or 2 to decode.")
