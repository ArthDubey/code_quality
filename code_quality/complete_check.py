from .comments_disitribution import commentsDistributionScore
from .document_size import rateDocuments
from .redundancy_check import redundancy_check
from .function_size import functionScore


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
    functionScoreForFile = functionScore(lines)

    return {
        "Readability Score": commentsDistributionScoreForFile,
        "Document Size Score": documentSizeScoreForFile,
        "Redundancy Check Score": redundancyCheckScore,
        "Function size score": functionScoreForFile
    }
