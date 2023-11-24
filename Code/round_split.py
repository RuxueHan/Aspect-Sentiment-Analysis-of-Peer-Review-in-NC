import difflib
import os
import xlsxwriter

counttest = 0

def read_txt(path):
    with open(path, 'r', encoding=u'utf-8' or 'ANSI', errors='ignore') as f:
        lines = f.readlines()
        return lines

# 求两字符串的最长公共子串
def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]
    # 开辟列表空间
    # 多了一位以后就不存在超界问题
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位
    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:  # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:  # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]  # 记录最大匹配长度的终止位置
                    p = i + 1
    return maxNum

def get_txtdict(lines, path, dir_name):
    global counttest
    # 分段，存入sections列表
    sections = []  # 存储每一段的列表
    k = 0  # 控制行数
    while k < len(lines):
        sline = ""
        if len(lines[k]) > 2:  # 一段的开始
            sline = ' '.join(lines[k].split()).replace("\n", "")  # ' '.join(xxx.split()) 将多个空格替换成一个空格
            if k + 1 < len(lines):
                sline2 = ""
                for j in range(k, len(lines) - 1):
                    # print(len(lines))
                    # if len(lines[j + 1]) > 2 and j + 1 < len(lines) - 1:
                    #     sline2 = sline2 + " " + ' '.join(lines[j + 1].split()).replace("\n", "")
                    if len(lines[j + 1]) > 2 and j + 1 < len(lines) - 1:
                        if "reviewers' comments" in lines[j + 1].lower() or "reviewer comments" in lines[j + 1].lower(): #判断下一行是否是reviewer comments
                            sline = sline + sline2
                            sections.append(sline)
                            sections.append(lines[j + 1])
                            k = j + 1
                            break
                        else:
                            sline2 = sline2 + "\n" + ' '.join(lines[j + 1].split()).replace("\n", "")
                    elif len(lines[j + 1]) > 2 and j + 1 == len(lines) - 1:    # 判断是否是最后一行
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

    # 记录每轮分割处的段号
    Round = []
    weizhi = []  # 记录分割段的段号（位置）
    tip = []  # 记录分割位置是回复开始or下一轮开始
    p = 1    # 记录每一段段号
    index = 0  # 标识位
    n = 0  # 记录列表weizhi中的元素个数
    rounddict = {}

    if len(sections) == 0:   # 全文只有一段，未分段
        print("None-" + path)
        key = "@@Round-1"
        rounddict[key] = "None comment"
        return rounddict
    else:
        Round.append(sections[0])
        weizhi.append(0)    # 第0段为第一轮的开始
        tip.append("newRound-begin")
        for ee in sections[1:len(sections)]:
            # print(str(p) + "-" + ee)

            # 方法①：计算两字符串的最长公共子串
            # for i in Round[weizhi[n]:]:  # Round[weizhi[n]:]  将每一轮分割开来，如第二轮开始后直接从第二轮开始段位置之后进行匹配
            #     _ee = ''.join(ee.split())  # 去除掉一段中所有空格，包括单词之间的空格
            #     _i = ''.join(i.split())
            #     lable = ("reviewer #" in ee.lower() or "reviewers' comments" in ee.lower() or "reviewer comments" in ee.lower()) and len(ee) < 60  # 标签行
            #     if index == 0 and lable:
            #         break
            #     if index == 0 and not (lable) and getNumofCommonSubstr(_ee, _i) > 150:
            #         index = 1  # index由0->1 回复开始
            #         # weizhi.append(p)
            #         # tip.append("response-begin")
            #         break
            #     if index == 1 and ("reviewers' comments" in ee.lower() or "reviewer comments" in ee.lower()) and len(ee) < 30:
            #         index = 0  # index由1->0 下一轮开始
            #         weizhi.append(p)
            #         n += 1
            #         tip.append("newRound-begin")
            #         break

            # 方法②：difflib计算相似度
            for i in Round[weizhi[n]:]:
                _ee = ' '.join(ee.split()).split('.')[0]  # 截取一句计算相似度
                _i = ' '.join(i.split()).split('.')[0]
                lable = ("reviewer #" in ee.lower() or "reviewers' comments" in ee.lower() or "reviewer comments" in ee.lower()) and len(ee) < 60  # 标签行
                if index == 0 and lable:
                    break
                if index == 0 and not (lable) and difflib.SequenceMatcher(None, _ee, _i).quick_ratio() > 0.9 and len(_ee) > 60:
                    index = 1  # index由0->1 回复开始
                    # weizhi.append(p)
                    # tip.append("response-begin")
                    break
                if index == 1 and ("reviewers' comments" in ee.lower() or "reviewer comments" in ee.lower()) and len(ee) < 30:
                    index = 0  # index由1->0 下一轮开始
                    weizhi.append(p)
                    n += 1
                    tip.append("newRound-begin")
                    break
            p += 1
            Round.append(ee)
        weizhi.append(len(sections))  # 记录最后一段段号
        if len(weizhi) == 3 or len(weizhi) == 4:
            counttest += 1
            # print(path)

        # 按分割位置合并每段，存为字典

        roundcount = 1
        responsecount = 1
        for i in range(len(weizhi) - 1):
            if "newRound" in tip[i]:
                key = "@@Round-" + str(roundcount)
                rounddict[key] = '\n\n'.join(sections[weizhi[i]:weizhi[i + 1]])
                roundcount += 1
            # elif "response" in tip[i]:
            #     key = "Response to @@Round-" + str(responsecount)
            #     rounddict[key] = '\n\n'.join(sections[weizhi[i]:weizhi[i + 1]])
            #     responsecount += 1
        return rounddict


