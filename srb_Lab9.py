
def encode(password):
    c = 0
    encoded_password = 0
    while password > encoded_password:
        encoded_password = password + 3*(10**c)
        password = encoded_password
        c = c + 1
    return encoded_password




'''def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        choice = input("Please enter an option: ")

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            decode(password)
            pass
        else:
            break'''

print(encode(12345555))