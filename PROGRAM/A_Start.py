from Pemograman.B_Penggajian1 import penggajian
from Pemograman.C_Inputnilai  import inputnilai
from Pemograman.D_Pembayaran1 import pembayaran
from Pemograman.E_Kalkulator  import kalkulator
import getpass


def login():
        print ("\nLogin in system") ; user = input("Username : ") ; password = getpass.getpass ("Password : ")
        if user == 'M.S' and password == '123':
            start()
        else:
            print (("\n                  !!! WARNING !!!                     "),
                   ("\n!!! Username atau Password yang anda masukan salah !!!"))
            login()
            
def start():

    from Pemograman.A_Judul import judul ; judul ()
    pilihan = input("\n--> Masukan Pilihan JENIS PEMOGRAMAN ?  ")
    if   pilihan == '1' :
         penggajian()
    elif pilihan == '2' :
         inputnilai()
    elif pilihan == '3' :
         pembayaran()
    elif pilihan == '4' :
         kalkulator()
    else :
        print (("\n        !!! WARNING !!!        "),("\n!!! Pilihan Tidak Ditemukan !!!"))
    tambahan()


def tambahan() :
    
    tambah = input ("\n--> Kembali Ke MENU PEMOGRAMAN (y/t)? ")
    if tambah == 'y' :
        start()
    else :
        import Pemograman.F_Akhir ; print("")
        
login()
