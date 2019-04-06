from texttable import Texttable

def pembayaran():
    
    jawab3 = "y"

    while(jawab3 == "y"):
        
        table3 = Texttable ()
        print (("\n"),("~"*3),("PEMBAYARAN"),("~"*3))   
        nama  = (input("\nMasukan Nama  : "))
        nim   = (input("Masukan NIM   : "))
        kelas = (input("Masukan Kelas : "))

#--------------------------------------------------------------------------------------------------#
        pilih_UTS = (input("\nBayar UTS (y/t) ? "))
        if    pilih_UTS == 'y':
              uang_UTS = 50000
        else:
              uang_UTS = 0

        pilih_UAS = (input("\nBayar UAS (y/t) ? "))
        if    pilih_UAS == 'y':
              uang_UAS = 50000
        else:
              uang_UAS = 0

              
#--------------------------------------------------------------------------------------------------#
        pilih_Bulanan = (input("\nBayar BULANAN (y/t) ? "))
        if    pilih_Bulanan == 'y':
              uang_Bulanan = int(input("\n-- BULANAN -- \nDi bayar untuk berapa bulan ? "))
              total_Bulanan = 500000*uang_Bulanan
        else:
              total_Bulanan = 0

              
#--------------------------------------------------------------------------------------------------#
        pilih_Seminar = (input("\nBayar SEMINAR (y/t) ? "))
        if     pilih_Seminar == 'y':
               uang_Seminar = 100000
        else:
               uang_Seminar = 0

            
#--------------------------------------------------------------------------------------------------#
        pilih_Kas = (input("\nBayar KAS (y/t) ? "))
        if     pilih_Kas == 'y':
               uang_Kas = int(input("\n-- KAS -- \nDi bayar untuk berapa bulan ? "))
               total_Kas = 20000*uang_Kas
        else:
               total_Kas = 0


#--------------------------------------------------------------------------------------------------#
        print ("\n\nBiaya Admin 5000");input('')
        uang_Admin = 5000

        grand_total = uang_UTS+uang_UAS+total_Bulanan+uang_Seminar+total_Kas+uang_Admin

               
#--------------------------------------------------------------------------------------------------#
        table3.set_cols_dtype(['i','i','i','i','i','i','i','i','i','i'])
        table3.add_rows([['NAMA','NIM','KELAS','UTS','UAS','BULANAN','SEMINAR','KAS','ADMIN','TOTAL'],
                         [nama,nim,kelas,uang_UTS,uang_UAS,total_Bulanan,uang_Seminar,total_Kas,uang_Admin,grand_total]])
        print ("\n")
        print (table3.draw())
        
        jawab3 = input("\n  Tambahkan Data PEMBAYARAN (y/t)? ") ; print("")
 
            

