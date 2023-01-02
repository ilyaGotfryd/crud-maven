# crete password generator funciton that takes in password length
# and list of special characters defaulting to "!@#$%^&*()"
# import and use random.shuffle and random.choice functions
# password needs to consist out of [a-z][A-Z][0-9][!@#$%^&*()]
# use range, list comprehansion ord()=> chr to int  and chr()=> int to chr funcitons
# return password
# run 3 times and print the output every time

legal_chars = [char(i) for i in range(ord('a'), ord('z')+1)]

def generate_credentials():
    print(legal_chars)
# import logging decorator
# decorate the password function
# run and see the output

generate_credentials()