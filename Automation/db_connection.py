# connection details
import cx_Oracle

lb_connectionstring = cx_Oracle.makedsn('l00coelbrmsdb01.corp.local', 1521, 'rmscoe')
ca_connectionstring = cx_Oracle.makedsn('l00coecarmsdb01.corp.local', 1521, 'RMSCECA')

