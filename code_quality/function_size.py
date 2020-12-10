GOOD_FUNCTION_SIZE = 25  # LINES


def findFunctions(lines: list) -> list:
    funs = []
    i = 0
    while i < len(lines):
        line = lines[i]
        line.strip()
        if line[:3] != 'def':
            i += 1
            continue
        # [index of line, index of char d in that line]
        funs.append([i, lines[i].index('d')])
        i += 1
    return funs


def functionSize(lines: list) -> int:
    functions = findFunctions(lines)
    sizes = []
    for function in functions:
        index, charPos = function
        runner = index + 1
        while lines[runner][:charPos+1] == " "*(charPos+1):
            runner += 1
        size = runner - index
        sizes.append(size)
    return sizes
