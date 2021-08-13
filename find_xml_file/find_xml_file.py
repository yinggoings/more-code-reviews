import os


def find_xml_file(folder):
    files = os.listdir(folder)

    xml_file = None

    for filename in files:
        if filename.endswith(".xml"):
            xml_file = filename
            break

    return xml_file
