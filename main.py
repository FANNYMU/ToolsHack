import time
import pywhatkit
import pyautogui
import datetime
import os
import webbrowser


def home():
    while True:
        pyautogui.alert("Selamat Datang Di Haking\n\nAda yang bisa saya bantu?\n\n1. SPAM WA\n2. Bobol Password\n3. EXIT")
        
        userInput = pyautogui.prompt("Masukan nomor pilihan anda: ")
        
        if userInput == '1':
            spam()
        elif userInput == '2':
            try:
                from hack import main
                main()
            except ImportError:
                pyautogui.alert("Module hack tidak ditemukan.")
        elif userInput == '3':
            exit()
        else:
            pyautogui.alert("Maaf, pilihan anda tidak tersedia. Silahkan coba lagi!")


def spam():
    pyautogui.alert("OPTION\n\n1. Text\n2. Gambar")
    
    inputNomorSpam = pyautogui.prompt("Pilih nomor yang anda inginkan: ")

    if inputNomorSpam == '1':
        text()
    elif inputNomorSpam == '2':
        gambar()
    else:
        pyautogui.alert("Pilihan tidak valid, silakan coba lagi.")
        spam()


def text():
    nomor = pyautogui.prompt("Masukan nomor WhatsApp yang ingin anda spam, dengan kode negara, tanpa tanda '+': ")
    pesan = pyautogui.prompt("Masukan pesan yang ingin dikirim: ")
    jumlahSpam = int(pyautogui.prompt("Masukan jumlah spam yang ingin anda lakukan: "))
    jeda = int(pyautogui.prompt("Masukan jeda waktu antar pesan (dalam detik): "))

    for _ in range(jumlahSpam):
        pywhatkit.sendwhatmsg_instantly(f"+{nomor}", pesan)
        time.sleep(jeda)

    pyautogui.alert(f"Spam sebanyak {jumlahSpam} pesan telah dilakukan ke nomor {nomor}")


def gambar():
    pyautogui.alert("1. love\n2. kotak\n3. lingkaran\n4. segitiga")
    
    pesanGambar = pyautogui.prompt("Masukan nomor gambar: ")

    if pesanGambar == '1':
        love()
    elif pesanGambar == '2':
        kotak()
    elif pesanGambar == '3':
        bulat()
    elif pesanGambar == '4':
        segitiga()
    else:
        pyautogui.alert("Pilihan tidak valid, silakan coba lagi.")
        gambar()


def love():
    nomor = pyautogui.prompt("Masukan nomor WhatsApp yang ingin anda spam, dengan kode negara, tanpa tanda '+': ")
    pesan = '''
                 ** **
                *  *  *
                *     *
                 *   *
                  * *
                   *'''

    jumlahSpam = int(pyautogui.prompt("Masukan jumlah spam yang ingin anda lakukan: "))
    jeda = int(pyautogui.prompt("Masukan jeda waktu antar pesan (dalam detik): "))

    for _ in range(jumlahSpam):
        pywhatkit.sendwhatmsg_instantly(f"+{nomor}", pesan)
        time.sleep(jeda)

    pyautogui.alert(f"Spam sebanyak {jumlahSpam} pesan telah dilakukan ke nomor {nomor}")


def kotak():
    nomor = pyautogui.prompt("Masukan nomor WhatsApp yang ingin anda spam, dengan kode negara, tanpa tanda '+': ")
    pesan = '''
                 *****
                 *   *
                 *   *
                 *****
              '''

    jumlahSpam = int(pyautogui.prompt("Masukan jumlah spam yang ingin anda lakukan: "))
    jeda = int(pyautogui.prompt("Masukan jeda waktu antar pesan (dalam detik): "))

    for _ in range(jumlahSpam):
        pywhatkit.sendwhatmsg_instantly(f"+{nomor}", pesan)
        time.sleep(jeda)

    pyautogui.alert(f"Spam sebanyak {jumlahSpam} pesan telah dilakukan ke nomor {nomor}")


def bulat():
    nomor = pyautogui.prompt("Masukan nomor WhatsApp yang ingin anda spam, dengan kode negara, tanpa tanda '+': ")
    pesan = '''
                      *****     
                    *********   
                   ***********  
                  ************* 
                  ************* 
                  ************* 
                  ************* 
                   ***********  
                    *********   
                      *****     
              '''

    jumlahSpam = int(pyautogui.prompt("Masukan jumlah spam yang ingin anda lakukan: "))
    jeda = int(pyautogui.prompt("Masukan jeda waktu antar pesan (dalam detik): "))

    for _ in range(jumlahSpam):
        pywhatkit.sendwhatmsg_instantly(f"+{nomor}", pesan)
        time.sleep(jeda)

    pyautogui.alert(f"Spam sebanyak {jumlahSpam} pesan telah dilakukan ke nomor {nomor}")


def segitiga():
    nomor = pyautogui.prompt("Masukan nomor WhatsApp yang ingin anda spam, dengan kode negara, tanpa tanda '+': ")
    pesan = '''
                     *
                    ***
                   *****
                  *******
                 *********
              '''

    jumlahSpam = int(pyautogui.prompt("Masukan jumlah spam yang ingin anda lakukan: "))
    jeda = int(pyautogui.prompt("Masukan jeda waktu antar pesan (dalam detik): "))

    for _ in range(jumlahSpam):
        pywhatkit.sendwhatmsg_instantly(f"+{nomor}", pesan)
        time.sleep(jeda)

    pyautogui.alert(f"Spam sebanyak {jumlahSpam} pesan telah dilakukan ke nomor {nomor}")


home()
