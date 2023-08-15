import maxminddb


def get_country_name(ip_sanitized: str) -> str:
    '''Accepts an ip address and check it with GeoLite2-Country db'''
    try:
        with maxminddb.open_database('./assets/GeoLite2-Country.mmdb') as db_reader:
            country = db_reader.get(ip_sanitized)
            return country['country']['names']['ru']
    except ValueError:
        return ''
    except TypeError:
        return ''
