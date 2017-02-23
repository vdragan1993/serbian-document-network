import codecs


def write_list_of_links(sub_register, links):
    """
    Write list of search result links in text file
    :param sub_register: sub register value
    :param links: list of search result links
    :return:
    """
    f = open('data/' + sub_register + '.txt', 'w')
    lines = '\n'.join(links)
    f.write(lines)
    f.close()


def write_document(document_name, content):
    """
    Write cyrillic content into text file at given location
    :param document_name:
    :param content:
    :return:
    """
    f = codecs.open(document_name, 'w', 'utf-8')
    f.write(content)
    f.close()
