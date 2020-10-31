
from model import *
import sys
from datetime import datetime
import requests

def load_cz(args):
    url = 'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/nakaza.json'
    data = requests.get(url).json()['data']

    data = map(lambda x: ActiveCases(datetime.strptime(x['datum'], '%Y-%m-%d'), x['prirustkovy_pocet_nakazenych']), data)
    return DataFile(args.source, data)

def load_sk(args):
    url = 'https://mapa.covid.chat/export/json'
    data = requests.get(url).json()

    data = map(lambda x: ActiveCases(datetime.strptime(x['date'], '%d-%m-%Y'), x['daily_cases']), data)
    return DataFile(args.source, data)

source_map = {
    'cz': load_cz,
    'sk': load_sk,
}

def load_data(args):
    global source_map

    if args.source not in source_map:
        print('Unsupported source: {}'.format(args.source))
        sys.exit(1)

    return source_map[args.source](args)

