#!/usr/bin/env python

import pwd
import sys
import string
import os

def find_and_make():
        user = str(sys.argv[1])
        org_pwnam = pwd.getpwnam(user)
        print org_pwnam[0], "should have a home directory at", org_pwnam[5], "and a group numeral of", org_pwnam[3]


        org_pathdir = org_pwnam[5]
        print "Checking path:", org_pathdir

        if os.path.exists(org_pathdir):
                print "Home directory already exists. Halting operation"
        else:
                print "Directory does not exist. Creating and applying appropriate ownership"
                os.makedirs(org_pathdir)
                os.chown(org_pathdir, org_pwnam[2], org_pwnam[3])

if os.getuid() is not 0:
	print "rerun command with sudo"
else:
	find_and_make()


print "Done."
