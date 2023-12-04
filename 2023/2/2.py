import re

def part_1(file):
    pattern = r'(\d+)\s(\w+)'
    allowedColor = {
        'red': 12,
        'blue': 14,
        'green': 13
    }
    gameID = 1
    maxCubes = 12 + 13 + 14
    sum = 0
    with open(file) as f:
        for line in f:
            maxColor = {
                'red': 0,
                'blue': 0,
                'green': 0
            }
            line.strip()
            matches = re.findall(pattern, line)
            for match in matches:
                if match[1] == 'red':
                    if maxColor['red'] < int(match[0]):
                        maxColor['red'] = int(match[0])
                elif match[1] == 'blue':
                    if maxColor['blue'] < int(match[0]):
                        maxColor['blue'] = int(match[0])
                elif match[1] == 'green':
                    if maxColor['green'] < int(match[0]):
                        maxColor['green'] = int(match[0])
                else:
                    print("Not a allowed color!")
                    return 0
            allCubes = maxColor['red'] + maxColor['blue'] + maxColor['green']
            if maxColor['red'] > allowedColor['red']:
                gameID += 1
                print(f"Game {gameID} ist ungültig! (red)")
                continue
            elif maxColor['blue'] > allowedColor['blue']:
                gameID += 1
                print(f"Game {gameID} ist ungültig! (blue)")
                continue
            elif maxColor['green'] > allowedColor['green']:
                gameID += 1
                print(f"Game {gameID} ist ungültig! (green)")
                continue
            elif allCubes > maxCubes:
                gameID += 1
                print(f"Game {gameID} ist ungültig! (all)")
                continue
            else:
                print(maxColor)
                sum += gameID
                gameID += 1
    print(sum)


def part_2(file):
    pattern = r'(\d+)\s(\w+)'
    gameID = 1
    sum = 0
    with open(file) as f:
        for line in f:
            minColor = {
                'red': 0,
                'blue': 0,
                'green': 0
            }
            line.strip()
            matches = re.findall(pattern, line)
            for match in matches:
                if match[1] == 'red':
                    if minColor['red'] < int(match[0]):
                        minColor['red'] = int(match[0])
                elif match[1] == 'blue':
                    if minColor['blue'] < int(match[0]):
                        minColor['blue'] = int(match[0])
                elif match[1] == 'green':
                    if minColor['green'] < int(match[0]):
                        minColor['green'] = int(match[0])
                else:
                    print("Not a allowed color!")
                    return 0
            sum += minColor['red'] * minColor['blue'] * minColor['green']
    print(sum)

# part_1("2/inputFile.txt")
part_2("2/inputFile.txt")
            
