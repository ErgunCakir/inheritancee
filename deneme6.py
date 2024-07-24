class Materyal:
    def __init__(self, baslik, yazar, yayin_yili):
        self.baslik = baslik
        self.yazar = yazar
        self.yayin_yili = yayin_yili
    
    def bilgi_ver(self):
        raise NotImplementedError("Bu metod alt sınıflar tarafından uygulanmalıdır.")
    
    def __str__(self):
        return f"{self.baslik} - {self.yazar}, {self.yayin_yili}"

class Kitap(Materyal):
    def __init__(self, baslik, yazar, yayin_yili, sayfa_sayisi):
        super().__init__(baslik, yazar, yayin_yili)
        self.sayfa_sayisi = sayfa_sayisi
    
    def bilgi_ver(self):
        return f"{self.baslik} yazarı {self.yazar} tarafından {self.yayin_yili} yılında yayınlanmıştır. Toplam {self.sayfa_sayisi} sayfa."

    def __str__(self):
        return f"Kitap: {super().__str__()}, Sayfa Sayısı: {self.sayfa_sayisi}"

class Dergi(Materyal):
    def __init__(self, baslik, yazar, yayin_yili, sayi):
        super().__init__(baslik, yazar, yayin_yili)
        self.sayi = sayi
    
    def bilgi_ver(self):
        return f"{self.baslik} adlı dergi, {self.yayin_yili} yılında {self.yazar} tarafından yayınlanmıştır. Bu, {self.sayi}. sayıdır."

    def __str__(self):
        return f"Dergi: {super().__str__()}, Sayi: {self.sayi}"

class Dizi(Materyal):
    def __init__(self, baslik, yazar, yayin_yili, sezon_sayisi, bolum_sayisi):
        super().__init__(baslik, yazar, yayin_yili)
        self.sezon_sayisi = sezon_sayisi
        self.bolum_sayisi = bolum_sayisi
    
    def bilgi_ver(self):
        return f"{self.baslik}, {self.yayin_yili} yılında {self.yazar} tarafından yayınlanmıştır. {self.sezon_sayisi} sezon ve toplam {self.bolum_sayisi} bölümden oluşmaktadır."

    def __str__(self):
        return f"Dizi: {super().__str__()}, Sezon Sayısı: {self.sezon_sayisi}, Bölüm Sayısı: {self.bolum_sayisi}"

kitap = Kitap("Python Programlama", "Guido van Rossum", 2020, 350)
dergi = Dergi("Bilim ve Teknik", "TÜBİTAK", 2021, 56)
dizi = Dizi("Breaking Bad", "Vince Gilligan", 2008, 5, 62)

print(kitap)
print(kitap.bilgi_ver())
print(dergi)
print(dergi.bilgi_ver())
print(dizi)
print(dizi.bilgi_ver())   
