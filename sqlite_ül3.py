import sqlite3

def create_table():
    conn = sqlite3.connect('epood_dmahdi.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS tooted(first_name TEXT, car_price INTEGER)')
    conn.commit()
    conn.close()

def lisa_tooted():
    conn = sqlite3.connect('epood_dmahdi.db')
    c = conn.cursor()
    first_name = input("Sisesta toote nimi: ")
    car_price = int(input("Sisesta toote hind: "))
    c.execute("INSERT INTO tabel (first_name, car_price) VALUES (?, ?)", (first_name, car_price))
    conn.commit()
    conn.close()
    print("Toode lisatud edukalt!")

def loe_tooted():
    conn = sqlite3.connect('epood_dmahdi.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tabel')
    results = c.fetchall()
    for result in results:
        print(result)
    conn.close()

def otsi_toode():
    conn = sqlite3.connect('epood_dmahdi.db')
    c = conn.cursor()
    first_name = input('Sisestage toote nimi: ')
    c.execute('SELECT * FROM tabel WHERE first_name = ?', (first_name,))
    results = c.fetchall()
    for result in results:
        print(result)
    conn.close()

def kustuta_toode():
    conn = sqlite3.connect('epood_dmahdi.db')
    c = conn.cursor()
    first_name = input('Sisestage toote first_name: ')
    c.execute('DELETE FROM tabel WHERE first_name = ?', (first_name,))
    conn.commit()
    conn.close()

def valikud():
    print('Valige, mida soovite teha:')
    print('1. Lisa toode')
    print('2. Loetle tooted')
    print('3. Otsi toodet')
    print('4. Kustuta toode')
    print('5. Välju programmist')

def main():
    create_table()
    while True:
        valikud()
        valik = input('Sisestage valiku number: ')
        if valik == '1':
            lisa_tooted()
        elif valik == '2':
            loe_tooted()
        elif valik == '3':
            otsi_toode()
        elif valik == '4':
            kustuta_toode()
        elif valik == '5':
            break
        else:
            print('Vale valik. Palun proovige uuesti.')

if __name__ == '__main__':
    main()