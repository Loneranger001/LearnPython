import os
from datetime import date
from shutil import make_archive
from zipfile import ZipFile
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


