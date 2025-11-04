#!/usr/bin/env python

"""
The Main module that starts the Game Class
"""
import sys
from classes.game import Game
from classes.terminal_ui import TerminalUI

MIN_MAJOR = 3
MIN_MINOR = 12


# Based on original 1978 version of Oregon Trail:
#  from https://github.com/clintmoyer/oregon-trail/tree/master/refactor
# shown in BASIC
# PROGRAM NAME - OREGON        VERSION:01/01/78
# ORIGINAL PROGRAMMING BY BILL HEINEMANN - 1971
# SUPPORT RESEARCH AND MATERIALS BY DON RAWITSCH,
# MINNESOTA EDUCATIONAL COMPUTING CONSORTIUM STAFF
# CDC CYBER 70/73-26     BASIC 3.1
# DOCUMENTATION BOOKLET 'OREGON' AVAILABLE FROM
#     MECC SUPPORT SERVICES
#     2520 BROADWAY DRIVE
#     ST. PAUL, MN  55113


def display_version_error(major: int, minor: int) -> None:
    print(
        f"This script requires Python {MIN_MAJOR}.{MIN_MINOR} or higher."
        f"\nYou are running python {major}.{minor}."
    )


def exit_if_python_is_too_old() -> None:
    """Exits early if python is not newer than minimum version.  Dataclasses were added
    in Python 3.7 though this only supports versions newer than 3.12"""
    major, minor = sys.version_info.major, sys.version_info.minor
    if major < MIN_MAJOR or (major == MIN_MAJOR and minor < MIN_MINOR):
        display_version_error(major, minor)
        sys.stdout.flush()
        sys.exit()


def main() -> None:
    """ Main Function that starts the Game class """
    terminal_ui = TerminalUI()
    g = Game(ui=terminal_ui)
    g.introduction()

    while g.miles < g.MAX_MILES:
        if not g.handle_turn():
            g.handle_death()
            sys.exit(0)
        g.current_turn += 1
    g.conclusion()


if __name__ == "__main__":
    exit_if_python_is_too_old()
    main()
