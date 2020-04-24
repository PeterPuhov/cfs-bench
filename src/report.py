import json
from mdutils import MdUtils


def create_report(res_files: [], output: str, title="", description=""):
    res = []
    for f in res_files:
        with open(f) as json_file:
            res.append(json.load(json_file))

    mdFile = MdUtils(file_name=output, title=title)
    if description:
        mdFile.new_paragraph(description, bold_italics_code='b')

    mdFile.new_header(level=1, title='Platform')

    platform = res[0]['platform']
    list_of_strings = ["System", "Information"]
    rows = 1
    for key in platform.keys():
        list_of_strings.extend([key, str(platform[key])])
        rows += 1
    mdFile.new_line()
    mdFile.new_table(columns=2, rows=rows, text=list_of_strings, text_align='left')

    mdFile.new_header(level=1, title='Test results')
    tests = res[0]['tests']
    for test_key in tests.keys():
        mdFile.new_paragraph("{}: {}".format(test_key, tests[test_key]['command']), bold_italics_code='bc', color='blue')
        list_of_strings = ["Test", "Result"]
        rows = 1
        for r in res:
            list_of_strings.extend([r['name'], r['tests'][test_key]['result'] + " ({})".format(tests[test_key]['unit'])])
            rows += 1
        mdFile.new_line()
        mdFile.new_table(columns=2, rows=rows, text=list_of_strings, text_align='left')
        mdFile.new_line()

    mdFile.create_md_file()
