def maxDiff(num: int) -> int:
    strnum = str(num)
    x1 = '9'
    x2 = '9'
    for i in range(len(strnum)):
        if strnum[i] != '9':
            x1 = strnum[i]
            break
    y1 = '0'
    y2 = '0'
    if set(strnum) == {'1'}:
        y1 = '1'
        y2 = '1'
    elif strnum[0] == '1':
        for i in range(1, len(strnum)):
            if strnum[i] not in '01':
                y1 = strnum[i]
                y2 = '0'
                break
    else:
        y1 = strnum[0]
        y2 = '1'

    max_num = int(strnum.replace(x1, x2))
    min_num = int(strnum.replace(y1, y2))

    return max_num - min_num

