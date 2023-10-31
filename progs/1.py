#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sentence = input("Enter sentente: ")
    index = 0
    while index < len(sentence):
        print(sentence[index])
        if index + 1 < len(sentence):
            print(sentence[index + 1])
        index += 4
