class pesan(object):
    """
    sebuah class bernama pesan
    """
    def __init__(self,string):
        self.teks=string
    def cetak(self):
        print(self.teks)
    def cetakkapital(self):
        print(str.upper(self.teks))
    def cetakkecil(self):
        print(str.lower(self.teks))
    def jumkar(self):
        return len(self.teks)
    def cetakjumlah(self):
        print("kalimatku mempunyai: ",len(self.teks),"karakter")
    def perbarui(self,strbaru):
        self.teks = strbaru
# NO 1 a
    def terkandung(self,x):
        a=str(x)
        if x in self.teks:
            print("true")
        else:
            print("false")
# NO 1 b
    def hitungk(self):
        a='aioueAIOUE'
        x=0
        for i in self.teks:
            if i not in a:
                x+=1
        return(x)
# NO 1 c    
    def hitungv(self):
        a='aioueAIOUE'
        x=0
        for i in self.teks:
            if i in a:
                x+=1
        return(x)

# eksekusi 1a
a=pesan("indonesia adalah negeri tercinta")
a.terkandung("negeri")
a.terkandung("adelah")

# eksekusi 1b
b= pesan("Muhammadiyah")
print(b.hitungk())

# eksekusi 1c
print(b.hitungv())




