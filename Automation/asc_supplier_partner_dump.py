import xlwt
import os
import sys
import cx_Oracle
# import db_connection as dc
from datetime import datetime
import pytz
import traceback

t_day = datetime.now(tz=pytz.timezone('US/Pacific')).strftime('%Y%m%d')
extract_types = ('supplier', 'partner', 'supplier_partner_matrix')
sheet_names = ('Supplier', 'Partner', 'SupplierPartnerMatrix')


class InvalidBrand(Exception):
    """ This is a custom exception """
    pass


# define the function
def send_mail(*args):
    for arg in args:
        print('Email {}'.format(arg))


def make_db_connection(brand):

    # Take input from standard input.
    # user = sys.argv[1]
    # password = sys.argv[2]
    user = 'alaskar_db'
    password = 'Ascena2020!'
    lb_connectionstring = cx_Oracle.makedsn('ORAPRDCSTR01-SCAN.corp.local', 1521, service_name='RMSPRD.corp.local')
    ca_connectionstring = cx_Oracle.makedsn('ORAPRDCSTR01-SCAN.corp.local', 1521, service_name='RMSPRCA.corp.local')
    drs_connectionstring = cx_Oracle.makedsn('dbrmsproddb', 1521, 'RMSPRD')
    mau_connectionstring = cx_Oracle.makedsn('mauaix21', 1521, service_name='rtkprd10')
    try:
        if brand == 'LB':
            conn = cx_Oracle.connect(user, password, lb_connectionstring)
        elif brand == 'CA':
            conn = cx_Oracle.connect(user, password, ca_connectionstring)
        elif brand == 'MAU':
            conn = cx_Oracle.connect(user, password, mau_connectionstring)
        elif brand == 'DRS':
            conn = cx_Oracle.connect(user, password, drs_connectionstring)
        else:
            raise InvalidBrand
    except ConnectionError:
        print(traceback.print_exc())
        raise
    except Exception:
        print(traceback.print_exc())
        raise
    else:
        print('Connection Successfully Established!')
    return conn


def get_data(type_of_data, conn_obj, brand):
    if type_of_data == extract_types[0]:
        sql_string = 'SELECT * FROM {0} ORDER by 1'.format('sups')
    elif type_of_data == extract_types[1]:
        sql_string = 'SELECT * FROM {0} ORDER by 1'.format('partner')
    elif type_of_data == extract_types[2]:
        if brand in ('LB', 'CA'):
            sql_string = 'SELECT * FROM {0} ORDER by 1'.format('ASCENA_SUPPLIER_PARTNER_MATRIX')
        elif brand == 'MAU':
            sql_string = 'SELECT * FROM {0} ORDER by 1'.format('ASC_SUPPLIER_PARTNER_XREF')
        elif brand == 'DRS':
            sql_string = 'SELECT * FROM {0} ORDER by 1'.format('DRS_SUPPLIER_PARTNER_XREF')

    cur = conn_obj.cursor()
    cur.execute(sql_string)
    data = cur.fetchall()
    row_count = cur.rowcount
    col_names = [row[0] for row in cur.description]
    cur.close()
    return data, col_names, row_count


def write_excel(brand):
    try:
        defaultpath = os.getenv('TEMP')
        print('Files will be written to {0}'.format(defaultpath))
        os.chdir(defaultpath)
        filename = brand + '_' + t_day + '.xls'
        print('Generated file: {}'.format(filename))
        # Make database connection
        db_conn = make_db_connection(brand)
        # data, col_names, row_count = get_data(extract_types[0], db_conn)
        # print(row_count)
        # create workbook object
        wb = xlwt.Workbook()
        # Add the sheets
        sheet_1 = wb.add_sheet(sheet_names[0], cell_overwrite_ok=True)
        sheet_2 = wb.add_sheet(sheet_names[1], cell_overwrite_ok=True)
        sheet_3 = wb.add_sheet(sheet_names[2], cell_overwrite_ok=True)
        # Loop through extract types and get the data
        for type_of_extract in extract_types:
            data, col_names, row_count = get_data(type_of_extract, db_conn, brand)
            if type_of_extract == 'supplier':
                sheet = sheet_1
            elif type_of_extract == 'partner':
                sheet = sheet_2
            elif type_of_extract == 'supplier_partner_matrix':
                sheet = sheet_3

            # write the column names
            i = 0
            for name in col_names:
                sheet.write(0, i, name)
                i += 1
            # write the data
            k = 1
            for rows in data:
                j = 0
                for each_col in rows:
                    sheet.write(k, j, each_col)
                    j += 1
                k += 1
        wb.save(filename)
    except InvalidBrand:
        print('Invalid Brand Name, Program wil now exit.')
        raise
    except Exception:
        print(traceback.print_exc())
        raise
    finally:
        db_conn.close()
        print('Connection Closed for {0}'.format(brand))


if __name__ == '__main__':
    write_excel('LB')
    write_excel('MAU')
    write_excel('DRS')
    write_excel('CA')






