# coding=utf-8
__author__ = "Dragan Vidakovic"
import reader
import os
import writer
from collections import OrderedDict
from operator import itemgetter


def load_doc_num(file_path):
    lines = reader.read_file_line(file_path)
    doc_num_mapper = {}
    num_doc_mapper = {}
    clean_lines = [line[:-2] for line in lines if line.endswith('\r\n')]
    clean_lines.append(lines[-1])
    for line in clean_lines:
        number = int(line.split(',')[0])
        text = line[len(str(number))+1:]
        doc_num_mapper[text] = number
        num_doc_mapper[number] = text
    return doc_num_mapper, num_doc_mapper


def extract_link_names(file_path):
    lines = reader.read_file_line(file_path)
    ret_val = []
    for line in lines:
        if line.endswith('\r\n'):
            ret_val.append(line[:-2])
        else:
            ret_val.append(line)
    return ret_val


def find_max_value(input_dict):
    return max(input_dict.values())


def list_files_from_directory(directory):
    ret_val = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            ret_val.append(str(file))
    return ret_val


if __name__ == '__main__':
    doc_num_dict, num_doc_dict = load_doc_num('data/latin/num_doc.txt')
    all_documents = list_files_from_directory('data/latin/links')
    for document in all_documents:
        links = extract_link_names('data/latin/links/' + document)
        for link in links:
            if link not in doc_num_dict and len(link) > 1:
                new_num = find_max_value(doc_num_dict) + 1
                doc_num_dict[link] = new_num

    doc_num_dict_sorted = OrderedDict(sorted(doc_num_dict.items(), key=itemgetter(1)))
    output_lines = []
    for document in doc_num_dict_sorted:
        new_line = str(doc_num_dict_sorted[document]) + "," + document
        output_lines.append(new_line)

    writer.write_list_of_lines('data/latin/new_num_doc_sorted.txt', output_lines)
