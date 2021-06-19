#SQLite3 kütüphanesi
import sqlite3

#veritabani.db adında bir SQLite3 veri tabanı dosyası oluşturuluyor.
veritabani = sqlite3.connect('db.sqlite3')

#Veri tabanı üzerinde işlemleri gerçekleştirebilmek için bir Cursor objesi oluşturuluyor.
komut = veritabani.cursor()

'''
#Tablo Sıfırlama
komut.execute('DELETE FROM pages_oerdata;')
komut.execute('DELETE FROM sqlite_sequence WHERE name="pages_oerdata";')
veritabani.commit()
'''

'''
#Veri tabanındaki tabloları görüntüle
for tablolar in komut.execute('SELECT * FROM oers_oer_data'):
        print(tablolar)
'''

'''
#Veri tabanındaki tabloları görüntüle
for tablolar in komut.execute('SELECT * FROM sqlite_master'):
        print(tablolar)
'''
