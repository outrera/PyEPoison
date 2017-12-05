# from E3DLib.admin import is_admin
from E3DLib.admin import runAsAdmin
import os
locate = os.path.dirname(os.path.abspath('../python/'))
# if not is_admin():
runAsAdmin('')
print(locate + "\python\py.exe")
