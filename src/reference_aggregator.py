# coding=utf-8
__author__ = "Dragan Vidakovic"

import reader
import writer
import os


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


def list_files_from_directory(directory):
    ret_val = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            ret_val.append(str(file))
    return ret_val


def extract_file_references(file_path):
    lines = reader.read_file_line(file_path)
    clean_lines = [line[:-2] for line in lines if line.endswith('\r\n')]
    #clean_lines.append(lines[-1][:-2])
    srcs = []
    dists = []
    for line in clean_lines:
        splits = line.split('\t\t\t')
        srcs.append(splits[0])
        dists.append(splits[1])

    return clean_lines, srcs, dists


if __name__ == '__main__':
    doc_num_dict, num_doc_dict = load_doc_num('data/ascii/new_num_doc_sorted.txt')
    all_text_lines = []
    all_num_lines = []
    all_documents = list_files_from_directory('data/ascii/graph')
    for document in all_documents:
        new_lines, new_srcs, new_dists = extract_file_references('data/ascii/graph/' + document)
        all_text_lines += new_lines

        for i in range(len(new_srcs)):
            src_num = doc_num_dict[new_srcs[i]]
            dist_num = doc_num_dict[new_dists[i]]
            new_num_line = str(src_num) + "\t\t\t" + str(dist_num)
            all_num_lines.append(new_num_line)

    print(len(all_text_lines))
    writer.write_list_of_lines('data/ascii/all_text_lines.txt', all_text_lines)
    print(len(all_num_lines))
    writer.write_list_of_lines('data/ascii/all_num_lines.txt', all_num_lines)
