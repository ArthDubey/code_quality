from collections import Counter


def linesToCounter(lines: list) -> list:
    lines = [line.strip() for line in lines]
    return Counter(lines)


def counterToDistribution(cnt: Counter) -> list:
    dist = list(cnt.values())
    dist.sort()
    return dist


def distributionRating(dist: list) -> int:
    # empty document
    if not dist:
        return 100
    unique, total = len(dist), sum(dist)
    return (unique/total) * 100


def redundancy_check(lines: list) -> int:
    cnt = linesToCounter(lines)
    dist = counterToDistribution(cnt)
    score = distributionRating(dist)
    return score
