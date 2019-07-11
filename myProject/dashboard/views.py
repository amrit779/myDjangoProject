from django.shortcuts import render
import openpyxl
import pandas as pd


def index(request):
    if "GET" == request.method:
        return render(request, 'index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        # getting active sheet
        worksheet = wb.active
        #print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        df = pd.DataFrame(excel_data, columns = excel_data[0])
        list1 = df['Enrolment No.']
        #return render(request, 'index.html', {"excel_data":excel_data})
        return render(request, 'index.html', {"list1":list1})
        #return render(request, df.to_html())
