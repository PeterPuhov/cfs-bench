import json
from mdutils import MdUtils
from tabulate import tabulate
import numpy

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

def delta(b, p, hib):
    if(hib):
        return round(100 * (p - b)/ b, 3)
    else:
        return round(100 * (b - p)/ b, 3)

def create_patch_table(base, patch, hib, is_short=True):
    table_list = []
    b_arr = numpy.array(base)
    p_arr = numpy.array(patch)

    b = round(numpy.mean(b_arr), 3)
    p = round(numpy.mean(p_arr), 3)
    d = delta(b, p, hib)        
    col = ['mean', str(b), str(p), str(d)] 
    table_list.append(col)

    b = round(numpy.std(b_arr) * 100 / b, 3)
    p = round(numpy.std(p_arr) * 100 / p, 3)
    d = delta(b, p, hib)        
    col = ['std (%)', str(b), str(p), str(d)] 
    table_list.append(col)

    if is_short:
        return table_list

    b = round(numpy.min(b_arr), 3)
    p = round(numpy.min(p_arr), 3)
    d = delta(b, p, hib)        
    col = ['min', str(b), str(p), str(d)] 
    table_list.append(col)

    for per in [50, 75, 99]:
        b = round(numpy.percentile(b_arr, per), 3)
        p = round(numpy.percentile(p_arr, per), 3)
        d = delta(b, p, hib)        
        col = ['{}%'.format(per), str(b), str(p), str(d)] 
        table_list.append(col)

    b = round(numpy.max(b_arr), 3)
    p = round(numpy.max(p_arr), 3)
    d = delta(b, p, hib)        
    col = ['max', str(b), str(p), str(d)] 
    table_list.append(col)    

    return table_list


def create_patch(res_files: [], output: str, title="", description=""):
    res = []
    for f in res_files:
        with open(f) as json_file:
            res.append(json.load(json_file))

    print('Test results: \n\n\n')
    f = open(output + ".github", 'w')
    tests = res[0]['tests']
    for test_key in tests.keys():        
        test_res = tests[test_key]['result']        
        baseline_res = []
        patch_res = []
        for r in res:            
            if 'BASELINE' in r['name']:
                baseline_res.append(r['tests'][test_key]['raw_result'])
            elif 'PATCH' in r['name']:
                 patch_res.append(r['tests'][test_key]['raw_result'])
            else:
                print('Invalid name: ' + r['name'])
        
        table_list = create_patch_table(baseline_res, patch_res, r['tests'][test_key]['result']['HIB'])
        
        s = "{} iterations of:\n".format(len(baseline_res)) + tests[test_key]['command'] + "\n"
        if r['tests'][test_key]['result']['HIB']:
            s += "Higher result is better\n"
        else:
            s += "Lower result is better\n"
        s += "\n"            
        s += tabulate(table_list, [' ', 'BASELINE', '+PATCH', 'DELTA (%)'], tablefmt="github") +"\n\n"
        print(s)
        f.write(s)
    
    f.close()

def create_patch_loop(res_files: [], output: str, title="", description=""):
    res = []
    for f in res_files:
        with open(f) as json_file:
            res.append(json.load(json_file))

    print('Test results: \n\n\n')
    f = open(output + ".github", 'w')

    b_report = {}
    p_report = {}
    for r in res:
        tests = r['tests']        
        for test_key in tests.keys():            
            raw_result = []
            for t in tests[test_key]:
                raw_result.append(t['raw_result'])
                        
            if 'BASELINE' in r['name']:
                b_report[test_key] = {}
                b_report[test_key]['command'] = tests[test_key][0]['command']
                b_report[test_key]['HIB'] = tests[test_key][0]['result']['HIB']
                b_report[test_key]['raw_result'] = raw_result
            elif 'PATCH' in r['name']:
                p_report[test_key] = {}
                p_report[test_key]['command'] = tests[test_key][0]['command']
                p_report[test_key]['HIB'] = tests[test_key][0]['result']['HIB']
                p_report[test_key]['raw_result'] = raw_result


    for test_key in b_report.keys():            
        table_list = create_patch_table(b_report[test_key]['raw_result'], 
                                        p_report[test_key]['raw_result'], 
                                        b_report[test_key]['HIB'])
    
        s = "{} iterations of:\n".format(len(b_report[test_key]['raw_result'])) + b_report[test_key]['command'] + "\n"
        if b_report[test_key]['HIB']:
            s += "Higher result is better\n"
        else:
            s += "Lower result is better\n"

        s += "\n"            
        s += tabulate(table_list, [' ', 'BASELINE', '+PATCH', 'DELTA (%)'], tablefmt="github") +"\n\n"
        print(s)
        f.write(s)

    f.close()
