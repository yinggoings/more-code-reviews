from find_xml_file.find_xml_file import find_xml_file


def test_no_files_returns_None():
    assert find_xml_file(".") is None


def test_finds_existing_xml_file():
    PATH_TO_TEST_XML = "./test/test_data"
    assert find_xml_file(PATH_TO_TEST_XML) == "example.xml"
