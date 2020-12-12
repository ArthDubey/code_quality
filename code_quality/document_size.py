from .constants import *


def rateDocuments(lines: list) -> int:
    '''
    We'll scale 100-500 range in 100 points and invert
    to get the score
    '''
    size = len(lines)
    if size <= 20:
        return size*4
    if size < 100:
        return 100
    size -= GOOD_DOCUMENT_SIZE_THRESHOLD
    size //= BAD_DOCUCMENT_SIZE_THRESHOLD / GOOD_DOCUMENT_SIZE_THRESHOLD
    return 100 - min(size, 100)


# def rateDocuments(sizes: list) -> list:
#     rating = []
#     for i in range(len(sizes)):
#         if sizes[i] >= BAD_DOCUCMENT_SIZE_THRESHOLD:
#             rating.append(-1)
#         elif sizes[i] >= OK_DOCUMENT_SIZE_THRESHOLD:
#             rating.append(0)
#         else:
#             rating.append(1)
#     return rating


# def ratingToScore(rating: list) -> int:
#     length, total = len(rating), sum(rating)
#     upper_bound = 2*length
#     score = int((total/upper_bound) * 100)
#     return score


# def documentSize(lines: list) -> list:
#     return [len(line) for line in lines]


# def documentSizeScore(lines: list) -> list:
#     sizes = documentSize(lines)
#     ratings = rateDocuments(sizes)
#     score = ratingToScore(ratings)
#     return score
