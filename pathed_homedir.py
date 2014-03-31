import pwd
import sys
import string
import os

# Get the user name first to feed it into a global variable
# org_pwnam will be reused in various defs below

def which_type():
  user = raw_input("Please enter the username whose homedir you wish to create:")
  global org_pwnam
  org_pwnam = pwd.getpwnam(user)  
  try:
    pwd.getpwnam(user)
  except KeyError:
    print "User not found."
    keep_going()

  if "ifshome" in org_pwnam[5]:
    print "Account is a user account"
    make_account()
  elif "ftphome" in org_pwnam[5]:
    print "Account is an ftp account"
    make_ftp()
  else:
    print "Neither account type found. Please check account settings. Sending you back to user selection..."
    keep_going()


def make_account():
  print "The mounted home directory will be", org_pwnam[5], "but we need to create the homedir at /ifs/home/%s" % (org_pwnam[0])
  org_pathdir = "/ifs/home/%s" % (org_pwnam[0])
  print "Checking path:", org_pathdir
  if os.path.exists(org_pathdir):
	print "Home directory already exists."
	keep_going()
  else:
    print "Directory does not exist. Creating and applying appropriate ownership"
    os.makedirs(org_pathdir)
    os.chown(org_pathdir, org_pwnam[2], org_pwnam[3])
    keep_going()

def make_ftp():
  print "The mounted home directory will be", org_pwnam[5], "but we need to create the homedir at /ifs/ftphome/%s" % (org_pwnam[0])
  org_pathdir = "/ifs/ftphome/%s" % (org_pwnam[0])
  print "Checking path:", org_pathdir
  if os.path.exists(org_pathdir):
	print "Home directory already exists."
	keep_going()
  else:
    print "Directory does not exist. Creating and applying appropriate ownership"
    os.makedirs(org_pathdir)
    os.chown(org_pathdir, org_pwnam[2], org_pwnam[3])
    keep_going()

def keep_going():
  yes = set(['yes', 'y', 'Y', 'Yes', 'ye', ''])
  no = set(['no', 'No', 'n', 'N'])
  more_answer = raw_input("Would you like to create another home directory? [yes]")
  if more_answer in yes:
  	which_type()
  elif more_answer in no:
    print "Done."
    sys.exit()
  else:
    print "Please say yes or no"
    keep_going()


if os.getuid() is not 0:
   	print "rerun command with sudo"
else:
	which_type()
