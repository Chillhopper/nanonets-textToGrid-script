
def PC_Part_NO_List_1(number_string):
    numbers = [numbers_string[offset: offset + 12] for offset in range(0, len(numbers_string), 13)]

    numbers = []
    for offset in range(0, len(numbers_string), 13):
        numbers.append(numbers_string[offset: offset + 12])

def PC_Part_NO_List_2(number_string):

    numbers = [numbers_string[offset : offset + 12] for offset in range(0, len(numbers_string), 13)]

    someList = []
    for offset in range(0, len(numbers_string), 11):
        someList.append(numbers_string[offset : offset + 11])

    for data in someList:
        print(data)


def groupFunc(parseData):
    groupList = []
    for spacing in range(0, len(parseData), 4):
        groupList.append(parseData[spacing : spacing + 3])

    for gil in groupList:
        print(gil)

def figFunc(parseData):
    groupList = []
    for spacing in range(0, len(parseData), 4):
        groupList.append(parseData[spacing : spacing + 3])

    for gil in groupList:
        print("\'" + gil)

