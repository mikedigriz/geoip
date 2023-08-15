from src import GeoLite, Writer


ip_file = './assets/http.txt'


def read_file(ip_file: str = ip_file) -> None:
    '''Open file http.txt, cleanup and call func get_country_name_by_ip()'''
    try:
        with open(ip_file, 'r', newline='') as ip_list:
            for ip in ip_list:
                ip_sanitized = ip.strip().split(':')[0]
                country = GeoLite.get_country_name(ip_sanitized)
                Writer.csv_writer(ip.strip(), country)
                print(ip_sanitized, country)
    except KeyboardInterrupt:
        print('\nForce Interrupt!')