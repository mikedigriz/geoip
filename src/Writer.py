import csv


def csv_writer(ip: str, country: str) -> None:
    '''
    Create if not exist and append file with data.
    If you use LibreOffice change encoding to Windows-1251.
    '''
    with open('./ip_by_country.csv', 'a', encoding='Windows-1251',  newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([ip, country])
