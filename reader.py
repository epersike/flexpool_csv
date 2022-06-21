import csv
from datetime import datetime

MONTH = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
}

def read_file(filename):
    ret = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(spamreader):
            if i == 0: continue # ignora linha de cabeçalho [ 'Date', 'Value ETH', 'Value USD' ]
            ret.append(_parse_row(row))
    return ret

def _parse_row(row):
    
    return {
        'date' : _parse_datetime(row[0]),
        'eth_value': row[1],
        'usd_value': row[2]
    }


def _parse_datetime(datestr):

    try:
        dict_aux = {
            'year': int(datestr[-4:]),
            'month': MONTH.get(datestr[4:7]),
            'day': int(datestr[8:10]),
        }
        ret = datetime(**dict_aux)
    except:
        print("Erro ao converter data: {}".format(datestr))
        raise

    return ret

if __name__ == '__main__':
    from pprint import pprint
    pprint(read_file('rewards.csv'))