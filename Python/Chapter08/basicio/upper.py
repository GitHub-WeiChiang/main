__author__ = "ChiangWei"
__date__ = "2022/05/04"

import sys

src_path = sys.argv[1]
dest_path = sys.argv[2]

with open(src_path) as src, open(dest_path, 'w') as dest:
    content = src.read()
    dest.write(content.upper())
