#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import collections


if __name__ == "__main__":
    print(collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir()))
