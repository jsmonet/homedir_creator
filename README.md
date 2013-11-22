##Homedir creation script##
This python script is meant for use on linux operating systems. You can get it to run on OSX, but I haven't seen any real reason to use it there yet, so I haven't tested that use.

There are a few caveats here. I wrote this in a Python 2.6.x~2.7.x series of environments. I use bash commonly, and the default zsh on Isilon nodes. This is a trivial piece of information because Python takes the reigns right away, but I do not want anyone living in the likes of tcsh saying I didn't warn them of odd unseen issues. Also, dude... bash is the business. <3 bash.

I understand people will be hesitant to run things directly on the storage servers, but there's something delightfully Slim Pickens-riding-the-bomb-in-strangelove about rockin' out right on the nodes.

###interactive_homedir.py###
This is where I am spending the bulk of my time now. This script assumes you are running a pre-3.x version of python because I haven't tested it in 3.x. Give it a shot if you like and feel free to port anything that doesn't work fluidly between the versions.

I may remove the #! header in future revisions. It really does breed bad habits and imprecision in multi-python-revision servers. You would simply run the script with <your path to python> interactive_homedir.py. This is a trivial bit of aliasing. 

Leaving the header in place, if you chmod +x the file you can run it like a binary. If I remove the header and you're bummed about it, just add it back and you're in business.

###isi_int_homedir.py###
Funny enough, I've removed the #! header because I'd prefer to force people to run this as python executing a python script rather than something standalone. I've checked all the functionality against our Isilon cluster running OneFS v7.0.2.1 and Python 2.6.1. If you're running an earlier revision of OneFS and/or Python, just open an interactive Python session and try the commands out against your users and a /tmp dir on one of the nodes. 

This version replaces org_pwnam[5], which returns the declared homedir, with the /ifs/home/%s + org_pwnam[0] (username) string because we mount homedirs to a simpler path than what you have on the cluster. Sure I could change the homedir path on the cluster, but I prefer it this way. 

There is a preceeding line echoing what the homedir path will be as mounted and what the script will create on the cluster. The non-isi version simply shows you the mounted path as it assumes creation on a different server against a mounted path of /ifshome/username. 


