import qrcode
from PIL import Image
import pyodbc
# Define the content of the QR code
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_directory, "code.png")


def generateCustomerQRcode(docNumber):
    # SELECT DocEntry, HeX AS 'DT'  FROM [@QRTV]
    # SELECT DocEntry, HeX AS 'DT'  FROM [@QRTV] WHERE DocEntry  = 5
    query = "SELECT DocEntry, HeX AS 'DT'  FROM [@QRTV] WHERE DocEntry  ="
    query = query + str(docNumber)
    conn = pyodbc.connect("Driver={SQL Server};"
                          "Server=10.10.10.100;"
                          "Database=LB;"
                          "UID=ayman;"
                          "PWD=admin@1234;")
    cursor = conn.cursor()
    cursor.execute(query)
    rowResult = cursor.fetchall()
    data = rowResult[0][1]
    # return data
    # 0 Of First Index For the List , 1 For second index For the QR Only

    # Define a list of sizes and resolutions
    size_and_resolution_list = [
        (90, 90, 72),  # Size: 100x100 pixels, Resolution: 72 DPI
        # (100, 100, 72),  # Size: 100x100 pixels, Resolution: 72 DPI
        # (200, 200, 300),  # Size: 200x200 pixels, Resolution: 300 DPI
        # (300, 300, 600),  # Size: 300x300 pixels, Resolution: 600 DPI
    ]

    # Generate QR code images with different sizes and resolutions
    for size, resolution, dpi in size_and_resolution_list:
        qr = qrcode.QRCode(
            version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((size, size), Image.ANTIALIAS)
        img.save(image_path, dpi=(dpi, dpi))

    return 'code.png'
