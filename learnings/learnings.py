import os
from datetime import date, datetime
from shutil import make_archive
from zipfile import ZipFile
from xml.etree import ElementTree
import cx_Oracle

names = [('Asfakul', 'Laskar'), ('Noor', "Islam")]
# To have 2 different variables, it should be a list of iterables
for name, surname in names:
    print('name: %s, surname:  %s' % (name, surname))

if os.path.exists('guru.txt'):
    src = os.path.realpath('guru.text')
    # Full Path or absolute path
    # src = (os.path.realpath(src))
    print(src)
    root_dir, tail = os.path.split(src)
    print('root: %s, tail: %s' %(root_dir, tail))

    # only the file name minus path
    print(os.path.basename(src))
    # this will create a .zip file with everything inside root_dir
    # make_archive('supplier_partner_extracts', 'zip',root_dir)

    with ZipFile('supplier_partner_extracts.zip', 'w') as newzip:
        newzip.write('guru.txt')

# check if a file exist
if not os.path.exists('kohls.txt'):
    print('kohls.txt does not exist')
# Join strings
today = date.today().strftime('%Y%m%d')
print(''.join(['lb', '_', 'supplier_partner', '_', 'extract', '.xls']))

# reading through duplicate tags

root = ElementTree.fromstring("""<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="web">
    <title lang="en">XQuery Kick Start</title>
    <author>James McGovern</author>
    <author>Per Bothner</author>
    <author>Kurt Cagle</author>
    <author>James Linn</author>
    <author>Vaidyanathan Nagarajan</author>
    <year>2003</year>
    <price>49.99</price>
  </book>
  <book category="web">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>
""")

# Print string version
# print(ElementTree.tostring(root, encoding='utf-8').decode('utf-8'))
for book in root.findall('book'):
    title = book.find('title').text
    # join to make a string
    author = ';'.join([author.text for author in book.findall('author')])
    year = book.find('year').text
    price = book.find('price').text
    print('title: {0} \nauthor: {1} \nyear: {2} \nprice: {3}'.format(title, author, year, price))

effective_date = datetime.strptime('11-JUNE-2019', '%d-%B-%Y')
print(effective_date)


# Demo of callproc
# item_number =
try:
    con = cx_Oracle.connect('maubatch_test/maubatch_test@mauaix81/rtktst10')
    # # col_name
    cursor = con.cursor()
    # # declare OUT cursor variable
    # ret_cursor = con.cursor()
    # # l_cur = cursor.var(cx_Oracle.CURSOR)
    # cursor.callproc('item_data', ['23092059', ret_cursor])
    # col_name = [col[0] for col in ret_cursor.description]
    # print(col_name)
    # # for line in ret_cursor:
    # #     print(line)
    execute_date = '20170605'
    sql_string = "SELECT * FROM item_master WHERE TRUNC(create_datetime) = TO_DATE(:cre_date,'YYYYMMDD'"
    cursor.prepare(sql_string)
    cursor.execute(None, cre_date=execute_date)
    print(cursor.rowcount)
except Exception as e:
    print(e)
finally:
    con.close()
    print('Connection Closed')



