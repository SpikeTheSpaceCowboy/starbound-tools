#!/usr/bin/env python
# This hacky script iterates over your starbound log file and prints a list of
# connected clients. This will work until some update changes log format

# Credit goes to sethdmoore/mcapplbee - He wrote the original code I simply
# -- added to it in order to suit my needs. 

# My changes are as follows:
# Number of connected users & connected users list now writes to a text file
# A timestamp has been added to the end of each request for connected users list
# A 12 hour timer (shown in minutes) has been added to show how long until the --
# -- server needs to be restarted.
#
# -Spike ;p

import time;

# Set this to be the full path to your log file
STARBOUND_LOGFILE = "C:\Steam\Steamapps\common\Starbound\starbound_server.log"

# Log keywords
# connected disconnected = duh
# connection = reaped ... we delete these keys from the dict
# " " = loading ship world received from client
    
def main():
    clients = {}
    # Timer process starts here (Goes for 12 hours 5 mins)
    counter = 43210
    start = time.time()
    while True:
        # Main log parsing process starts here
        with open(STARBOUND_LOGFILE, 'r') as log:
            for line in log:
            # Chat begins with two spaces in the log and contains a caret.
            # Find it and strip it as we don't want to count chat
                status = line.split(': ')
                if len(status) > 1:
                    status = ""
            # Now we can detect carets as connection messages
                status = line.split('<User: ')
                if len(status) > 1:
                # Strip new lines and ending carets
                    status = status[1].replace("\n", "")
                # Detect client number and set their status
                # if status.split(" ")[1] == "<User:":
                    if len(status.split("> ")) > 1:
                        clients[status.split("> ")[0]] = status.split("> ")[1]

        # Clean reaped players from dictionary
        for player, status in clients.items():
        # Player's connection has been reaped, keyword connection
            if status == 'connection':
                del clients[player]
        # Prints Total number of connected players to file (players.txt) & the screen
        PlayerLog = open("players.txt", "a")
        print "Total Connected Players: %s" % len(clients.keys())
        Endline = "\nTotal Connected Players: %s \n" %len(clients.keys())
        PlayerLog.seek(0, 2)
        line= PlayerLog.write( Endline )
        PlayerLog.close
        # Prints List of connected players to file (players.txt) & the screen
        for player, status in clients.iteritems():
            PlayerLog = open("players.txt", "a")
            print "[client %s = %s]" % (player, status)
            Endline = "[client %s = %s] \n" % (player, status)
            PlayerLog.seek(0, 2)
            line= PlayerLog.write( Endline )
            PlayerLog.close
        # Gets the local time and prints it after users list to screen and file (players.txt)
        localtime = time.asctime( time.localtime(time.time()) )
        print " "
        PlayerLog = open("players.txt", "a")
        print "Time checked:", localtime
        Endline = "\nTime Checked: "
        PlayerLog.seek(0, 2)
        line= PlayerLog.write( Endline )
        PlayerLog.close
        PlayerLog = open("players.txt", "a")
        Endline = localtime
        PlayerLog.seek(0, 2)
        line= PlayerLog.write( Endline )
        PlayerLog.close
        PlayerLog = open("players.txt", "a")
        Endline = "\n\n"
        PlayerLog.seek(0, 2)
        line= PlayerLog.write( Endline )
        PlayerLog.close
        print " "
        # Timer countdown process begins here-Loops back to beginning-Prints to screen only
        time.sleep(30)
        if time.time() - start > 1:
            start = time.time()
            counter = counter - 1
        print "%s minutes remaining until server needs to be restarted." % counter
        print " "
        # Timer stops here when it reaches 0
        if counter <=0:
            break
        
if __name__ == '__main__':
    main()