def get_dir_path(root_path):
    dir_list = []
    for root, dirs, files in os.walk(root_path):
        for d in dirs:
            dir_list.append(os.path.join(root, d))
    return dir_list


def get_file_path(dir_path):    # 获得每个学科的文件路径及文件名
    file_path_list = []
    file_name_list = []
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            # print(os.path.join(root, f))
            # print(os.path.basename(f))
            file_path_list.append(os.path.join(root, f))
            file_name_list.append(os.path.basename(f))
    return file_path_list, file_name_list

# 分割写入Excel
def pr_dic_write(dir_path, dir_name, dic):  # 写入pr字典
    file_path = dir_path + '\\' + dir_name + '1' + '.xlsx'
    f = xlsxwriter.Workbook(str(file_path))
    sheet1 = f.add_worksheet(u'sheet1')  # 创建sheet1
    # 将数据写入第 i 行，第 j 列
    i = 0
    for k, v in dic.items():  # 遍历每个文件
        sheet1.write(i, 0, k)
        i += 1
        round = 1
        for k1, v1 in v.items():  # 遍历文件的每个字典
            # sheet1.write(i, 0, '@@Round #'+str(round))
            sheet1.write(i, 0, k1)
            sheet1.write(i, 1, v1)
            i += 1
            round += 1
    f.close()

# 分割写入txt
def pr_dic_write_txt(dir_path, dir_name, dic):  # 写入pr字典
    for k, v in dic.items():  # 遍历每个文件
        # round = 1
        for k1, v1 in v.items():  # 遍历文件的每个字典
            file_path = dir_path + '\\' + k.split('.')[0] + '-' + k1 + '.txt'
            with open(file_path, 'w', encoding=u'utf-8' or 'ANSI', errors='ignore') as f:
                f.write(v1)
            # round += 1
            f.close()

if __name__ == '__main__':
    root_path = 'C:/Users/Han Ruxue/Desktop/Biological sciences'
    dir_list = get_dir_path(root_path)  # 二级学科
    subject_dic = {}
    for dir_path in dir_list:  # 获得某个学科的评审意见
        dir_name = os.path.basename(dir_path)
        # print(dir_name)
        file_path_list, file_name_list = get_file_path(dir_path)
        dic = {}
        for i in range(len(file_path_list)):  # 获得一个文件的评审意见
            path = file_path_list[i]
            print(path)
            lines = read_txt(path)
            txtdict_final = get_txtdict(lines, path, dir_name)
            name = file_name_list[i]
            dic[name] = txtdict_final
        # pr_dic_write(dir_path, dir_name, dic)   # 写入excel
        pr_dic_write_txt(dir_path, dir_name, dic)  # 写入txt
        subject_dic[dir_name] = dic
        print(counttest)
