from texttable import Texttable

def judul() :
    print ("\n\n")
    print ("="*51)                              
    print ("~"*17,"MENU PEMOGRAMAN","~"*17)
    print (("="*51),("\n By: M.Shiddiqy (311810604)"),("\n"))
    
    table = Texttable ()
    print ("")
    table.add_rows([['NO','JENIS PEMOGRAMAN'],['1.','PENGGAJIAN'],['2.','INPUTAN NILAI'],['3.','PEMBAYARAN'],['4.','KALKULATOR']])
    print (table.draw())


