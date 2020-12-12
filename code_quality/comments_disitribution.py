from .constants import *


def isComment(lines: list, index: int) -> tuple:
    strip = lines[index].strip()
    if len(strip) == 0:
        return False, index + 1
    if strip[0] == '#':
        return True, index + 1
    if strip[:3] == '"""' or strip[:3] == "'''":
        ender = strip[:3]
        if ender in strip[3:]:
            return True, index + 1
        runner = index + 1
        while runner < len(lines) and ender not in lines[runner]:
            runner += 1
        return True, runner
    return False, index + 1


def ratioOfCommentToCode(lines: list) -> tuple:
    index = 0
    total, commentLines = len(lines), 0
    while index < total:
        isItComment, newIndex = isComment(lines, index)
        if isItComment:
            commentLines += newIndex - index
        index = newIndex
    return (commentLines, total)


def commentsDistributionScore(lines: list) -> int:
    ratio = ratioOfCommentToCode(lines)
    # Where document is empty
    if ratio[1] == 0:
        return 100
    distributionScore = ratio[0] / ratio[1]
    # Configurable by tweaking the constants
    goodRatioCoefficient = GOOD_RATIO_OF_COMMENT_TO_CODE[1] / \
        GOOD_RATIO_OF_COMMENT_TO_CODE[0]
    score = min(distributionScore * goodRatioCoefficient, 1.0)
    return score * 100
