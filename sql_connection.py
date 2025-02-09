import pypyodbc as odbc 

DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'sarangs-X1-G10\SQLEXPRESS'
DATABASE_NAME = 'DWH'

connection_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trusted_Connection=yes;"""

connection = odbc.connect(connection_string)
print(connection)