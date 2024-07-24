
def encode(password):
    string = ''
    for i in range(0,len(password)):
        p = int(password[i])
        if p < 7:
            p = p + 3
        elif p == 7:
            p = 0
        elif p == 8:
            p = 1
        elif p == 9:
            p = 2
        string = string + str(p)
    return string

def main():
    while True:
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == 2:

            pass
        else:
            break


if __name__ == '__main__':
    main()