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
        mdFile.new_header(level=2, title=test_key)
        mdFile.new_line('~~~')
        mdFile.new_line(tests[test_key]['command'])
        mdFile.new_line('~~~')

        test_res = tests[test_key]['result']
        list_of_strings = ['Test'] + list(test_res.keys())
        cols = len(list_of_strings)
        rows = 1
        avg = {}
        avgc = {}
        for r in res:
            list_of_strings.extend( [r['name'] + " (" + r['iteration'] + ")"] + list(r['tests'][test_key]['result'].values()) )
            rows += 1
            if r['name'] not in avg.keys():
                avg[r['name']] = list(r['tests'][test_key]['result'].values())
                avgc[r['name']] = 1
            else:
                avg[r['name']] = [str(float(x) + float(y)) for x, y in zip(avg[r['name']], list(r['tests'][test_key]['result'].values()))]
                avgc[r['name']] += 1

        for avg_key in avg.keys():
            avg[avg_key] = [str(round(float(x) / avgc[avg_key], 3)) for x in avg[avg_key]]
            list_of_strings.extend( [avg_key + " (avg)"] + avg[avg_key] )
            rows += 1

        mdFile.new_table(columns=cols, rows=rows, text=list_of_strings, text_align='left')
        mdFile.new_line()

    mdFile.create_md_file()
    print("{}.md succesfully created".format(output))
