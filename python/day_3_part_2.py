import aocd



def main():
    data =  aocd.get_data(year=2021, day=3).split("\n")

    oxygen = _find_oxygen(data)
    co2 = _find_co2(data)
    print(oxygen)
    print(co2)
    print(oxygen * co2)

def _find_oxygen(data, row_idx=0):
    if len(data) == 1:
        return int(data[0], 2)

    zero_rows = []
    one_rows = []

    for i, row in enumerate(data):
        if row[row_idx] == "1":
            one_rows.append(row)
        else:
            zero_rows.append(row)

    if len(zero_rows) > len(one_rows):
        return _find_oxygen(zero_rows, row_idx + 1)

    return _find_oxygen(one_rows, row_idx + 1)

def _find_co2(data, row_idx=0):
    if len(data) == 1:
        return int(data[0], 2)

    zero_rows = []
    one_rows = []

    for row in data:
        if row[row_idx] == "1":
            one_rows.append(row)
        else:
            zero_rows.append(row)

    if len(zero_rows) <= len(one_rows):
        return _find_co2(zero_rows, row_idx + 1)

    return _find_co2(one_rows, row_idx + 1)





if __name__ == '__main__':
    main()