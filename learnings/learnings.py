import os
from datetime import date

names = [('Asfakul', 'Laskar'), ('Noor', "Islam")]
# To have 2 different variables, it should be a list of iterables
for name, surname in names:
    print('name: %s, surname:  %s' % (name, surname))

if os.path.exists('guru.txt'):
    src = os.path.realpath('guru.text')
    # Full Path or absolute path
    print(os.path.realpath(src))
    # only the file name minus path
    print(os.path.basename(src))

# check if a file exist
if not os.path.exists('kohls.txt'):
    print('kohls.txt does not exist')
# Join strings
today = date.today().strftime('%Y%m%d')
print(''.join(['lb', '_', 'supplier_partner', '_', 'extract', '.xls']))


