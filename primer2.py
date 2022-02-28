#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib


def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = ' ' * depth
        print(f'{spacer}+ {path.name}')


if __name__ == "__main__":
    tree(pathlib.Path.cwd())
