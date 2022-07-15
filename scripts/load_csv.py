import csv
from myapp.models import BankDetail

def run():
    fdata=open('myapp/bank_branches.csv')
    read=csv.reader(fdata)
    BankDetail.objects.all().delete()

    for row in read:
        print(row)
        b,created= BankDetail.objects.get_or_create(ifsc=row[0],bank_id=row[1],branch=row[2],address=row[3],city=row[4],district=row[5],state=row[6],bank_name=row[7])
    b.save()
