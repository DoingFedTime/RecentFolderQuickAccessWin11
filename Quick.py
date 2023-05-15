import winreg

def add_recent_folders_to_quick_access():
    key_path = r'Software\Microsoft\Windows\CurrentVersion\Explorer'
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, 
                                   winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, "ShowFrequent", 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(registry_key)

add_recent_folders_to_quick_access()
