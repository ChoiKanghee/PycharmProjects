# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def is_valid(email_input):
    if re.fullmatch(regex, email_input):
        print("Email: True")
        return True
    else:
        print("Email: False")
        return False


def check_email_is_gmail(email_input):
    if ("@gmail.com" in email_input):
        print("Gmail : True")
    else:
        print("Gmail : False")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    email = input('Enter email : ')
    if (is_valid(email)):
        check_email_is_gmail(email)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
