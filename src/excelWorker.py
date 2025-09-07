# read a CSV file
# after reading CSV add data validation (list dropdowns), auto population of columns using formulas or vlookup
# have the script lock all cells of excel except for two columns
# finally save the file as excel
# https://realpython.com/openpyxl-excel-spreadsheets-python/
# https://openpyxl.readthedocs.io/en/stable/
# https://openpyxl.pages.heptapod.net/openpyxl/index.html
# import pandas as pd
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
import csv 

# df = pd.read_csv('data.csv')
# print(df)
# df.to_excel('output.xlsx', index=False)

class PlanShell:
    def __init__(self, name: str, pkg: str, pmtid: int, varn: int) -> None:
        self.name = name
        self.pkg = pkg
        self.pmtid = pmtid
        self.varn = varn
        pass

    def __str__(self) -> str:
        return f'{self.name}, {self.pkg}, {self.pmtid}, {self.varn}'

plan_list = [
    PlanShell("PPO plan in PPC no cap", '10', 2, 3),
    PlanShell("PPO plan in AltNet no cap", '11', 5, 6),
    PlanShell("PPO plan in Trad no cap", '12', 8, 9),
    PlanShell("HMO plan in PPC with cap", '13', 2, 3),
    PlanShell("HMO plan in AltNet with cap", '14', 2, 3),
]

class Region:
    def __init__(self, region_cd: str, region_nm: str) -> None:
        self.region_cd = region_cd
        self.region_nm = region_nm

    def __str__(self) -> str:
        return f'{self.region_cd}, {self.region_nm}'
    

region_list = [
    Region('A', 'Region A'),
    Region('B', 'Region B'),
    Region('C', 'Region C'),
    Region('D', 'Region D'),
    Region('E', 'Region E'),
    Region('F', 'Region F'),
    Region('G', 'Region G'),
    Region('H', 'Region H'),
    Region('I', 'Region I'),
    Region('J', 'Region J'),
]

def readCSV(filename: str, sheet) -> None:
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            sheet.append(row)
    pass

def addLookupSheet(workbook) -> None:
    sheet = workbook.create_sheet('Lookup')
    
    # header row
    sheet['A1'] = 'Plan Name'
    sheet['B1'] = 'Package ID'
    sheet['C1'] = 'PMT ID'
    sheet['D1'] = 'Variation'
    # table data
    for i in range(len(plan_list)):
        sheet[f'A{i+2}'] = plan_list[i].name
        sheet[f'B{i+2}'] = plan_list[i].pkg
        sheet[f'C{i+2}'] = plan_list[i].pmtid
        sheet[f'D{i+2}'] = plan_list[i].varn

    sheet['F1'] = 'Region Code'
    sheet['G1'] = 'Region Name'
    for i in range(len(region_list)):
        sheet[f'F{i+2}'] = region_list[i].region_cd
        sheet[f'G{i+2}'] = region_list[i].region_nm
    
    pass

def addPlanListValidation(sheet) -> None:
    dv = DataValidation(type="list", formula1='"PPO plan in PPC no cap", "PPO plan in AltNet no cap", "PPO plan in Trad no cap", "HMO plan in PPC with cap", "HMO plan in AltNet with cap"', allow_blank=True)
    dv.error ='Your entry is not in the list'
    dv.errorTitle = 'Invalid entry'
    dv.errorType = 'warning'
    dv.prompt = 'Please select from the list'
    dv.promptTitle = 'List Selection'
    dv.showErrorMessage = True
    dv.showInputMessage = True

    # attach data validation first to the sheet
    sheet.add_data_validation(dv)

    # attach data validation to entire column
    # dv.add(worksheet=sheet, col=4)
    dv.add('D1:D1048576')
    pass

def addPckIDFormula(column) -> None:
    column[1] = "=B1"
    pass

def addPmtIDFormula(column) -> None:
    column[2] = "=B1"
    pass

def addGLFormula(column) -> None:
    column[3] = "=B1"
    pass

def protectSheet(sheet) -> None:
    sheet.security.lockStructure = True
    sheet.protection.delete = True
    sheet.protection.sheet = True
    # sheet.protection.password = 'password'
    sheet.protection.enable()
    pass


def writeExcel(workbook, filename: str) -> None:
    workbook.save(filename)  ## this will save, overwrite the workbook
    pass

def main():
    workbook = openpyxl.Workbook()
    
    sheet = workbook.active
    sheet.title = 'Data'
    readCSV('data.csv', sheet)
    addLookupSheet(workbook)

    # addPlanListValidation(sheet.columns.column(1))
    addPlanListValidation(sheet)
    # addPckIDFormula(sheet.columns.column(2))
    # addPmtIDFormula(sheet.columns.column(3))
    # addGLFormula(sheet.columns.column(4))

    # unlockPlanRegion(sheet)

    # protectSheet(sheet)
    writeExcel(workbook, 'output.xlsx')
    pass

if __name__ == '__main__':
    main()