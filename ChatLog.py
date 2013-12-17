# !/usr/bin/env python
# chatlog.py
# credit to: David M. Beazley (http://www.dabeaz.com/generators/)
# for his "tail -f" equivalent function. It was very helpful.
# -Spike ;p

import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open("C:\Steam\Steamapps\common\Starbound\starbound_server.log","r")
    loglines = follow(logfile)
    for line in loglines:
        status = line.split(':  ')
        if len(status) > 1:
            status = status[1].replace("\n", "")
            localtime = time.strftime("%H:%M:%S")
            print "%s %s\n" % (localtime, status),
