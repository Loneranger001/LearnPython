import xlwt
import os
import sys
import cx_Oracle
import db_connection
from datetime import datetime
import pytz




tday = datetime.now(tz=pytz.timezone('US\Eastern')).strftime('%Y%m%d%H%M%S')

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


def write_excel(brand):








