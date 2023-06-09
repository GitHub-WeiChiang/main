__author__ = "ChiangWei"
__date__ = "2022/05/03"

import sys
from contextlib import contextmanager
from typing import Iterator, IO

@contextmanager
def file_reader(filename) -> Iterator[IO]:
    try:
        f = open(filename, 'r')
        yield f
    finally:
        f.close()

with file_reader(sys.argv[1]) as f:
    for line in f:
        print(line, end='')
