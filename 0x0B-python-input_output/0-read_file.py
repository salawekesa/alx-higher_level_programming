#!/usr/bin/python3
"""Reads a text file and prints it to stdout"""


def read_file(filename=""):
    """prints out the text in the my_file_0.txt file"""
    with open(filename, encoding="utf-8")as UTF8:
        print(UTF8.read(),end="")
