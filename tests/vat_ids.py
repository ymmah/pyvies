VALID_VAT_IDS = {
    'AT': 'U33826303',
    'CZ': '48025551',
    'DE': '263104148',
    'DK': '13189900',
    'ES': 'B57835241',
    'FR': '39518813530',
    'FI': '18217187',
    'GB': '248233561',
    'HU': '11062361',
    'HR': '59992797221',
    # 'IS': '??????',
    'IE': '4575414W',
    'IT': '01441870449',
    'LT': '100005724315',
    'LU': '19112340',
    'NL': '817335808B02',
    'MT': '10374410',
    'PT': '504791834',
    'PL': '1231076587',
    'RO': '9919750',
    'SK': '2022293009',
    'SI': '42457157',
    'SE': '556132966401',
    'se': ' -  556-132\t 966\n401  ',
}

INVALID_VAT_IDS = [
    # garbage
    '',
    'a',
    'aa',
    'aaa',
    'ab1',
    '\t\n      ',
    '!@#$%^&*()',

    # no country code
    '298152355',
    '40103854051',
    '858556789B01',
    '10341606Y',
    '920 1205 85',
    '283358087',

    # unsupported country codes
    'AA123456789',
    'ZZ12345678',
    'xz11111111',

    # invalid/outdated vat numbers
    'CZ123456789',
    'NL018146077B01',
    'DK38699598',
    'ESB98346646',
    'DK3889013',
    'GB283320026',
    'GB279873824',
    'DE216384455',
    'IS065084',
    'AAAAAAAAAA',
    'AT33826303',
    'IT00000000',
]

