import re

def part_1(file):
    sum = 0
    with open(file) as f:
        for line in f:
            match_f = re.search(r'\d', line).group()
            flip = line[::-1]
            match_l = re.search(r'\d', flip).group()
            num = int(match_f) * 10 + int(match_l)
            sum += num
        return sum

def part_2(file):
    help_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    help_dict_flip = {
        'eno': '1',
        'owt': '2',
        'eerht': '3',
        'ruof': '4',
        'evif': '5',
        'xis': '6',
        'neves': '7',
        'thgie': '8',
        'enin': '9',
    }
    sum = 0
    operations = 0
    with open(file) as f:
        for line in f:
            res = []
            res = {}
            match_f = re.search(r'\d', line)
            res[match_f.start()] = match_f.group()
            for ele in help_dict:
                match = re.search(ele, line, re.IGNORECASE)
                if match:
                    res[match.start()] = help_dict[match.group()]
            sortedList = list(res.keys())
            sortedList.sort()
            sortedDict = {i: res[i] for i in sortedList}
            sortedList = list(sortedDict.values())
            if sortedList:
                first = sortedList[0]

            fliped = line[::-1]
            res_flip = []
            res_flip = {}
            match_l = re.search(r'\d', fliped)
            res_flip[match_l.start()] = match_l.group()
            for ele in help_dict_flip:
                match_fliped = re.search(ele, fliped, re.IGNORECASE)
                if match_fliped:
                    res_flip[match_fliped.start()] = help_dict_flip[match_fliped.group()]
            sortedList_fliped = list(res_flip.keys())
            sortedList_fliped.sort()
            sortedDict_fliped = {i: res_flip[i] for i in sortedList_fliped}
            sortedList_fliped = list(sortedDict_fliped.values())
            if sortedList_fliped:
                last = sortedList_fliped[0]

            sum += int(first) * 10 + int(last)
            print("")
            print(line, int(first) * 10 + int(last), fliped)
        return sum

# print(part_1("1/inputFile"))
print(part_2("1/inputFile"))
