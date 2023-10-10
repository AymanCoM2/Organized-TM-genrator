from PartOne import e_mainsCreate, f_merge
# from PartOne.e_mainsCreate import createMainsPages
# from PartOne.f_merge import combineParts

fileNamesList = e_mainsCreate.createMainsPages(576)
# 4 pages Nearly
# fileNamesList = e_mainsCreate.createMainsPages(5)
# 1 Page

finalFileName = f_merge.combineParts(fileNamesList)
print("finalFileName")
print(finalFileName)
# What after the Combinations ?
# First there are Some Changes
# For example the Quantitng in the Invoice is Not a Decimal Number and
# Some Prices Need the Two Decimal Number after the point
# Second Thing Make The Following :
# ---------------------------------------------
