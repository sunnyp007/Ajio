import xlrd
from Library.config import Config
path = r"D:\Sunny Patil\Capgemini Training\Ajio Project\file_data.xlsx"
prod_search = "Shirt"
mob_num = "7066962805"


def read_locators():
    workbook=xlrd.open_workbook(Config.data_path)              #open xlxs file
    worksheet=workbook.sheet_by_name("ProdDetails")    #sheet name
    rows=worksheet.get_rows()        #read the data and return a generator object
    print(rows)
    header = next(rows)
    d={}
    for row in rows:
        d[row[0].value]=(row[1].value,row[2].value)
    return d


print(read_locators())