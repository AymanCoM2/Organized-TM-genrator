import pyodbc
from . import a_functions_LB


def runRowQuery(docNumber):
    rowQuery = a_functions_LB.replaceRowsQuery(str(docNumber))
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=10.10.10.100;"
                          "Database=LB;"
                          "UID=ayman;"
                          "PWD=admin@1234;")
    cursor = conn.cursor()
    cursor.execute(rowQuery)
    rowResult = cursor.fetchall()
    return rowResult


def runHeaderFooterQuery(docNumber):
    headerfooterQuery = a_functions_LB.replaceHeaderFooterQuery(str(docNumber))
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=10.10.10.100;"
                          "Database=LB;"
                          "UID=ayman;"
                          "PWD=admin@1234;")
    cursor = conn.cursor()
    cursor.execute(headerfooterQuery)
    headerFooterResult = cursor.fetchall()
    return headerFooterResult
