import json, csv
from pprint import pprint

def open_csv(filename, rows, dialect='excel'):
    '''
    :param: `filename` :str:
    :param: `rows`:int:
    :param: `dialect`: default to 'excel' :str:
    :yields: OrderedDict
            from csv.DictReader
    '''
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, dialect=dialect)
        for count in range(rows):
            # process 2 lines each time
            for i in range(1):
                yield next(reader)


def get_csv_rows(filename, row_count):
    '''
    :param: filename: str
    :param: row_count: int
    :return: list
            dicts in a list
    '''
    # there's no need to convert to dict when using python 3.8+: return list(get_csv_rows(...))
    csv_rows = [dict(d) for d in list(open_csv(filename, row_count))]
    return csv_rows


if __name__ == '__main__':
    data = get_csv_rows('credit_loan_dataset.csv', 20)
    pprint(data)