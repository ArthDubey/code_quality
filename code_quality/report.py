from termcolor import colored
from .consistent_padding_line import consistentPadding
from .advices import advices

scoreToColorMap = {
    0: 'red',
    1: 'yellow',
    2: 'green',
    3: 'green'
}


def printScore(key: str, val: int) -> None:
    color = scoreToColorMap[val//33]
    print(colored(
        key +
        "\t"*3 +
        "{:.2f}".format(val) + " / 100",
        color
    ))
    return


def summaryFromScore(score: dict) -> bool:
    padding = "=" * 70
    print(
        consistentPadding("Summary")
    )
    lackingParts = []
    for key in score.keys():
        printScore(key, score[key])
        if score[key] < 66.66:
            lackingParts.append(key)
    reportAdvices(lackingParts)
    return True


def reportAdvices(lackingParts: list) -> None:
    print(consistentPadding("Possible Resolution"))
    print()
    for lackingPart in lackingParts:
        print(
            "-->",
            colored(advices[lackingPart], 'cyan')
        )
    print()
    print(
        colored(
            consistentPadding("Check completed"),
            'green'
        )
    )
    return None
