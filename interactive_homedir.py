#!/usr/bin/env python

import pwd
import sys
import string
import os



def find_and_make():
        user = raw_input("Please enter the username whose homedir you wish to create:")
        try:
                pwd.getpwnam(user)
                org_pwnam = pwd.getpwnam(user)
                print org_pwnam[0], "should have a home directory at", org_pwnam[5], "and a group numeral of", org_pwnam[3]
                org_pathdir = org_pwnam[5]
                print "Checking path:", org_pathdir

                if os.path.exists(org_pathdir):
                        print "Home directory already exists."
                        keep_going()
                else:
                        print "Directory does not exist. Creating and applying appropriate ownership"
                        os.makedirs(org_pathdir)
                        os.chown(org_pathdir, org_pwnam[2], org_pwnam[3])
                        keep_going()
        except KeyError:
                pass
                print "User not found."
                keep_going()

def keep_going():
        yes = set(['yes', 'y', 'Y', 'Yes', 'ye', ''])
        no = set(['no', 'No', 'n', 'N'])
        more_answer = raw_input("Would you like to create another home directory?")
        if more_answer in yes:
                find_and_make()
        elif more_answer in no:
                print "Done."
        else:
                print "Please say yes or no"
                keep_going()


if os.getuid() is not 0:
        print "rerun command with sudo"
else:
        find_and_make()