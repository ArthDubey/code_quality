BAD_FUNCTION_SIZE_THRESHOLD = 40
OK_FUNCTION_SIZE_THRESHOLD = 30
GOOD_FUNCTION_SIZE_THRESHOLD = 20  # LINES


def rateFunctions(sizes: list) -> list:
    rating = []
    for i in range(len(sizes)):
        if sizes[i] >= BAD_FUNCTION_SIZE_THRESHOLD:
            rating.append(-1)
        elif sizes[i] >= OK_FUNCTION_SIZE_THRESHOLD:
            rating.append(0)
        else:
            rating.append(1)
    return rating


def ratingToScore(rating: list) -> int:
    length, total = len(rating), sum(rating)
    upper_bound = 2*length
    score = int((total/upper_bound) * 100)
    return score


def findFunctions(lines: list) -> list:
    funs = []
    i = 0
    while i < len(lines):
        line = lines[i]
        line = line.strip()
        if line[:3] != 'def':
            i += 1
            continue
        # [index of line, index of char d in that line]
        funs.append([i, lines[i].index('d')])
        i += 1
    return funs


def functionSize(lines: list) -> list:
    functions = findFunctions(lines)
    print("Functions are:", functions)
    sizes = []
    for function in functions:
        index, charPos = function
        runner = index + 1
        while lines[runner][:charPos+1] == " "*(charPos+1):
            runner += 1
        size = runner - index - 1
        sizes.append(size)
    return sizes
