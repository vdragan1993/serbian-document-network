# coding=utf-8
__author__ = "Dragan Vidakovic"

import re

stop = {'biti', 'jesam', 'budem', 'sam', 'jesi', 'budes', 'si', 'jesmo', 'budemo', 'smo', 'jeste', 'budete', 'ste',
        'jesu', 'budu', 'su', 'bih', 'bejah', 'beh', 'bejase', 'bi', 'bese', 'bejasmo', 'bismo', 'besmo', 'bejaste',
        'biste', 'beste', 'bejahu', 'bejahu', 'bi', 'bise', 'behu', 'bio', 'bili', 'budimo', 'budite', 'bila', 'bilo',
        'bile', 'cu', 'ces', 'ce', 'cemo', 'cete', 'zelim', 'zelis', 'zeli', 'zelimo', 'zelite', 'zele', 'moram',
        'moras', 'mora', 'moramo', 'morate', 'moraju', 'trebam', 'trebas', 'treba', 'trebamo', 'trebate', 'trebaju',
        'mogu', 'mozes', 'moze', 'mozemo', 'mozete'}


def syllable_r(text):
    return re.sub(r'(^|[^aeiou])r($|[^aeiou])', r'\1R\2', text)


def has_vowel(text):
    if re.search(r'[aeiouR]', syllable_r(text)) is None:
        return False
    else:
        return True


def replace_special_characters(input_text):
    input_text = input_text.replace("Č", "C")
    input_text = input_text.replace("Ć", "C")
    input_text = input_text.replace("Dž", "Dz")
    input_text = input_text.replace("Đ", "Dj")
    input_text = input_text.replace("Š", "S")
    input_text = input_text.replace("Ž", "Z")

    input_text = input_text.replace("č", "c")
    input_text = input_text.replace("ć", "c")
    input_text = input_text.replace("dž", "dz")
    input_text = input_text.replace("đ", "dj")
    input_text = input_text.replace("š", "s")
    input_text = input_text.replace("ž", "z")

    return input_text


def transform(token, transformations):
    for search, swap in transformations:
        if token.endswith(search):
            return token[:-len(search)] + swap
    return token


def root(token, rules):
    for rule in rules:
        division = rule.match(token)
        if division is not None:
            if has_vowel(division.group(1)) and len(division.group(1)) > 1:
                return division.group(1)
    return token


def stem(input_text):
    input_text = replace_special_characters(input_text)
    output_text = ''
    rules = [re.compile(r'^('+osnova+')('+nastavak+r')$') for osnova, nastavak in [e.strip().split(' ') for e in open('rules.txt')]]
    transformations = [e.strip().split('\t') for e in open('transformations.txt')]
    for token in re.findall(r'\w+', input_text, re.UNICODE):
        if token.lower() in stop:
            output_text += token.lower() + ' '
            continue
        output_text += root(transform(token.lower(), transformations), rules) + ' '

    return output_text
