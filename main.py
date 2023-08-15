'''
Parse ip address, return csv-file with IP, Country.
Change ip_file = 'your_file.txt'
'''
from src import Reader


ip_file = './assets/http.txt'


if __name__ == "__main__":
    Reader.read_file(ip_file)