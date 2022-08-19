import win32com.client as win32

xl = win32.gencache.EnsureDispatch("Excel.Application")
book = xl.Books.New()
