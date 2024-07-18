import argparse
import logging


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument( '--start', type=int)
    parser.add_argument('--end', type=int)
    parser.add_argument('--verbose', action='store_true')
    return parser

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    start: int = args.start
    end: int = args.end
    verbose: bool = args.verbose

    print(start, end, verbose)

