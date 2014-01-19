# -*- coding: utf-8 -*-
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('../src')

import Tokenizer as tk


def main():
    a = "這邊介紹一個叫做get的method，只適用於dictionary"
    tk.tokenize(a)

if __name__ == '__main__':
    main()
