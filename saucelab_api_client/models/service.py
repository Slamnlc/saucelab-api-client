import base64
import random
import sys
from datetime import datetime
from threading import Event
from time import sleep


def compare_version(version: str, new_version: str) -> str:
    version_split = version.split('.')
    new_version_split = new_version.split('.')
    for index, sub_version in enumerate(version_split):
        if index >= len(new_version_split):
            return 'more'
        elif index + 1 == len(version_split) and index + 2 <= len(new_version_split):
            return 'less'
        elif int(sub_version) > int(new_version_split[index]):
            return 'more'
        elif int(sub_version) < int(new_version_split[index]):
            return 'less'
    return 'draw'


def validate_dict(dict_to_check: dict, example: (tuple, list), soft_check: bool = False) -> bool:
    error_message = []
    for key in dict_to_check:
        if key not in example:
            error_message.append(f'Unavailable key "{key}". Must be one of {example.keys()}')
    if not soft_check:
        for key in example:
            if key not in dict_to_check:
                error_message.append(f'Missing requirements key "{key}". Requirements keys {dict_to_check.keys()}')
        if len(error_message) != 0:
            raise KeyError('\n'.join(error_message))
    else:
        if len(error_message) != 0:
            raise KeyError('\n'.join(error_message))
    return True


class Auth:
    def __init__(self, username, password):
        self.data = base64.b64encode(b':'.join((username.encode('ascii'),
                                                password.encode('ascii')))).strip().decode('ascii')

    def __call__(self, r):
        r.headers['Authorization'] = f'Basic {self.data}'
        return r

    def __del__(self):
        return 'BasicAuth'


def print_progress(event: Event, progress_type: str):
    start, work, end = {
        'download': ('Start download file', 'Download time', 'Download finished'),
        'upload': ('Start upload file', 'Upload time', 'Upload finished')
    }[progress_type]
    main_icon, meet = '🐱', ('🙈', '🙉', '🙊')
    enemy = ['🐲', '🐶', '🐭', '🐝', '🦄', '🐕', '🐳', '🦑', '🦂', '🐺', '🐼', '🐸']
    row = ['.' for _ in range(15)]
    row[1] = main_icon
    start_time = datetime.now()
    print(start)
    symbols, index = ('/', '|', '\\', '|'), 0
    while True:
        if row[1] != main_icon:
            row[1] = main_icon
        for position, value in enumerate(row):
            if value in enemy:
                if row[position - 1] == main_icon:
                    row[position - 1] = random.choice(meet)
                    row[position] = '.'
                else:
                    row[position - 1] = value
                    row[position] = '.'
        if random.randint(0, 7) == 5:
            row[-1] = random.choice(enemy)
        main_row = ''.join(row)
        txt = f'\r{work} {str(datetime.now() - start_time).split(".", maxsplit=1)[0]}...{symbols[index]}'
        sys.stdout.write(f'{txt} {main_row}')
        sys.stdout.flush()
        index += 1
        if index >= len(symbols):
            index = 0
        sleep(.3)
        if event.is_set():
            print(f'\n{end}', )
            break
