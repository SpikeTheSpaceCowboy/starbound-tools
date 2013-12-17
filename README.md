starbound-tools
===============

Miscellaneous collection of scripts and tools for managing a Starbound server.

**Current Starbound Build: Offended Koala**

Upcoming Features:
=================
  * 1. (Complete) xShow users connected I.P. Address next to their name.
    * 1a. Show time users connected.  
  * 2. Implement ability to ban I.P. Addresses (Users) through use of windows firewall rules. 
    * 2a. Timed bans (Eg. 1 hr, 24 hrs, Permanently, etc.)
  * 3. Develop Graphical User Interface for ease of use.
  * 4. (Complete) xChat Log
  * 5. Config file for easy user entry of starbound install path.
  
Requirements:
=============
Tested on Windows 7, runs on various Linux variants with modification. 

* Python 2.7.6

Instructions:
=============
**Connected Users**

* Download and Install Python 2.7.6 - You must install to the default directory, eg. "C:\Python27"
* Download whoLogFile_OffendedKoala.py
* Download Connected Users.bat
* Run Connected Users.bat- Make sure to change the filepath in the .bat file to where you have saved the .py file.

   * Note: This script assumes the path to the starbound server log is:
    * "C:\Steam\Steamapps\common\Starbound"

   * If that is not the directory you have installed Starbound to, either move it there, or point to the correct directory by editing the .py file included in the archive. Edit this line: http://i.imgur.com/TCYTKXT.png 
        
   * This will create a players.txt file, so you can keep a log of when players connected to your server.

**Chat Log**

* Download and Install Python 2.7.6 - You must install to the default directory, eg. "C:\Python27"
* Download ChatLog.py
* Download ChatLog.bat.
* Run ChatLog.bat - Make sure to change the filepath in the .bat file to where you have saved the .py file.

   * Note: This script assumes the path to the starbound server log is:
    *"C:\Steam\Steamapps\common\Starbound"

   * If that is not the directory you have installed Starbound to, either move it there, or point to the correct directory by editing the .py file included in the archive. Edit this line: http://i.imgur.com/TCYTKXT.png 


