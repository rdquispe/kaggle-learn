ILLEGAL_SYMBOLS = [
    "    _  _  _  _  _           _  _  _  _     _  _  _                 _  _  _     _  _  _  _  _     _  _  _     _  _ ",
    "| ||  | || || |  |  |    _| _   | _| _| _|  | _| _  _|| ||_ |_||_ |  |_ |_ |_  _ |_ |_   |   |_| _||_||_||_||_||_|",
    "|_||_||_ | | _||_|     ||_ |_ |_  _ |   _| _|  | _|  |  |  |    _| _| _   ||_||_||_ | |     ||_||_|| ||_  _|  | _ ",
    "000001002003004005006007008009010011012013014015016017018019020021022023024025026027028029030031032033034035036037"
]

CELL_VALUES = {
    ' _ | ||_|': '0',
    '     |  |': '1',
    ' _  _||_ ': '2',
    ' _  _| _|': '3',
    '   |_|  |': '4',
    ' _ |_  _|': '5',
    ' _ |_ |_|': '6',
    ' _   |  |': '7',
    ' _ |_||_|': '8',
    ' _ |_| _|': '9'
}

READ = 'r'

ALTERNATIVES = {
    '0': ['8'],
    '1': ['7'],
    '2': [],
    '3': ['9'],
    '4': [],
    '5': ['6', '9'],
    '6': ['5', '8'],
    '7': ['1'],
    '8': ['0', '6', '9'],
    '9': ['5', '8']
}

POSIBLE_DIGIT = {
    "000": ['0'],
    "001": ['0', '6'],
    "002": ['0'],
    "003": ['0'],
    "004": ['0', '9'],
    "005": ['0'],
    "006": ['1'],
    "007": ['1'],
    "008": ['2'],
    "009": ['2'],
    "010": ['2'],
    "011": ['2', '3'],
    "012": ['2'],
    "013": ['3'],
    "014": ['3'],
    "015": ['3'],
    "016": ['3', '5'],
    "017": ['4', '1'],
    "018": ['4', '1'],
    "019": ['4'],
    "020": ['4'],
    "021": ['5'],
    "022": ['5'],
    "023": ['5'],
    "024": ['5'],
    "025": ['6'],
    "026": ['6'],
    "027": ['6'],
    "028": ['6'],
    "029": ['7'],
    "030": ['7'],
    "031": ['8'],
    "032": ['8', '2', '3'],
    "033": ['8'],
    "034": ['8', '2'],
    "035": ['9', '4'],
    "036": ['9', '4'],
    "037": ['9']
}