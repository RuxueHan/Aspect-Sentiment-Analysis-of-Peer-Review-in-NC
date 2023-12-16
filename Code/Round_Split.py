import difflib
import os
import xlsxwriter

counttest = 0

def read_txt(path):
    with open(path, 'r', encoding=u'utf-8' or 'ANSI', errors='ignore') as f:
        lines = f.readlines()
        return lines


def get_txtdict(lines, path, dir_name):
    global counttest
    # ,Segmentation results are stored in the sections list
    sections = []  #  a list store each segment
    k = 0  # Control rows
    while k < len(lines):
        sline = ""
        if len(lines[k]) > 2:  # the beginning of a paragraph
            sline = ' '.join(lines[k].split()).replace("\n", "")  
            if k + 1 < len(lines):
                sline2 = ""
                for j in range(k, len(lines) - 1):
                    if len(lines[j + 1]) > 2 and j + 1 < len(lines) - 1:
                        if "reviewers' comments" in lines[j + 1].lower() or "reviewer comments" in lines[j + 1].lower(): #Judge whether the next line is "reviewer comment" or not.
                            sline = sline + sline2
                            sections.append(sline)
                            sections.append(lines[j + 1])
                            k = j + 1
                            break
                        else:
                            sline2 = sline2 + "\n" + ' '.join(lines[j + 1].split()).replace("\n", "")
                    elif len(lines[j + 1]) > 2 and j + 1 == len(lines) - 1:    # Judging whether it is the last line
                        sline2 = sline2 + "\n" + ' '.join(lines[j + 1].split()).replace("\n", "")
                        sline = sline + sline2
                        sections.append(sline)
                        k = j + 1
                        break
                    else:
                        sline = sline + sline2
                        sections.append(sline)
                        k = j
                        break
        k += 1

    # Record the segment number at the split of each round
    Round = []
    weizhi = []  # Record the paragraph number (position) of the segmentation
    tip = []  # Record the split position as the start of the reply OR the start of the next round.
    p = 1    # Record each paragraph number
    index = 0  
    n = 0  # Record the number of elements in the list weizhi
    rounddict = {}

    if len(sections) == 0:   # The entire text is one paragraph, not subparagraphs
        print("None-" + path)
        key = "@@Round-1"
        rounddict[key] = "None comment"
        return rounddict
    else:
        Round.append(sections[0])
        weizhi.append(0)    
        tip.append("newRound-begin")
        for ee in sections[1:len(sections)]:
            # Calculating text similarity using difflib
            for i in Round[weizhi[n]:]:
                _ee = ' '.join(ee.split()).split('.')[0]  # 截取一句计算相似度
                _i = ' '.join(i.split()).split('.')[0]
                lable = ("reviewer #" in ee.lower() or "reviewers' comments" in ee.lower() or "reviewer comments" in ee.lower()) and len(ee) < 60  # 标签行
                if index == 0 and lable:
                    break
                if index == 0 and not (lable) and difflib.SequenceMatcher(None, _ee, _i).quick_ratio() > 0.9 and len(_ee) > 60:
                    index = 1  # index 0->1 marking the beginning of the response
                    break
                if index == 1 and ("reviewers' comments" in ee.lower() or "reviewer comments" in ee.lower()) and len(ee) < 30:
                    index = 0  # index 1->0 marking the beginning of the next round
                    weizhi.append(p)
                    n += 1
                    tip.append("newRound-begin")
                    break
            p += 1
            Round.append(ee)
        weizhi.append(len(sections))  # Record the last segment number
        if len(weizhi) == 3 or len(weizhi) == 4:
            counttest += 1

        # Merge each segment by split position, save as dictionary

        roundcount = 1
        responsecount = 1
        for i in range(len(weizhi) - 1):
            if "newRound" in tip[i]:
                key = "@@Round-" + str(roundcount)
                rounddict[key] = '\n\n'.join(sections[weizhi[i]:weizhi[i + 1]])
                roundcount += 1
        return rounddict


def get_dir_path(root_path):
    dir_list = []
    for root, dirs, files in os.walk(root_path):
        for d in dirs:
            dir_list.append(os.path.join(root, d))
    return dir_list


def get_file_path(dir_path):    # Get the file path and file name for each discipline
    file_path_list = []
    file_name_list = []
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            file_path_list.append(os.path.join(root, f))
            file_name_list.append(os.path.basename(f))
    return file_path_list, file_name_list

def pr_dic_write(dir_path, dir_name, dic):  
    file_path = dir_path + '\\' + dir_name + '1' + '.xlsx'
    f = xlsxwriter.Workbook(str(file_path))
    sheet1 = f.add_worksheet(u'sheet1')  
    i = 0
    for k, v in dic.items(): 
        sheet1.write(i, 0, k)
        i += 1
        round = 1
        for k1, v1 in v.items(): 
            sheet1.write(i, 0, k1)
            sheet1.write(i, 1, v1)
            i += 1
            round += 1
    f.close()

def pr_dic_write_txt(dir_path, dir_name, dic):  
    for k, v in dic.items():  
        # round = 1
        for k1, v1 in v.items(): 
            file_path = dir_path + '\\' + k.split('.')[0] + '-' + k1 + '.txt'
            with open(file_path, 'w', encoding=u'utf-8' or 'ANSI', errors='ignore') as f:
                f.write(v1)
            f.close()

if __name__ == '__main__':
    root_path = './ncomms pr txt/Biological sciences'
    dir_list = get_dir_path(root_path)  # second-level disciplines
    subject_dic = {}
    for dir_path in dir_list:  # Obtaining reviews in a discipline
        dir_name = os.path.basename(dir_path)
        file_path_list, file_name_list = get_file_path(dir_path)
        dic = {}
        for i in range(len(file_path_list)):  # Obtaining a review of a document
            path = file_path_list[i]
            print(path)
            lines = read_txt(path)
            txtdict_final = get_txtdict(lines, path, dir_name)
            name = file_name_list[i]
            dic[name] = txtdict_final
        # pr_dic_write(dir_path, dir_name, dic)   # write into excel
        pr_dic_write_txt(dir_path, dir_name, dic)  #  write into txt
        subject_dic[dir_name] = dic
        print(counttest)
