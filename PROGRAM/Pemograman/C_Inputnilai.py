from texttable import Texttable

def inputnilai() :
    table2 = Texttable ()

    no2 = 0      
    nama2 = []
    nim2 = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    jawab2 = "y"

    while(jawab2 == "y"):
        print (("\n"),("~"*3),("INPUTAN NILAI"),("~"*3))
        nama2.append(input("\nMasukan Nama : "))
        nim2.append(input("Masukan NIM  : "))
        nilai_tugas.append(input("Nilai Tugas  : "))
        nilai_uts.append(input("Nilai UTS    : "))
        nilai_uas.append(input("Nilai UAS    : "))
        jawab2 = input("\n  Tambahkan Data INPUTAN NILAI (y/t)? ")
        print ("")
        no2 += 1
    
    for i2 in range(no2):
        tugas = int(nilai_tugas[i2])
        uts = int(nilai_uts[i2])
        uas = int(nilai_uas[i2])
        akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100)
        table2.set_cols_dtype(['a','i','i','i','i','i','i'])
        table2.add_rows([['NO','NAMA','NIM','TUGAS','UTS','UAS','AKHIR'],[i2+1,nama2[i2],nim2[i2],nilai_tugas[i2],nilai_uts[i2],nilai_uas[i2],akhir]])
    print (("\n"*2),("~"*3),("TABLE INPUTAN NILAI"),("~"*3))
    print (table2.draw())



