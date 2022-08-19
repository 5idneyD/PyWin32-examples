import win32com.client as win32

# Initiates xl application
xl = win32.gencache.EnsureDispatch("Excel.Application")
# Creates new workbook
book = xl.Books.New()
# Select which sheet to edit
sheets = book.Worksheets("Sheet1")

# Assigns values to cells
sheet.Range("A1").Value = 3
sheet.Range("B1").Value = 2

# Shows the sum of the first 2 cells
# Result is 5
sheet.Range("C1").Formula = "=sum(A1:B1)"

book.Save("Test.xlsx")
book.Close()
