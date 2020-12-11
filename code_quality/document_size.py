BAD_DOCUCMENT_SIZE_THRESHOLD = 40
OK_DOCUMENT_SIZE_THRESHOLD = 30
GOOD_DOCUMENT_SIZE_THRESHOLD = 20  # LINES


def rateDocuments(sizes: list) -> list:
    rating = []
    for i in range(len(sizes)):
        if sizes[i] >= BAD_DOCUCMENT_SIZE_THRESHOLD:
            rating.append(-1)
        elif sizes[i] >= OK_DOCUMENT_SIZE_THRESHOLD:
            rating.append(0)
        else:
            rating.append(1)
    return rating


def ratingToScore(rating: list) -> int:
    length, total = len(rating), sum(rating)
    upper_bound = 2*length
    score = int((total/upper_bound) * 100)
    return score


def documentSize(lines: list) -> list:
    return [len(line) for line in lines]
