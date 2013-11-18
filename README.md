Simple homedir creation script written in Python.

This script assumes that you have sufficient privs to sudo on the box you use to create the directories. 
Usage: chmod +x a.py then execute with one argument:
sudo ./a.py username
You can also copy this file, sans extension, into your local bin dir that isn't /usr/bin and run it by name, assuming you have that directory in your path. Personally I would put it in /usr/local/sbin or similar. 

homedir_commented.py is just a heavily commented version of the same script. It exists solely for reference, as the other version is cleaner for real world use.

I'll be looking at creating an interactive version of this script so you can run it and keep inputting usernames without having to rerun the process constantly. 
