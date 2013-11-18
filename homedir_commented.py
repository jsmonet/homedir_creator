#!/usr/bin/env python

import pwd
import sys
import string
import os

# define the function to get the user name, user variables, check homedir path for existence, then create the homedir as needed

def find_and_make():
        user = str(sys.argv[1]) 		# username
        org_pwnam = pwd.getpwnam(user)		# user properties
        print org_pwnam[0], "should have a home directory at", org_pwnam[5], "and a group numeral of", org_pwnam[3]
						# parse the props to name [0], homedir path [5], and primary guid [3]

        org_pathdir = org_pwnam[5] 		# making this a variable keeps the rest cleaner
        print "Checking path:", org_pathdir	# we're being verbose

        if os.path.exists(org_pathdir):		# in case the path exists, you want this to skip the creation process
                print "Home directory already exists. Halting operation"
        else:
                print "Directory does not exist. Creating and applying appropriate ownership"
                os.makedirs(org_pathdir)	# create the directory based on the var "org_pathdir" we just made
                os.chown(org_pathdir, org_pwnam[2], org_pwnam[3])	# path, numeric uid [2], numeric guid [3]

if os.getuid() is not 0:
	print "rerun command with sudo"		# kick you out if this isn't run as root or via sudo
else:
	find_and_make()				# calls the function above to do its thing


print "Done."
