import pyautogui
import time
import datetime
import os
import webbrowser

def main():
    while True:
        yakin = pyautogui.confirm(text='Lihat Tutorial?', title='', buttons=['Y', 'N'])
        
        if yakin == "Y":
            webbrowser.open("https://fannymu.github.io/Tutorials/")
        elif yakin == "N":
            brute()
            break
        elif yakin is None:
            pyautogui.alert("Dialog ditutup tanpa memilih pilihan.")
            break

def brute():
    pyautogui.alert(f"Current time: {datetime.datetime.now()}")
    userList = "wordlist.txt"
    
    try:
        with open(userList, mode="r") as file:
            time.sleep(3)
            pyautogui.write(file.read(), interval=0.23)  # Type with quarter-second pause in between each key.
    except FileNotFoundError:
        pyautogui.alert(f"File {userList} tidak ditemukan.")
    except Exception as e:
        pyautogui.alert(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
