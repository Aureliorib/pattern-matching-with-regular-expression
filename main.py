from phonenumber import isPhoneNumber

num = input("Enter your phone number: ")
print(f"Is {num} a phone number?")
print(isPhoneNumber(num))