def encode(password):
    ans = ""
    for val in password:
        ans += str(int(val) + 3)
    return ans

def decode(password):
    ans = ""
    for val in password:
        ans += str(int(val) - 3)
    return ans


def main():
    menu = "Menu\n" \
            "-------------\n" \
            "1. Encode\n" \
            "2. Decode\n" \
            "3. Quit\n" \

    while True:
        print(menu)
        userIn = input("Please enter an option: ")
        if userIn == "1":
            try:
                userEncode = input("Please enter your password to encode: ")
                print("Your password has been encoded and stored!\n")
            except ValueError:
                print("Invalid Input, try again\n")
        elif userIn == "2":
            print(f"The encoded password is {encode(userEncode)}, and the original password is {userEncode}.")
        elif userIn == "3":
            break
        else:
            print("Invalid Input\n")

if __name__ == "__main__":
    main()
    #comment test