def penggajian() :
    from texttable import Texttable
    table1 = Texttable ()

    no1 = 0
    nama1 = []
    jabatan = []
    gaji = []
    jawab1 = "y"

    while (jawab1 == "y"):
        print (("\n"),("~"*3),("PENGGAJIAN"),("~"*3))
        nama1.append(input("\nMasukan nama : "))
        jab = input("Jabatan      : ")
        jabatan.append(jab)
    
        if   (jab == 'Programer'):
              gaji.append('Rp.150.000.000')
              jawab1 = input ("\n Tambahkan Data PENGGAJIAN (y/t)? ")
              print (" ")
              no1 += 1
            
        elif (jab == 'Farmasi'):
              gaji.append('Rp.100.000.000')
              jawab1 = input ("\n Tambahkan Data PENGGAJIAN (y/t)? ")
              print (" ")
              no1 += 1
                                   
        elif (jab == 'Ninja'):
              gaji.append('Rp.50.000.000')
              jawab1 = input ("\n Tambahkan Data PENGGAJIAN (y/t)? ")
              print (" ")
              no1 += 1
             
        else :
              print ("\nJabatan Tidak Ditemukan!") ; input("")
              from A_Start import start 
          
    for i1 in range(no1):
        table1.set_cols_dtype(['i','i','i','i'])
        table1.add_rows([['NO','NAMA','JABATAN','GAJI'],[i1+1,nama1[i1],jabatan[i1],gaji[i1]]])
    print (("\n"*2),("~"*3),("TABLE INPUTAN PENGGAJIAN"),("~"*3))
    print (table1.draw())


 
