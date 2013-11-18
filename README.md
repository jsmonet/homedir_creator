Simple homedir creation script written in Python.

This script assumes that you have sufficient privs to sudo on the box you use to create the directories. 
Usage: chmod +x a.py then execute with one argument:
sudo ./a.py username
You can also copy this file, sans extension, into your local bin dir that isn't /usr/bin and run it by name, assuming you have that directory in your path. Personally I would put it in /usr/local/sbin or similar. 

homedir_commented.py is just a heavily commented version of the same script. It exists solely for reference, as the other version is cleaner for real world use.

The interactive version of this script is interactive_homedir.py. This should be a bit more user-friendly and it even thanks you when you end the program. To execute, chmod +x and sudo ./interactive_homedir.py (or whatever you end up calling it). Script does not require or parse arguments.
