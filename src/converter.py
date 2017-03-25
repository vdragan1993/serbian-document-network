# coding=utf-8
__author__ = "Dragan Vidakovic"


def convert_to_latin(input_text):
    """
    Convert Serbian Cyrillic to Latin
    :param input_text: Cyrillic text
    :return: Latin text
    """
    # caps
    input_text = input_text.replace("А", "a")
    input_text = input_text.replace("Б", "b")
    input_text = input_text.replace("В", "v")
    input_text = input_text.replace("Г", "g")
    input_text = input_text.replace("Д", "d")
    input_text = input_text.replace("Ђ", "dj")
    input_text = input_text.replace("Е", "e")
    input_text = input_text.replace("Ж", "z")
    input_text = input_text.replace("З", "z")
    input_text = input_text.replace("И", "i")
    input_text = input_text.replace("Ј", "j")
    input_text = input_text.replace("К", "k")
    input_text = input_text.replace("Л", "l")
    input_text = input_text.replace("Љ", "lj")
    input_text = input_text.replace("М", "m")
    input_text = input_text.replace("Н", "n")
    input_text = input_text.replace("Њ", "nj")
    input_text = input_text.replace("О", "o")
    input_text = input_text.replace("П", "p")
    input_text = input_text.replace("Р", "r")
    input_text = input_text.replace("С", "s")
    input_text = input_text.replace("Т", "t")
    input_text = input_text.replace("Ћ", "c")
    input_text = input_text.replace("У", "u")
    input_text = input_text.replace("Ф", "f")
    input_text = input_text.replace("Х", "h")
    input_text = input_text.replace("Ц", "c")
    input_text = input_text.replace("Ч", "c")
    input_text = input_text.replace("Џ", "dz")
    input_text = input_text.replace("Ш", "s")
    # non caps
    input_text = input_text.replace("а", "a")
    input_text = input_text.replace("б", "b")
    input_text = input_text.replace("в", "v")
    input_text = input_text.replace("г", "g")
    input_text = input_text.replace("д", "d")
    input_text = input_text.replace("ђ", "dj")
    input_text = input_text.replace("е", "e")
    input_text = input_text.replace("ж", "z")
    input_text = input_text.replace("з", "z")
    input_text = input_text.replace("и", "i")
    input_text = input_text.replace("ј", "j")
    input_text = input_text.replace("к", "k")
    input_text = input_text.replace("л", "l")
    input_text = input_text.replace("љ", "lj")
    input_text = input_text.replace("м", "m")
    input_text = input_text.replace("н", "n")
    input_text = input_text.replace("њ", "nj")
    input_text = input_text.replace("о", "o")
    input_text = input_text.replace("п", "p")
    input_text = input_text.replace("р", "r")
    input_text = input_text.replace("с", "s")
    input_text = input_text.replace("т", "t")
    input_text = input_text.replace("ћ", "c")
    input_text = input_text.replace("у", "u")
    input_text = input_text.replace("ф", "f")
    input_text = input_text.replace("х", "h")
    input_text = input_text.replace("ц", "c")
    input_text = input_text.replace("ч", "c")
    input_text = input_text.replace("џ", "dz")
    input_text = input_text.replace("ш", "s")

    return input_text
