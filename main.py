import pprint
import re
from PIL import ImageColor
from bs4 import BeautifulSoup


def split_arr(array, split_num):
    return [array.split()[i:i + split_num] for i in range(0, len(array.split()), split_num)]


def process_shorten(process_list):
    return_list = []
    for i in range(len(process_list)):
        tmp = process_list[i][1].replace('-.', '-0.').replace('-', ' -')
        tmp_text = ''
        for separate in tmp.split(' '):
            # print(separate)
            if separate == '':
                continue
            if str(separate)[0] == '.':
                separate = '0' + separate
            if '.' in str(separate):
                separate = separate.replace('.', ' 0.')
                separate = re.sub(' 0.', '.', separate, count=1)
            tmp_text += (separate + ' ')
        if process_list[i][0] == "M" or process_list[i][0] == "m":
            return_list.append([process_list[i][0], split_arr(tmp_text, 2)])

        if process_list[i][0] == "H" or process_list[i][0] == "h":
            return_list.append([process_list[i][0], split_arr(tmp_text, 1)])

        if process_list[i][0] == "V" or process_list[i][0] == "v":
            return_list.append([process_list[i][0], split_arr(tmp_text, 2)])

        if process_list[i][0] == "C" or process_list[i][0] == "c":
            return_list.append([process_list[i][0], split_arr(tmp_text, 6)])

        if process_list[i][0] == "S" or process_list[i][0] == "s":
            return_list.append([process_list[i][0], split_arr(tmp_text, 4)])

        if process_list[i][0] == "Q" or process_list[i][0] == "q":
            return_list.append([process_list[i][0], split_arr(tmp_text, 4)])

        if process_list[i][0] == "T" or process_list[i][0] == "t":
            return_list.append([process_list[i][0], split_arr(tmp_text, 2)])

        if process_list[i][0] == "A" or process_list[i][0] == "a":
            return_list.append([process_list[i][0], split_arr(tmp_text, 7)])
    return return_list


def conv_color(color_obj, already_color):
    if color_obj.has_attr('fill'):
        color = list(ImageColor.getcolor(color_obj["fill"], mode='RGB'))
    else:
        color = already_color
    return color


with open('SVG_logo.svg', mode='r') as f:
    svg_obj = f.read()

svg = BeautifulSoup(svg_obj, 'xml').find('svg')


def recursive_tags(tag_source):
    for parts in tag_source.findChildren(recursive=False):
        print("\t" * len(parts.find_parents()) + parts.name)
        # print(str(parts).replace(str(parts.extract()), ''))
        if parts.name == 'a' or parts.name == 'g':
            recursive_tags(parts)
    # print()
    # print("\n\n\n\n\n\n\n")


recursive_tags(svg)

# pprint.pprint(svg.findChildren())
# for i in range(len(paths)):
#     color = conv_color(color_obj=paths[i], already_color=color)
#     pprint.pprint(paths[i].find_parents('g').has_attr('fill'))
#     for parent in paths[i].parents:
#         pass
#         # print(parent)
#     path = ""
#     if paths[i].has_attr('d') is True:
#         path = paths[i]["d"]
#
#     paths_count = re.subn(r'[a-z]', r'', string=path, flags=re.IGNORECASE)[-1] - 1
#     print(paths_count)
#     tmp = path
#     paths_list = []
#     tmp_string = ""
#     for j in range(paths_count):
#         tmp = re.sub(r'([a-z])', r'#\1', tmp.split('#')[-1], flags=re.IGNORECASE, count=2)
#         paths_list.append([tmp.split('#')[1][0], tmp.split('#')[1][1:]])
#
#     pprint.pprint(paths_list, indent=4)
#     print("\n")
#
