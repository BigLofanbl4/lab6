#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sentence = "или были да кабили или да"
    count = sentence.split(" ").count("или")
    print(f"Число слов или: {count}")
