
def consistentPadding(msg: str) -> str:
    length = len(msg)
    if length % 2 == 0:
        raise Exception("Please send only odd length msgs for padding.")
    padding = "=" * (77 - (length//2))
    return padding + " " + msg + " " + padding
