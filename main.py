'''
Parse ip address, return csv-file with IP, Country.

I'm use it for visualize site geo-data.
Ex:
echo "select ip from tablename;"| mysql -u db_username -pPa$$word db_name > ./assets/http.txt
'''

#TODO Прикрутить Sqlite, Прикрутить TG-бот

from src import Reader


ip_file = './assets/http.txt'


if __name__ == "__main__":
    Reader.read_file(ip_file)