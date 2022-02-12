import pprint
import re

from bs4 import BeautifulSoup

with open('./svg.svg', mode='r') as f:
    svg = f.read()

paths = BeautifulSoup(svg, 'xml').find_all('path')

for i in range(len(paths)):
    color = 0x000000
    if paths[i].has_attr('fill') is True:
        color = paths[i]["fill"][1:]
    print(hex(int(str(color), 16)))

    path = ""
    if paths[i].has_attr('d') is True:
        path = paths[i]["d"]

    paths_count = re.subn(r'[a-z]', r'', string=path, flags=re.IGNORECASE)[-1] - 1
    print(paths_count)
    tmp = path
    paths_list = []
    tmp_string = ""
    for j in range(paths_count):
        tmp = re.sub(r'([a-z])', r'#\1', tmp.split('#')[-1], flags=re.IGNORECASE, count=2)
        paths_list.append([tmp.split('#')[1][0], tmp.split('#')[1][1:]])

    pprint.pprint(paths_list, indent=4)
    print("\n")
