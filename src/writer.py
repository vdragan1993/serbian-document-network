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
