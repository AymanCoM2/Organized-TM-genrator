from b_headerFooterData import runHeaderFooterQuery, runRowQuery
from decimal import Decimal


def headerFooterParsing(docNumber):
    headerFooterResult = runHeaderFooterQuery(docNumber)
    hfDict = {}
    for item in headerFooterResult:
        _, description, company, code, _, start_date, end_date, primary_id, * \
            decimals, status, _ = item
        decimals = [float(d) for d in decimals]

        start_date = start_date.strftime('%Y/%m/%d')
        end_date = end_date.strftime('%Y/%m/%d')
        hfDict = {
            'Description': description,
            'Company': company,
            'Code': code,
            'StartDate': start_date,
            'EndDate': end_date,
            'PrimaryID': primary_id,
            'Decimals': decimals,
            'Status': status
        }
# hfDict['PrimaryID']
    headerList = [
        "", "",
        "", "TM"+str(docNumber),
        hfDict['EndDate'], hfDict['StartDate'],
        "", hfDict['Description'],
        hfDict['Code'], hfDict['Company'],
    ]

#   [(10,  -> DocEntry
#   'فاتورة ضريبية مبسطة', Invoice Title
#   'مؤسسة تسويق البناء - شقراء'  CARD Name
#   'D0040',  CardCode
#   None,  الرقم الضريبي
#   datetime.datetime(2019, 5, 5, 0, 0),  StartDate
#   datetime.datetime(2019, 5, 20, 0, 0),  End Date
#   'Primary100009', >> DocNum
#   Decimal('773.400000'),  NetTotalBefDisc
#   Decimal('25.000000'), DiscPrcnt
#   Decimal('193.350000'), "DiscSum" How Much Deduction
#   Decimal('580.050000'),  NetTotalBefVAT
#   Decimal('29.000000'),  VatSum
#   Decimal('609.050000'),  DocTotal
#   'S10',  U_NAME
#   None)] Comments

    footerList = [str(hfDict['Decimals'][0]),
                  str(hfDict['Decimals'][2])+"        " +
                  str(hfDict['Decimals'][1]) + "%",
                  str(hfDict['Decimals'][3]),
                  str(hfDict['Decimals'][4]),
                  str(hfDict['Decimals'][5])
                  ]
    return headerList, footerList


def convert_to_rounded_string(value):
    if isinstance(value, Decimal):
        return str(round(float(value), 1))
    else:
        return str(value)


def rowsParsing(docNumber):
    counter = 1
    rowResult = runRowQuery(docNumber)
    finalDataList = []
    for rRow in rowResult:
        internalList = [
            convert_to_rounded_string(rRow[10]),
            convert_to_rounded_string(rRow[9]),
            convert_to_rounded_string(rRow[8]) + "%",
            convert_to_rounded_string(rRow[7]),
            convert_to_rounded_string(
                rRow[5]) + " " + convert_to_rounded_string(rRow[6]),
            convert_to_rounded_string(rRow[4]),
            convert_to_rounded_string(rRow[3]),
            convert_to_rounded_string(rRow[2]),
            convert_to_rounded_string(counter)
        ]
        finalDataList.append(internalList)
        counter = counter + 1
    return finalDataList


# [(100009 DocNum (0)
#  10   DocEntry (1)
#  '14352307116' ItemCode (2)
#  'كشاف ليد رفيد 10 وات أبيض IP65 ) SMD 6000k )   ( RFE-0260 )' Dscription (3)
#  Decimal('20.000000') Quantity (4)
# 'حبة' unitMsr "Measure" (5)
#  'ER' Location   [ Both Measure and Location are Concatenated ] (6)
#  Decimal('22.670000') PriceBefDi "Before Discount" (7)
#  Decimal('0.000000') DiscPrcnt "Percentage"  (8)
#  Decimal('22.670000') Price "After Discount" (9)
#  Decimal('453.40000000000') TotalBefVAT (10)
#  Decimal('476.070000000')) TotalAftVAT (11)
# ]
