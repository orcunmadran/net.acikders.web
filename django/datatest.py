#SQLite3 kütüphanesi yükleniyor
import sqlite3

#veritabani.db adında bir SQLite3 veri tabanı dosyası oluşturuluyor.
veritabani = sqlite3.connect('db.sqlite3')

#Veri tabanı üzerinde işlemleri gerçekleştirebilmek için bir Cursor objesi oluşturuluyor.
komut = veritabani.cursor()

'''
#Tablo Sıfırlama
komut.execute('DELETE FROM oers_oersTest;')
komut.execute('delete from sqlite_sequence where name="oers_oersTest";')
veritabani.commit()
'''

'''
#Veri tabanındaki tabloları görüntüle
for tablolar in komut.execute('SELECT * FROM oers_oer_data'):
        print(tablolar)
'''
#Veri tabanındaki tabloları görüntüle
for tablolar in komut.execute('SELECT * FROM sqlite_master'):
        print(tablolar)
