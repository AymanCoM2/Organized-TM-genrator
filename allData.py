#################################
## This script is Only Used Once 
## to Load Data From the DB 
#################################


import pyodbc
from lightSql import connect_and_query_db

def replaceHeaderFooterQuery():
    headerFooterQuery = """ 
        SELECT T0.DocEntry, CASE WHEN ISNULL(T0.LicTradNum, '') = '' THEN N'فاتورة ضريبية مبسطة'
        ELSE N'فاتورة ضريبية' END AS 'InvoiceTitle',
        T0.CardName, T0.CardCode , T0.LicTradNum , T0.DocDate , T0.DocDueDate ,
        CONCAT(ISNULL(N1.SeriesName,'') ,T0.DocNum )  'DocNum',
        (T0.DocTotal + T0.DiscSum - T0.RoundDif - T0.VatSum) 'NetTotalBefDisc',
        T0.DiscPrcnt , T0.DiscSum ,
        (T0.DocTotal - T0.RoundDif - T0.VatSum) 'NetTotalBefVAT',
        T0.VatSum , T0.DocTotal , T00.U_NAME , T0.Comments 
        FROM TM.DBO.OINV T0
        LEFT JOIN TM.DBO.NNM1 N1 ON N1.Series = T0.Series
        LEFT JOIN  TM.DBO.OUSR T00 ON T0.USERSIGN = T00.INTERNAL_K
        WHERE 
        T0.CANCELED ='N' 
        """
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=10.10.10.100;"
                          "Database=LB;"
                          "UID=ayman;"
                          "PWD=admin@1234;")
    cursor = conn.cursor()
    cursor.execute(headerFooterQuery)
    headerFooterResult = cursor.fetchall()
    return headerFooterResult

def replaceRowsQuery():
    rowsQuery = """ 
        SELECT
        T0.DocNum , T1.DocEntry, T1.ItemCode, T1.Dscription, T1.Quantity , T1.unitMsr , L0.Location ,
        T1.PriceBefDi , T1.DiscPrcnt , T1.Price , 
        ROUND(T1.Price * T1.Quantity,2) 'TotalBefVAT',
        ROUND(ROUND(T1.Price * T1.Quantity,2) * 1.05 ,2) 'TotalAftVAT'
        FROM 
        (TM.DBO.OINV T0 inner join TM.DBO.INV1 T1 on T1.DocEntry= T0.DocEntry)
        LEFT JOIN (TM.DBO.OWHS W0 LEFT JOIN TM.DBO.OLCT L0 ON W0.Location = L0.Code)
        ON W0.WhsCode = T1.WhsCode
        WHERE T1.DocEntry IN (SELECT T0.DocEntry FROM TM.DBO.OINV T0 WHERE T0.CANCELED ='N')
    """
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=10.10.10.100;"
                          "Database=LB;"
                          "UID=ayman;"
                          "PWD=admin@1234;")
    cursor = conn.cursor()
    cursor.execute(rowsQuery)
    rowResult = cursor.fetchall()
    return rowResult

# res1 = replaceRowsQuery()
res1 = replaceHeaderFooterQuery()
db_file = 'Schedules.sqlite'
for item in res1:
    docNumber = item[0] 
    invoiceSet = 0 
    phoneNumber = "None" 
    insert_query = "INSERT INTO Schedules (docNumber, invoiceSet, phoneNumber) VALUES (?, ?, ?);"
    data_to_insert = (docNumber , invoiceSet , phoneNumber)
    result = connect_and_query_db(db_file, insert_query, data_to_insert)
    print(insert_query)
