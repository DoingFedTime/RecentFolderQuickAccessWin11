# RecentFolderQuickAccessWin11
Python script to add "recent folders" to the Quick Access menu in Windows 11. 
# Quick Access Recent Folders Automation 🗂️💻

![Banner Image](https://www.wintools.info/images/easydark/easy-dark-mode.jpg)

A Python script that helps you to automatically add "Recent" folders to the Quick Access menu in Windows 11.

## 💡 About <a name = "-about"></a>

With the changes in Windows 11, navigating through your frequently used folders can be a bit of a chore. This Python script is here to make things easier by automatically adding "Recent" folders to the Quick Access menu. It's a small but powerful tool that can save you time and make your workflow more efficient. Typically, this is enabled by default, for me it wasn't. 

---

## ⭐ Features <a name = "-features"></a>

- 🚀 Fast and easy to use
- ⌛ Saves you time
- 📈 Makes your workflow more efficient

---

## 💻 Installation <a name = "-installation"></a>

**Automatic** Clone this repository, cd to the directory and run.

```git
git clone https://github.com/YourUsername/RecentFolderQuickAccessWin11.git

Open powershell as an admin and navigate to the directory you put it in. 

python Quick.py
```

**Manual Mode** If you still do not have it set you can manually do this by following these instructions. 

```git

Manually adding Recent folders to Quick access
Here are the steps to manually add Recent folders to Quick access:

Press Win+R to open the Run dialog box.

Type regedit and press Enter to open the Registry Editor. If User Account Control (UAC) prompts you for permission, click on "Yes" to continue.

In the Registry Editor, navigate to the following key: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer

In the right pane, look for ShowFrequent. If it doesn't exist, right-click on the empty space, select New > DWORD (32-bit) Value, and name it ShowFrequent.

Double-click on ShowFrequent to modify it.

Set the Value data to 1 and make sure that Base is set to Hexadecimal. Click on "OK".

Close the Registry Editor.

Restart your computer or log off and log on again to make the changes take effect.

Remember, editing the Registry can have serious consequences if not done correctly, so always proceed with caution and make sure you have a backup of your data.
```
