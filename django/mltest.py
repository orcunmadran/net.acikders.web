#Most Similar Example

from gensim.models import KeyedVectors
import sqlite3

kelimeVektoru = KeyedVectors.load_word2vec_format('model/trModel500', binary=True)

vtBaglanti = sqlite3.connect('db.sqlite3')
vtSorgu = vtBaglanti.cursor()

def benzerKelimeler():

    anahtarKelime = input("Anahtar Kelime / kelimeler: ").lower()
    anahtarKelimeler = anahtarKelime.split()
    print("Anahtar Kelimeler : "+ str(anahtarKelimeler))

    aranacakKelimeler = []
    cikartilanKelimeler = []

    for kelime in anahtarKelimeler:
        if kelime in kelimeVektoru:
            aranacakKelimeler.append(kelime)
        else:
            cikartilanKelimeler.append(kelime)
    print("- - - - -")
    print("Aranacak Kelimeler : " + str(aranacakKelimeler))
    print("Çıkartılan Kelimeler : " + str(cikartilanKelimeler))

    if len(aranacakKelimeler) > 0:
        oneriler = (kelimeVektoru.most_similar(positive=aranacakKelimeler))
    else:
        oneriler = (kelimeVektoru.most_similar(positive="test"))

    print(oneriler)

    #VT Sorgu

    sorguCumlesi = ""
    for oneri in oneriler:
        sorguCumlesi += '''
                        OE.oer_title LIKE '%{keyword}%' OR 
                        OE.oer_subject LIKE '%{keyword}%' OR 
                        OE.oer_description LIKE '%{keyword}%' OR
                        OE.oer_creator LIKE '%{keyword}%' OR
                        OE.oer_publisher LIKE '%{keyword}%' OR 
                        OE.oer_contributor LIKE '%{keyword}%' OR '''.format(keyword = oneri[0])
    sorguCumlesi += " OE.oer_contributor = 'XXXXX'"

    sonucToplam = 0

    print("--- Açık Dersler ---")

    for row in vtSorgu.execute("SELECT OE.oer_title, OE.oer_subject FROM pages_OerData OE WHERE {query}".format(query = sorguCumlesi)):
        print(row)
        sonucToplam +=1
    print(sonucToplam)
    benzerKelimeler()

benzerKelimeler()