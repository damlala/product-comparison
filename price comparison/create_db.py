import sqlite3

# users.db dosyasını oluştur
conn = sqlite3.connect('users.db')

# users tablosunu oluştur
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Örnek kullanıcı ekle (opsiyonel)
conn.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('test', '1234'))

conn.commit()
conn.close()

print("Veritabanı başarıyla oluşturuldu.")
