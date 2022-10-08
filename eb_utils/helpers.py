#!/usr/bin/env python3
import sys
from os import system

class Colors:

    R  = "\033[1;31m"
    G  = "\033[1;32m"
    Y  = "\033[1;33m"
    BR = "\033[33m"
    B  = "\033[0;34m"
    P  = "\033[0;35m"
    LB = "\033[1;34m"
    E  = "\033[00m"

def clear():
    os = sys.platform
    if 'linux' in os:
        system('clear')
    elif 'win' in os:
        system('cls')
        
