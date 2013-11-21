==Homedir creation script==
This python script is meant for use on linux operating systems. You can get it to run on OSX, but I haven't seen any real reason to use it there yet, so I haven't tested that use.

===homedir.py===
This is the initial script that kicked this off. I'm no longer working on this one, so I'll likely remove it soon.

===homedir_commented.py===
This is a commented version of the original script. Like above, this is not really necessary anymore and will be removed soon.

===interactive_homedir.py===
This is where I am spending the bulk of my time now. This script assumes you are running a pre-3.x version of python because I haven't tested it in 3.x. Give it a shot if you like and feel free to port anything that doesn't work fluidly between the versions.

===usage of interactive_homedir.py===
Run it, follow directions. There is a comment in the header of the file that talks about running this with +x props via
<pre>$ ./interactive_homedir.py</pre>

but if you want to operate in a stricter environment, erase/comment out the env line (line 1) and run it with your preferred version of python:
<pre>$ /usr/local/python-2.7.3/bin/python interactive_homedir.py</pre>

