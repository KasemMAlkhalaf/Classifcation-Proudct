import sqlite3
import csv
conn = sqlite3.connect('DataOne.sqlite')
cur = conn.cursor()
cur.execute('Drop table if exists DataOneTable')
cur.execute('''create table "DataOneTable" ( "Product_id" text ,
 "Text" text ,"Rate" int , "summary" text  )''')
fname = input('Enter the ecoplanet csv file name ')
if len(fname) < 1:
    fname = "phone.csv"
with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
        id = row[0]
        name = row[1]
        rate = row[2]
        summary = row[3]
        cur.execute(
            '''insert into DataOneTable( Product_id , Text, Rate, summary ) values (?,?,?,?)''', (id, name, rate, summary))
        conn.commit()
