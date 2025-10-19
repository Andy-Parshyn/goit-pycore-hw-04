from colorama import Fore
from pathlib import Path
import sys


def path_validator(argv:list[str]) -> Path:         
    path_string = ' '.join(argv[1:]).strip()
    path = Path(path_string).resolve()

    return path


def dir_tree(path: Path, prefix= ''):
    files = list(path.iterdir())
    
    for index, el in enumerate(files):
        is_last_element = index == len(files) - 1
        connector = '└──' if is_last_element else '├──'
        element_name = f'{Fore.GREEN}{el.name}{Fore.RESET}' if el.is_dir() else f'{Fore.BLUE}{el.name}{Fore.RESET}'
        print(prefix + connector + element_name)

        if el.is_dir():
            extension = '    ' if is_last_element else '|   '
            dir_tree(el,prefix + extension)


def main():
    if len(sys.argv) < 2:
        print(f'{Fore.RED} No path found in the input!!')

    else:
        try:
            dir_tree(path_validator(sys.argv))
        except FileNotFoundError: 
            print(f'{Fore.RED}Directory does not exists, please check your input.')


if __name__ == '__main__':
    main()


