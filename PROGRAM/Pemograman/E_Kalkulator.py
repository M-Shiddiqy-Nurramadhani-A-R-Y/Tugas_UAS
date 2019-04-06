from texttable import Texttable

def kalkulator():
    
    jawab4 = "y"
    while(jawab4 == "y"):
        table4 = Texttable ()
        #---pilih---#
        print (("\n"),("~"*3),("KALKULATOR"),("~"*3))
        table4.add_rows([['NO','JENIS HITUNGAN'],['1.','(+) Penjumlahan'],['2.','(-) Pengurangan'],['3.','(x) Perkalian'],['4.','(:) Pembagian']])
        print (table4.draw())
        
        jenishitungan = (input("\n--> Masukan Pilihan JENIS HITUNGAN ?  "))

        if   jenishitungan == '1':
             print("\n+ Penjumlahan +")
             angka1 = int(input("Masukan angka pertama : "))
             angka2 = int(input("Masukan angka kedua   : "))
             hasil = angka1+angka2
             print("\n>",angka1,"+",angka2,"=",hasil,"\n")
            
        elif jenishitungan == '2':
             print("\n- Pengurangan -")
             angka1 = int(input("Masukan angka pertama : "))
             angka2 = int(input("Masukan angka kedua   : "))
             hasil = angka1-angka2
             print("\n>",angka1,"-",angka2,"=",hasil,"\n")

        elif jenishitungan == '3':
             print("\nx Perkalian x")
             angka1 = int(input("Masukan angka pertama : "))
             angka2 = int(input("Masukan angka kedua   : "))
             hasil = angka1*angka2
             print("\n>",angka1,"x",angka2,"=",hasil,"\n")

        elif jenishitungan == '4':
             print("\n: Pembagian :")
             angka1 = int(input("Masukan angka pertama : "))
             angka2 = int(input("Masukan angka kedua   : "))
             hasil = angka1/angka2
             print("\n>",angka1,":",angka2,"=",hasil,"\n")

        else:
            print (("\n        !!! WARNING !!!        "),("\n!!! Pilihan Tidak Ditemukan !!!"))

            
        jawab4 = input("\n  Tambahkan Data KALKULATOR (y/t)? ") ; print("")

 
