# coding=utf-8
__author__ = "Dragan Vidakovic"
import os
import reader
import converter
import writer


def list_files_from_directory(directory):
    """
    List all files from given directory
    :param directory:
    :return: list of file paths
    """
    ret_val = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            ret_val.append(str(file))
    return ret_val


def is_file_in_directory(file_name, directory):
    """
    Returns True if given file name is in given directory
    :param file_name:
    :param directory:
    :return:
    """
    for file in os.listdir(directory):
        if str(file) == file_name:
            return True

    return False


def extract_document_name(file_name):
    """
    Extracts document name from its id
    :param file_name:
    :return:
    """
    lines = reader.read_file_line('data/458/ids/' + file_name)
    name = converter.convert_to_latin(lines[1])
    return name.split(':')[0]


def extract_document_links(file_name):
    """
    Extracts linked documents for given document
    :param file_name:
    :return:
    """
    destination_file = 'data/latin/links/' + file_name
    if is_file_in_directory(file_name, 'data/458/links'):
        all_lines = reader.read_file_line('data/458/links/' + file_name)
        new_lines = []
        for line in all_lines:
            latin_line = converter.convert_to_latin(line)
            new_lines.append(latin_line.split(':')[0])
        writer.write_list_of_lines(destination_file, new_lines)


if __name__ == '__main__':
    all_documents = list_files_from_directory('data/458/docs')
    all_document_names = []
    for document in all_documents:
        all_document_names.append(extract_document_name(document))
        extract_document_links(document)
        content = reader.read_file_content('data/458/docs/' + document)
        latin_content = converter.convert_to_latin(content)
        writer.write_document('data/latin/docs/' + document, latin_content)
    writer.write_list_of_lines('data/latin/all_docs.txt', all_document_names)
