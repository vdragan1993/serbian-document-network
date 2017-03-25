# coding=utf-8
__author__ = "Dragan Vidakovic"
import codecs


def read_file_content(path):
    """
    Read file from given path
    :param path: file path
    :return: file content
    """
    f = codecs.open(path, 'r', 'utf-8')
    content = f.read()
    f.close()
    return content


def read_file_line(path):
    """
    Read all lines from file
    :param path: file path
    :return: list of lines
    """
    f = codecs.open(path, 'r', 'utf-8')
    lines = f.readlines()
    f.close()
    return lines
