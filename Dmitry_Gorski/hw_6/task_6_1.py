from luna.Luna import luhn as validate


def check_convert_input(ingest: str) -> (int, str):
    if ingest.isdigit() and len(ingest) != 0:
        return ''.join(map(str, ingest))
    return 'Incorrect input'


if __name__ == "__main__":
    some_number = input('Input some number: ')
    if validate(check_convert_input(some_number)):
        print('Valid')
    else:
        print('Invalid')
