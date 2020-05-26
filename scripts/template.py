#!/usr/bin/env python3
""" Returns with exitcode 1 if /....., otherwise 0 (success)
"""

import os, sys, traceback

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def sprint(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)


def show_usage():
    eprint("Usage: " + os.path.basename(__file__) + " <option>")
    eprint("   description of the script operations")


def main():
    if len(sys.argv) != 1:
        eprint("error: invalid argument(s)\n")
        show_usage()
        return 1

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc(file=sys.stdout)

    show_usage()
    sys.exit(1)
