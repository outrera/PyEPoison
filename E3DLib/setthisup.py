import E3DLib.admin
import os
if not is_admin():
    runAsAdmin('-m setthisup.py')
else:
    locate = os.path.dirname(os.path.abspath('../python/'))
    handle = open(locate + "\FRST.txt", "r+", encoding="utf8")
    firsttime = int(handle.readline())
    if firsttime is 1:
        setup_ports()
