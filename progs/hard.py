#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sentence = input("Enter sentence: ").split()
    sentence[0], sentence[-1] = sentence[-1], sentence[0]
    print(f'Result: {" ".join(sentence)}')
