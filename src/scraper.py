# coding=utf-8
from bs4 import BeautifulSoup
import writer


def get_result_links(html):
    """
    Extract urls to search result documents
    :param html: result page html
    :return: list of urls
    """
    ret_val = []

    soup = BeautifulSoup(html, 'html.parser')

    urls = soup.findAll("a", attrs={"ng-if": "item.uuid !== null"})
    for url in urls:
        ret_val.append(url['href'])

    return ret_val


def save_document_data(html, save_directory, name):
    """
    Extract document metadata and send to writer
    :param html: html of document page
    :param save_directory: save directory
    :param name: document number in current sub register
    """
    # preparing writing files
    ids_name = 'data/' + save_directory + '/ids/' + str(name) + '.txt'

    soup = BeautifulSoup(html, 'html.parser')
    all_labels = soup.findAll("td", attrs={"class": "act-idcard-label-cell-1"})
    all_values = soup.findAll("td", attrs={"class": "act-idcard-value-cell-1"})
    labels = []
    values = []
    for label in all_labels:
        labels.append(label.get_text().strip())

    for value in all_values:
        values.append(value.get_text().strip())

    ids = ''
    for i in range(len(labels)):
        ids += labels[i] + '\n' + values[i] + '\n'

    # writing content
    writer.write_document(ids_name, ids)


def save_document_links(html, save_directory, name):
    """
    Extract document references and send to writer
    :param html: references html page
    :param save_directory: save directory
    :param name: document number in current sub register
    """
    links_name = 'data/' + save_directory + '/links/' + str(name) + '.txt'
    soup = BeautifulSoup(html, 'html.parser')
    all_links = soup.findAll("a", attrs={"ng-bind": "link.name"})
    links = []
    for link in all_links:
        links.append(link.get_text().strip())

    links_text = ''
    for link in links:
        links_text += link + '\n'
    writer.write_document(links_name, links_text)


def save_document_content(html, save_directory, name):
    """
    Extract document text and send to writer
    :param html: document html
    :param save_directory: save directory
    :param name: document number in current sub register
    """
    docs_name = 'data/' + save_directory + '/docs/' + str(name) + '.txt'
    soup = BeautifulSoup(html, 'html.parser')
    docs = soup.find("body")
    docs_text = docs.get_text().strip()
    writer.write_document(docs_name, docs_text)
