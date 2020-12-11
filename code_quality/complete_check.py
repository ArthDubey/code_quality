from .comments_disitribution import commentsDistributionScore
from .document_size import rateDocuments
from .redundancy_check import redundancy_check


def completeCheck(filepath: str) -> list:
    """
    complete check for a document
    will return a dictinary of scores
    """
    with open(filepath, 'r+') as f:
        lines = f.readlines()
    commentsDistributionScoreForFile = commentsDistributionScore(lines)
    documentSizeScoreForFile = rateDocuments(lines)
    redundancyCheckScore = redundancy_check(lines)

    return {
        "Comments Distribution Score": commentsDistributionScoreForFile,
        "Document Size Score": documentSizeScoreForFile,
        "Redundancy Check Score": redundancyCheckScore
    }
