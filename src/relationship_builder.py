# coding=utf-8
__author__ = "Dragan Vidakovic"
import reader
import os
import writer
from nltk.tokenize import RegexpTokenizer
import serbian_stemmer


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


def get_document_links(document_name):
    ret_val = []
    if is_file_in_directory(document_name, 'data/latin/links'):
        ret_val = extract_link_names('data/latin/links/' + document_name)

    return ret_val


def remove_list_from_list(a, b):
    new_list = [x for x in a if x not in b]
    return new_list


def tokenize_and_stem(sentence):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(sentence)
    ret_val = []
    for word in words:
        ret_val.append(serbian_stemmer.stem(word).strip())
    return ret_val


def contains_reference(original_document, ref_document_words):
    ref_document = ' '.join(ref_document_words)
    return ref_document in original_document


def find_document_references(document_name, list_of_documents):
    ret_val = []
    original_document_words = tokenize_and_stem(reader.read_file_content('data/latin/docs/' + document_name))
    original_document_text = ' '.join(original_document_words)
    for ref_document in list_of_documents:
        ref_document_words = tokenize_and_stem(ref_document)
        if contains_reference(original_document_text, ref_document_words):
            ret_val.append(ref_document)
    return ret_val


def find_max_value(input_dict):
    return max(input_dict.values())


def is_file_in_directory(file_name, directory):
    for file in os.listdir(directory):
        if str(file) == file_name:
            return True

    return False


def list_files_from_directory(directory):
    ret_val = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            ret_val.append(str(file))
    return ret_val


def form_output_lines(source, destinations):
    ret_val = []
    for destination in destinations:
        new_line = source + "\t\t\t" + destination
        ret_val.append(new_line)

    return ret_val


if __name__ == '__main__':
    doc_num_dict, num_doc_dict = load_doc_num('data/latin/new_num_doc_sorted.txt')
    all_documents = num_doc_dict.keys()
    total_relationships = 0
    for document in all_documents:
        # existing links
        existing_links = get_document_links(str(document) + ".txt")
        # search for new links
        not_to_look = []
        not_to_look.append(num_doc_dict[document])
        if len(existing_links) > 0:
            not_to_look += existing_links
        docs_to_look = remove_list_from_list(doc_num_dict.keys(), not_to_look)
        new_links = find_document_references(str(document) + ".txt", docs_to_look)
        new_links += existing_links
        # write as source - destination pairs
        if len(new_links) > 0:
            lines_to_write = form_output_lines(num_doc_dict[document], new_links)
            writer.write_list_of_lines('data/graph/' + str(document) + ".txt", lines_to_write)
            print("Done document: {0}".format(document))
            total_relationships += len(new_links)

    print("Total relationships: {0}".format(total_relationships))
