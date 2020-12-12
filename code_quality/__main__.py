from .directory_score_aggr import aggregateScore
import os
import argparse


parser = argparse.ArgumentParser(
    description="""
                    A light-weight library for testing code quality. Includes various software principles check.
                """
)

DEFAULT_DIR = os.path.dirname(os.path.abspath(__file__))

parser.add_argument("-d", "--Directory",
                    help="The filepath for repository or the file to execute checks on.", type=str, default=DEFAULT_DIR)

args = parser.parse_args()

aggregateScore(args.Directory)
