from PartOne import e_mainsCreate, f_merge, q_QR
from whatsApp import hideEveryThing, openBrowser, openWhatasppLinkAndSendMSG, handleUPload
import shutil
import sqlite3


def get_first_unprocessed_document(db_file='Schedules.sqlite'):
    #  CONNECT TO DB and Get the First DOC number That Has false For invoiceSet
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    try:
        # Execute a SQL query to find the first document with invoiceSet as False
        cursor.execute(
            "SELECT docNumber FROM Schedules WHERE invoiceSet = 0 LIMIT 1")
        result = cursor.fetchone()
        if result:
            return result[0]  # Return the docNumber
        else:
            return None  # If no such document is found
    except sqlite3.Error as e:
        print("Error while retrieving data from the database:", e)
    finally:
        # Close the database connection
        conn.close()


def update_invoice_set(doc_entry, db_file='Schedules.sqlite'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    try:
        # Execute an SQL UPDATE statement to set invoiceSet to True for the specified docNumber
        cursor.execute(
            "UPDATE Schedules SET invoiceSet = 1 WHERE docNumber = ?", (doc_entry,))
        conn.commit()
        print(f"invoiceSet for docNumber {doc_entry} has been set to True.")
    except sqlite3.Error as e:
        print("Error while updating data in the database:", e)
        conn.rollback()
    finally:
        # Close the database connection
        conn.close()


# 1 - Get the next DocEntry to Send Him the message
nextDocEntry = get_first_unprocessed_document()
# 2- Create the Files For this Customer // The invoice
# But First Create His QR Code
qrFileName = q_QR.generateCustomerQRcode(nextDocEntry)
fileNamesList = e_mainsCreate.createMainsPages(34, qrFileName)
# 3 - Combine the Generated Files From the Pdf Generator into One File
finalFileName = f_merge.combineParts(fileNamesList)
# 4-  Move The Newly Created File to the Documents Folder
destination_folder = "C:/Users/BAB AL SAFA/Documents"
try:
    source_path = finalFileName
    destination_path = f"{destination_folder}/{finalFileName}"
    shutil.move(source_path, destination_path)
    print(f"Moved {finalFileName} to {destination_folder}")
except Exception as e:
    print(f"Error moving {finalFileName}: {e}")


# 5 Hide Everything On Screen
hideEveryThing()
# 6 open the Browser
openBrowser()
# 7-  Get the Phone Number To open Whataspp web
# Which Will open Whataspp Desktop For the Input Phone Number
openWhatasppLinkAndSendMSG(phoneNumber='01126517150')
# 8- Handle the Uplaoding Process To get the Invoice From the Documents Folder
# and Then Send the File
handleUPload()
# 9- Finally Mark this File as sent to Generate New Invoice For another Customer
update_invoice_set(nextDocEntry)
# TODO 
# ! DELETE the Old sqlite DB and Create new One later 
