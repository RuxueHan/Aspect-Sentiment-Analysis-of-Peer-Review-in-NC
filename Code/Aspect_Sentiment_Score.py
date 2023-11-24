import os
import xlrd
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def walkFile(root_path):
    files_list = []
    dir_list = []
    for root, dirs, files in os.walk(root_path):
        for f in files:
            files_list.append(os.path.join(root, f))
        for d in dirs:
            dir_list.append(os.path.join(root, d))
    return files_list, dir_list


def read_xlsx(xlsx_path, i):  # 读取同行评审句数据表，获得评审标签
    data = []
    data_xsls = xlrd.open_workbook(xlsx_path)
    sheet_name = data_xsls.sheets()[i]
    sentiments = sheet_name.col_values(0)[0:]  # 情感极性
    aspects = sheet_name.col_values(3)[0:]  # 属性词
    return sentiments, aspects


def aspect_word(path):  # 读取各属性类
    data_xlsx = xlrd.open_workbook(path)
    sheet_name = data_xlsx.sheets()[0]
    count_nrows = sheet_name.nrows
    count_ncols = sheet_name.ncols
    i = 0
    aspect_dict = {}
    while i < count_ncols:
        key = sheet_name.col_values(i)[1]
        aspect_dict[key] = sheet_name.col_values(i)[2:]
        aspect_dict[key] = [k for k in aspect_dict[key] if k != '']
        i += 1
    return aspect_dict


def sentiment_score(score_dic, frequency_dic, classname, classaspects, sentiments, aspects):
    for i in range(len(aspects)):
        m = 0
        while m < 11:
            if lemmatizer.lemmatize(aspects[i]) in classaspects[m]:
                score_dic[classname[m]] += int(sentiments[i])  # 该属性类下的属性词情感及极性累加
            if lemmatizer.lemmatize(aspects[i]) in classaspects[m]:
                frequency_dic[classname[m]] += 1  # 该属性类下的属性词正、中、负情感极性频次累加
            m += 1

    return score_dic, frequency_dic


if __name__ == '__main__':
    root_path = r'E:\毕业论文\韩茹雪-毕业论文数据\part_2 多轮同行评审意见的属性情感自动分类\ncomms pr txt round\Round=6'
    files_list, dir_list = walkFile(root_path)
    files_list = [path for path in files_list if
                  'Round' in os.path.basename(path) and '.xlsx' in os.path.basename(path)]
    write_path = 'C:/Users/Han Ruxue/Desktop/score6.txt'
    print(len(files_list))

    aspect = aspect_word('E:/科研训练/aspect-test/Aspect-cluster.xlsx')
    classname = list(aspect.keys())
    classaspects = list(aspect.values())

    class_list = ''
    for a in classname:
        class_list = class_list + str(a) + '\t'
    with open(write_path, 'a+') as f:
        f.write('Paper_ID' + '\t' + '评审总轮数' + '\t' + class_list + '\n')
    f.close()

    for i in range(0, len(files_list), 6):
        score_dic = {}
        frequency_dic = {}
        for m in classname:
            score_dic[m] = 0  # 初始值为0
            frequency_dic[m] = 0

        total_sentiments = []
        total_aspects = []
        for n in range(0, 6):
            sentiments, aspects = read_xlsx(files_list[i + n], 0)
            total_sentiments += sentiments
            total_aspects += aspects
        score_dic, frequency_dic = sentiment_score(score_dic, frequency_dic, classname, classaspects, total_sentiments,
                                                   total_aspects)

        for key, value in score_dic.items():
            if value != 0:
                score_dic[key] = value / frequency_dic[key]
            else:
                score_dic[key] = 0

        score_list = ''
        for b in score_dic.values():
            score_list = score_list + str(b) + '\t'

        with open(write_path, 'a+') as f:
            f.write(os.path.basename(files_list[i]).split('-@@')[0] + '\t' + '6' + '\t' + score_list + '\n')
        f.close()

