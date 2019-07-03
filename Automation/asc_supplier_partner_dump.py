import xlwt
import os
import sys
import cx_Oracle
# import db_connection as dc
from datetime import datetime
import pytz


tday = datetime.now(tz=pytz.timezone('US/Pacific')).strftime('%Y%m%d')
extract_types = ('supplier', 'partner', 'supplier partner matrix')
class InvalidBrand(Exception):
    """ This is a custom exception """
    pass


def make_db_connection(brand):

    # Take input from standard input.

    user = sys.argv[1]
    password = sys.argv[2]
    lb_connectionstring = cx_Oracle.makedsn('l00coelbrmsdb01.corp.local', 1521, 'rmscoe')
    ca_connectionstring = cx_Oracle.makedsn('l00coecarmsdb01.corp.local', 1521, 'RMSCECA')

    if brand == 'LB':
        conn = cx_Oracle.connect(user, password, lb_connectionstring)
    elif brand == 'CA':
        conn = cx_Oracle.connect(user, password, ca_connectionstring)
    elif brand == 'MAU':
        pass
    elif brand == 'DRS':
        pass
    else:
        raise InvalidBrand
    return conn


def get_data(type_of_data, conn_obj):

    if type_of_data == extract_types[0]:
        sql_string = 'SELECT * FROM sups ORDER by 1'
    elif type_of_data == extract_types[1]:
        sql_string = 'SELECT * FROM partner ORDER by 1'
    cur = conn_obj.cursor()
    cur.execute(sql_string)
    data = cur.fetchall()
    row_count = cur.rowcount
    col_names = [row[0] for row in cur.description]

    return data, col_names, row_count


def write_excel(brand):
    try:
        defaultpath = os.getenv('TEMP')
        print('Files will be written to {0}'.format(defaultpath))
        os.chdir(defaultpath)
        filename = brand + '_' + tday + '.xls'
        print('Generated file: {}'.format(filename))
        # Make database connection
        db_conn = make_db_connection(brand)
        # get supplier data
        data, col_names, row_count = get_data(extract_types[0], db_conn)

        




        # create workbook object
        wb = xlwt.Workbook()
        # Add a sheet
        sheet_1 = wb.add_sheet('Supplier')
        sheet_1.write(1,1,'Supplier')
        wb.save(filename)
    except InvalidBrand:
        print('Invalid Brand Name, Program wil not exit.')
        sys.exit(1)






if __name__ == '__main__':
    write_excel('LB')






