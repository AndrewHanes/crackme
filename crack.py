import json
import urllib
import string

__author__ = 'ahanes'

"""
Program to crack the password.

You need to finish it
"""

HOST = 'http://localhost:8000'
VALID_CHARS = string.ascii_lowercase


def check_password(username, password):
    """
    Check the password
    :param username: Username
    :param password: Password to try
    :return: Dictioary of the response.

    HINT:  The time field is important
    """
    params = urllib.urlencode(dict(username=username, password=password))
    resp = urllib.urlopen(HOST + '/login', params)
    return json.loads(resp.read())

def main():
    """
    TODO Fill in code here.  This is your cracker.

    Valid passwords contain only a-z (lower case alphabetic characters)
    VALID_CHARS can be treated as the set of valid password characters
    You can use check_password to test your password.
    :return:
    """
    #  TODO Put your cracking code here
    print("No solutions")

if __name__ == '__main__':
    main()
