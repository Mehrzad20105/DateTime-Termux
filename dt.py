#!/data/data/com.termux/files/usr/bin/env python

import time
from arrow import *
import os

def main():
    while (True):
        try:
            os.system("clear")
            week = ("SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI")

            print("    DateTime — @Mehrzad20105\n\t    Press <CTRL>+C for QUIT.")
            print("----------------------------------------")

            t = Arrow.now().format("HH:mm:ss")
            print("\t\t\033[1m\033[92m{}\033[0m".format(t))

            wd = week[Arrow.now().weekday()]

            d = Arrow.now().format("MMMM(MM) DD, YYYY")
            print("\t\033[93m{} - \033[3m{}\033[0m".format(d, wd))

            print()

            print("\033[37m\033[4m\033[1m<<Thank you for Download this script!>> \033[0m")

            time.sleep(0.9)
            os.system("clear")

        except KeyboardInterrupt:
            os.system("clear")
            quit()

main()
