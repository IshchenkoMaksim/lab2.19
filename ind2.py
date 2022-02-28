#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import pathlib
import colorama
import os
from colorama import Fore
import magic


def tree(directory):
    print(Fore.RED + f'> {directory}')
    for path1 in sorted(directory.rglob('*')):
        depth = len(path1.relative_to(directory).parts)
        spacer = '  ' * depth
        if os.path.isdir(path1):
            print(Fore.RED + f'{spacer} > {path1.name}')
        else:
            file = str(path1)
            type_file = magic.from_file(file, mime=True)
            if (type_file.split('/')[0]) == "audio":
                print(Fore.BLUE + f'{spacer} < {path1.name}')
            elif (type_file.split('/')[0]) == "video":
                print(Fore.CYAN + f'{spacer} < {path1.name}')
            elif (type_file.split('/')[0]) == "image":
                print(Fore.GREEN + f'{spacer} < {path1.name}')
            elif (type_file.split('/')[0]) == "text":
                print(Fore.YELLOW + f'{spacer} < {path1.name}')
            elif (type_file.split('/')[0]) == "application":
                print(Fore.MAGENTA + f'{spacer} < {path1.name}')
            else:
                print(Fore.BLACK + f'{spacer} < {path1.name}')


def tree_find(directory, suffix_select):
    root = str(directory)
    answer = []
    spacer = "  "

    for current, directories, files in os.walk(root):
        for f in files:
            if f.endswith(suffix_select):
                d = current
                if d not in answer:
                    answer.append(d)
                    print(Fore.RED + f'> {d}')
                print(Fore.BLUE + f'{spacer} < {f}')


def main(command_line=None):

    colorama.init()
    current = pathlib.Path.cwd()

    file_parser = argparse.ArgumentParser(add_help=False)

    parser = argparse.ArgumentParser("tree")
    parser.add_argument(
        "--version",
        action="version",
        help="The main parser",
        version="%(prog)s 1.0"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Субпарсер для выбора пути
    select_dir = subparsers.add_parser(
        "select",
        parents=[file_parser]
    )
    select_dir.add_argument(
        "path",
        action="store"
    )

    # Субпарсер для поиска файлов
    find_file = subparsers.add_parser(
        "find",
        parents=[file_parser]
    )
    find_file.add_argument(
        "suffix",
        action="store"
    )
    find_file.add_argument(
        "path",
        nargs='?',
        default=current,
    )

    args = parser.parse_args(command_line)

    if args.command == 'select':
        directory = pathlib.Path(args.path)
        if directory.exists():
            tree(directory)
        else:
            print(Fore.RED + "Путь не существует", file=sys.stderr)
            exit(1)
    elif args.command == 'find':
        suffix = args.suffix
        directory = pathlib.Path(args.path)
        tree_find(directory, suffix)
    else:
        tree(current)


if __name__ == "__main__":
    main()
