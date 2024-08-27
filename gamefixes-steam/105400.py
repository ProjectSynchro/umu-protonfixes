""" Game fix for Fable III
First launches will fail without the SupportFiles/G4W/gfwlivesetup.exe installer deleted.
The first setup process hangs indefinitely.
"""

#pylint: disable=C0103

import os
import shutil

from protonfixes import util
from protonfixes.logger import log


def main():
    # https://www.reddit.com/r/SteamDeck/comments/vuagy2/finally_got_fable_3_working/
    util.protontricks('xliveless')
