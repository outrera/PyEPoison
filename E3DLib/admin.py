import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def runAsAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "py.exe -m test.py", None, 1)
