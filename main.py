from e_mainsCreate import createMainsPages
from f_merge import combineParts

fileNamesList = createMainsPages(576)

combineParts(fileNamesList)
