import re
import nltk
from zhon.hanzi import punctuation
from nltk.corpus import wordnet
from nltk.parse import corenlp
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
import xlsxwriter
import os
import xlrd
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'D:\anaconda\stanfordNLP1\stanford-corenlp-4.1.0')
from nltk.parse import corenlp

nlp = corenlp.CoreNLPDependencyParser(url='http://localhost:9000')
nlp1 = StanfordCoreNLP(r'D:\anaconda\stanfordNLP1\stanford-corenlp-4.1.0')


# import stanza
# en_nlp = stanza.Pipeline('en')
def clean_text(path):  # 替换句子符号，分句
    with open(path, 'r', encoding='utf-8')as f:
        u = f.read().replace('=', '')
    nsen_list = []
    count = 0

    #     for u in reviews:
    u = re.sub('\. \. \.', '||| ||| |||', u)  # 英文省略号". . ."
    u = re.sub('et al\.', 'et al|||', u)  # 英文缩写"et al."
    u = re.sub('et\.', 'et|||', u)  # 英文缩写"i.a."
    u = re.sub('al\.', 'al|||', u)  # 英文缩写"i.a."
    u = re.sub('i\.e\.', 'i|||e|||', u)  # 英文缩写"i.e."
    u = re.sub('ie\.', 'ie|||', u)  # 英文缩写"i.e."
    u = re.sub('i\.i\.d\.', 'i|||i|||d|||', u)  # 英文缩写"i.i.d."
    u = re.sub('e\.g\.', 'e|||g|||', u)  # 英文缩写"e.g."
    u = re.sub('Fig\.', 'Fig|||', u)  # 英文缩写"Fig."
    u = re.sub('Tab\.', 'Tab|||', u)  # 英文缩写"Tab."
    u = re.sub('Sect\.', 'Sect|||', u)  # 英文缩写"Sect."
    u = re.sub('Eq\.', 'Eq|||', u)  # 英文缩写"Eq."
    u = re.sub('cf\.', 'cf|||', u)  # 英文缩写"cf."
    u = re.sub('E\.g\.', 'E|||g|||', u)  # 英文缩写"E.g."
    u = re.sub('Ex\.', 'Ex|||', u)  # 英文缩写"Ex."
    u = re.sub('v\.s\.', 'v|||s|||', u)  # 英文缩写"v.s."
    u = re.sub('vs\.', 'vs|||', u)  # 英文缩写"vs."
    u = re.sub('w\.r\.t\.', 'w|||r|||t|||', u)  # 英文缩写"w.r.t."
    u = re.sub('i\.a\.', 'i|||a|||', u)  # 英文缩写"i.a."
    u = re.sub('I\.e\.', 'I|||e|||', u)  # 英文缩写"i.a."
    u = re.sub('eq\.', 'e|||q|||', u)  # 英文缩写"i.a."
    u = re.sub('sec\.', 'sec|||', u)  # 英文缩写"i.a."
    u = re.sub('pp\.', 'pp|||', u)  # 英文缩写"i.a."
    u = re.sub('eg\.', 'eg|||', u)  # 英文缩写"i.a."
    u = re.sub('etc\.', 'etc|||', u)  # 英文缩写"i.a."
    u = re.sub('Sec\.', 'Sec|||', u)  # 英文缩写"i.a."
    u = re.sub('vol\.', 'vol|||', u)  # 英文缩写"i.a."
    u = re.sub('no\.', 'no|||', u)  # 英文缩写"i.a."
    u = re.sub('fig\.', 'fig|||', u)  # 英文缩写"i.a."
    u = re.sub('1\.', '1|||', u)  # 英文缩写"i.a."
    u = re.sub('2\.', '2|||', u)  # 英文缩写"i.a."
    u = re.sub('3\.', '3|||', u)  # 英文缩写"i.a."
    u = re.sub('4\.', '4|||', u)  # 英文缩写"i.a."
    u = re.sub('5\.', '5|||', u)  # 英文缩写"i.a."
    u = re.sub('6\.', '6|||', u)  # 英文缩写"i.a."
    u = re.sub('7\.', '7|||', u)  # 英文缩写"i.a."
    u = re.sub('8\.', '8|||', u)  # 英文缩写"i.a."
    u = re.sub('9\.', '9|||', u)  # 英文缩写"i.a."
    u = re.sub('0\.', '0|||', u)  # 英文缩写"i.a."
    u = re.sub('\,\n\t', '\,|||', u)  # 英文缩写"i.a."

    for sent in sent_tokenize(
            u.replace('Reviewers', '').replace('Reviewer #', '').replace('(Remarks to the Author):', '').replace(
                    'comments:', '')):
        if len(sent) < 60 or '' in sent or '$' in sent or '@@' in sent or '??' in sent:
            count += 0
        else:
            for i in punctuation:  # 去除中文符号
                sent = sent.replace(i, '')
            sent = sent.strip()  # 先去掉每个句子前后可能存在的空格
            sent = re.sub('\|\|\|', '.', sent)  # 将句子中可能存在的"|||"再替换成原来的"."
            if sent[-1] == ',' or sent[0] == ',':
                sent = sent.replace(',', '.')
            nsen_list.append(sent)
            count += 1

    return nsen_list


def get_reviews(path):  # 读取评审意见文本，获得切分好的语料
    sentence_list = []
    with open(path, 'r', encoding='utf-8')as f:
        txt = f.read().replace('=', '')
    for sent in sent_tokenize(txt):
        sentence_list.append(sent)
    return sentence_list


def get_new_review(reviews, nc2, nc3):  # 替换属性词组
    new_reviews_list = []
    for i in range(len(reviews)):
        new_reviews = reviews[i]
        #         if i%1000==0:
        #             print(i,'句正在处理中...',len(reviews))
        for j in range(len(nc3)):
            new_reviews = new_reviews.replace(nc2[j], nc3[j]).lower()
        new_reviews_list.append(new_reviews)
    #     print(new_reviews_list)
    return new_reviews_list


def read_xlsx(xlsx_path, i):  # 读取属性词表
    data = []
    data_xsls = xlrd.open_workbook(xlsx_path)
    sheet_name = data_xsls.sheets()[i]
    aspects = sheet_name.col_values(0)[0:]  # 属性词
    return aspects


def get_aspect_opinion(sentence):  # 通过句法关系获得属性词——情感词对
    opinion_to_aspect = []
    aspect_to_aspect = []
    opinion_xcomp_aspect = []
    sentence_list = nltk.word_tokenize(sentence)
    sentence_parse, = nlp.raw_parse(sentence)
    for (gov, gov_PoS), dependency, (dep, dep_PoS) in sentence_parse.triples():
        #     print((gov, gov_PoS), dependency, (dep, dep_PoS))

        if dependency == 'nsubj' and gov_PoS in ['JJ'] and dep_PoS in ['NN',
                                                                       'NNS'] and gov.lower() in new_lexicon and lemmatizer.lemmatize(
                dep).lower() in new_data_list:  # 名词主语 ('support', 'VBP') nsubj ('experiments', 'NNS')
            #             print(1,(gov, gov_PoS), dependency, (dep, dep_PoS))
            opinion_to_aspect.append((gov, dependency, dep, sentence))
        elif dependency == 'nsubj' and gov_PoS == ['VBP', 'VBZ', 'VB', 'VBG'] and dep_PoS in ['NN',
                                                                                              'NNS'] and gov.lower() in new_lexicon and lemmatizer.lemmatize(
                dep).lower() in new_data_list:  # ('weak', 'JJ') nsubj ('contribution', 'NN'）
            #             print(2,(gov, gov_PoS), dependency, (dep, dep_PoS))
            opinion_to_aspect.append((gov, dependency, dep, sentence))
        elif dependency == 'nsubj' and dep_PoS in ['NN', 'NNS'] and gov_PoS in ['VBP', 'VBZ',
                                                                                'VB'] and lemmatizer.lemmatize(
                dep).lower() in new_data_list:  # 主语，系动词，结合找到属性词——情感词组合
            for (gov1, gov_PoS1), dependency1, (dep1, dep_PoS1) in sentence_parse.triples():
                if dependency1 == 'xcomp' and dep_PoS1 in ['JJ'] and dep1.lower() in new_lexicon:
                    #                     print(8,(dep1, dep_PoS1),(dependency,dependency1),(dep, dep_PoS))
                    opinion_to_aspect.append((dep1, dependency, dep, sentence))
        elif dependency == 'nsubj' and gov_PoS in ['VBP', 'VBZ', 'VB', 'JJ'] and dep_PoS in [
            'PRP'] and gov.lower() in new_lexicon:  # ('hate', 'VBP') nsubj ('I', 'PRP') ; ('nice', 'JJ') nsubj ('it', 'PRP')
            aspects = [i for i, x in enumerate(sentence_list) if x in new_data_list]
            for aspect in aspects:
                opinion_to_aspect.append((gov, dependency, sentence_list[aspect], sentence))
            #             print(9,(gov, gov_PoS), dependency, (dep, dep_PoS))
        elif dependency == 'amod' and gov_PoS in ['NN', 'NNS'] and dep_PoS == ['VBP', 'VB', 'VBG',
                                                                               'VBZ'] and lemmatizer.lemmatize(
                gov).lower() in new_data_list and dep.lower() in new_lexicon:  # ('space', 'NN') amod ('continuous', 'JJ')情感词修饰属性词
            #             print(3,(gov, gov_PoS), dependency, (dep, dep_PoS))
            opinion_to_aspect.append((dep, dependency, gov, sentence))
        elif dependency == 'amod' and gov_PoS in ['NN', 'NNS'] and dep_PoS in ['JJ', 'JJS',
                                                                               'JJR'] and lemmatizer.lemmatize(
                gov).lower() in new_data_list and dep.lower() in new_lexicon:  # 名词主语
            #             print(4,(gov, gov_PoS), dependency, (dep, dep_PoS))
            opinion_to_aspect.append((dep, dependency, gov, sentence))
        elif dependency == 'conj' and gov_PoS in ['NN', 'NNS'] and dep_PoS in ['NN', 'NNS'] and lemmatizer.lemmatize(
                gov).lower() in new_data_list and lemmatizer.lemmatize(dep).lower() in new_data_list:  # 连词
            #             print(5,(gov, gov_PoS), dependency, (dep, dep_PoS))
            aspect_to_aspect.append((gov, dependency, dep, sentence))
        elif dependency == 'csubj' and gov_PoS in ['NN', 'NNS'] and dep_PoS in ['VBP', 'VB', 'VBG',
                                                                                'VBZ'] and lemmatizer.lemmatize(
                gov).lower() in new_data_list and dep.lower() in new_lexicon:  # ('discussion', 'NN') csubj ('lacking', 'VBG')
            #             print(6,(gov, gov_PoS), dependency, (dep, dep_PoS))
            opinion_to_aspect.append((dep, dependency, gov, sentence))
        elif dependency == 'obj' and dep_PoS in ['NN', 'NNS'] and gov_PoS in ['VBP', 'VB', 'VBG',
                                                                              'VBZ'] and lemmatizer.lemmatize(
                dep).lower() in new_data_list and gov.lower() in new_lexicon:  # ('invalidate', 'VB') obj ('contributions', 'NNS')
            #             print(7,(gov, gov_PoS), dependency, (dep, dep_PoS))
            opinion_to_aspect.append((gov, dependency, dep, sentence))
        elif dependency == 'xcomp' and gov_PoS in [
            'JJ'] and gov.lower() in new_lexicon:  # 补足句子成分 ('nice', 'JJ') xcomp ('see', 'VB');('easy', 'JJ') xcomp ('read', 'VB')
            #             print(10,(gov, gov_PoS), dependency, (dep, dep_PoS))
            opinion_xcomp_aspect.append((gov, dependency, dep, sentence))
    #     elif dependency == 'cop' and gov_PoS in ['JJ'] and gov.lower() in new_lexicon:  # ('intractable', 'JJ') cop ('be', 'VB')系动词['']
    #         print((gov, gov_PoS), dependency, (dep, dep_PoS))

    return opinion_to_aspect, aspect_to_aspect, opinion_xcomp_aspect


def get_aspect_polarity(opinion_to_aspect, aspect_to_aspect, opinion_xcomp_aspect, sentence_list):  # 获得属性情感
    aspect_polarity = {}
    aspect_sentence_polarity = []
    #     sentence_list = nltk.word_tokenize(sentence)
    #     print(len(sentence_list))
    for oa in opinion_to_aspect:  # 情感——属性词对中，属性词极性与修饰其情感词相同
        sentence_list = nltk.word_tokenize(oa[3])
        #         print((sentence_list))
        #         o_index = [i for i,x in enumerate(sentence_list) if x == oa[0]]
        o_index = [i for i, x in enumerate(sentence_list) if oa[0] in x]
        #         print(oa[0],o_index)
        #         a_index = [i for i,x in enumerate(sentence_list) if x == oa[2]]
        a_index = [i for i, x in enumerate(sentence_list) if oa[2] in x]
        #         print(oa[2],a_index)
        Non = [i for i, x in enumerate(sentence_list[0:o_index[0]]) if x in Negative_words]
        n = len(Non)
        Tran = [x for x in enumerate(sentence_list[o_index[0]:a_index[0]]) if x in tran_lexicon]  # 主张情感词后有转折词，极性相反
        t = len(Tran)
        aspect_polarity[oa[2]] = word_polarity[oa[0]] * (-1) ** n * (-1) ** t
        oa += (aspect_polarity[oa[2]],)
        aspect_sentence_polarity.append(oa)

    for aa in aspect_to_aspect:  # 连词属性词，情感极性相同
        sentence_list = nltk.word_tokenize(aa[3])
        if aa[0] in aspect_polarity.keys():
            aspect_polarity[aa[2]] = aspect_polarity[aa[0]]
        elif aa[2] in aspect_polarity.keys():
            aspect_polarity[aa[0]] = aspect_polarity[aa[2]]
        else:
            aspect_polarity[aa[0]] = 0
            aspect_polarity[aa[2]] = 0
        aa += (aspect_polarity[aa[2]],)
        aspect_sentence_polarity.append(aa)
    #         print(aa)

    for oxa in opinion_xcomp_aspect:  # easy read，属性词与动词情感词极性相同
        sentence_list = nltk.word_tokenize(oxa[3])
        index = [i for i, x in enumerate(sentence_list) if oxa[0] in x]
        Non = [i for i, x in enumerate(sentence_list[0:index[0]]) if x in Negative_words]
        n = len(Non)
        aspect_polarity[oxa[2]] = word_polarity[oxa[0]] * (-1) ** (n)
        oxa += (aspect_polarity[oxa[2]],)
        aspect_sentence_polarity.append(oxa)
    #         print(oxa)

    return aspect_sentence_polarity


def write_new_reviews(file_path, new_reviews_list, aspects):  # 写入抽取出情感词-属性词对的评审句
    workbook = xlsxwriter.Workbook(file_path)
    sheet1 = workbook.add_worksheet('new_reviews')
    n = 0
    for i in range(len(new_reviews_list)):
        if (new_reviews_list[i][2] in aspects) or (lemmatizer.lemmatize(new_reviews_list[i][2]) in aspects):  # 属性词在集合里
            for j in range(len(new_reviews_list[i]) - 1):
                sheet1.write(n, j + 1, new_reviews_list[i][j])
            sheet1.write(n, 0, new_reviews_list[i][-1])
            n += 1
    workbook.close()


def walkFile(root_path):
    files_list = []
    dir_list = []
    for root, dirs, files in os.walk(root_path):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f in files:
            files_list.append(os.path.join(root, f))

        # 遍历所有的文件夹
        for d in dirs:
            dir_list.append(os.path.join(root, d))

    return files_list, dir_list


def read_data(xlsx_path, i):  # 读取同行评审句数据表，获得评审标签

    data_xlsx = xlrd.open_workbook(xlsx_path)
    sheet_name = data_xlsx.sheets()[i]
    data = sheet_name.col_values(0)[0:]

    return data


def get_lex_polarity(new_lexicon):  # 获得情感词典的极性
    polarity = {}
    for word in new_lexicon:
        if word in neg_lexicon:
            polarity[word] = -1
        elif word in neu_lexicon:
            polarity[word] = 0
        else:
            polarity[word] = 1
    return polarity


def get_modal_polarity(sentence, word):
    #     sentence = [sub_sentence for sub_sentence in sentence.split(',') if word in sub_sentence][0]#找到情态动词所在的子句
    sentence_list = nlp1.word_tokenize(sentence)
    aspect_sentence_polarity = []
    aspect_polarity = {}
    opinion_to_aspect = []
    #     [sentence for sentence in ]
    aspects = [x for i, x in enumerate(sentence_list) if lemmatizer.lemmatize(x) in new_data_list]  # 找到句中的属性词
    for aspect in aspects:
        opinion_to_aspect.append((word, 'modal', aspect, sentence))
    #     print(opinion_to_aspect)
    for oa in opinion_to_aspect:
        if 'JJR' in [nlp1.pos_tag(word)[0][1] for word in sentence_list]:  # 情态动词+比较级，负面情感
            aspect_polarity[oa[2]] = -1
            oa += (aspect_polarity[oa[2]],)
            #             print(0)
            aspect_sentence_polarity.append(oa)
        #             print(0,aspect_sentence_polarity)
        elif oa[0] in ['could', 'would'] and (
                set(sentence_list).intersection(set(pos_lexicon)) != set()):  # could,would+正面情感词，负面情感
            aspect_polarity[oa[2]] = -1
            oa += (aspect_polarity[oa[2]],)
            #             print(1,sentence_list,(set(sentence_list).intersection(set(pos_lexicon))))
            aspect_sentence_polarity.append(oa)
        #             print(1,aspect_sentence_polarity)
        elif oa[0] in ['need', 'must', 'have to', 'had better'] and (
                set(sentence_list).intersection(set(Negative_words)) != set()):  # must,need+否定词，正面情感
            aspect_polarity[oa[2]] = 1
            oa += (aspect_polarity[oa[2]],)
            #             print(2)
            aspect_sentence_polarity.append(oa)
        #             print(2,aspect_sentence_polarity)
        elif oa[0] in ['could'] and (
                set(sentence_list).intersection(set(Negative_words)) == set()):  # 1.Can, could，表达完成某件事的能力，正面情感
            aspect_polarity[oa[2]] = 1
            oa += (aspect_polarity[oa[2]],)
            #             print(3)
            aspect_sentence_polarity.append(oa)
        #             print(3,aspect_sentence_polarity)
        else:
            aspect_polarity[oa[2]] = -1
            oa += (aspect_polarity[oa[2]],)
            aspect_sentence_polarity.append(oa)
    #             print(4,aspect_sentence_polarity)
    #             print(4)
    return aspect_sentence_polarity


def get_sentence_polarity(sentence):
    aspect_sentence_polarity_list = []
    #     sentence_list = nlp1.word_tokenize(sentence)#分词
    #     all_sentence = sentence.split(',')#分句
    #     all_sentence = list(sentence)
    #     for sentence in all_sentence:
    sentence_list = nlp1.word_tokenize(sentence)  # 分词
    sentence_list = [lemmatizer.lemmatize(x) for x in sentence_list]
    #     for word in modal:
    #         if word in sentence_list:
    if set(modal).intersection(set(sentence_list)):  # 句中包含情态动词
        for word in list((set(modal).intersection(set(sentence_list)))):
            aspect_sentence_polarity = get_modal_polarity(sentence, word)
            aspect_sentence_polarity_list += aspect_sentence_polarity
    else:
        opinion_to_aspect, aspect_to_aspect, opinion_xcomp_aspect = get_aspect_opinion(sentence)  # 句中不包含情态动词
        aspect_sentence_polarity = get_aspect_polarity(opinion_to_aspect, aspect_to_aspect, opinion_xcomp_aspect,
                                                       sentence_list)
        aspect_sentence_polarity_list += aspect_sentence_polarity

    return aspect_sentence_polarity_list


if __name__ == '__main__':
    aspect_path = r'E:/科研训练/aspect-test/Aspect-cluster.xlsx'.strip('\u202a')  # 属性集
    aspects = read_xlsx(aspect_path, 1)

    file_path1 = 'E:/科研训练/aspect-test/aspect_word.xlsx'.strip('\u202a')
    data_list1 = read_data(file_path1, 0)
    data_list = data_list1
    print('all_aspect', len(data_list))
    #     data_list = data_list1+data_list2+data_list3
    not_Negative_words = ['not only', 'not just', 'not to mention', 'no wonder']
    data_list4 = data_list + not_Negative_words
    new_data_list4 = [data.replace(' ', '_') for data in data_list4]
    new_data_list = [data.replace(' ', '_') for data in data_list]
    modal = ['could', 'would', 'should', 'shell', 'need', 'must', 'have to', 'had to', 'please']
    with open(r'E:\科研训练\lexicon\否定词.txt', 'r', encoding='utf-8')as f:
        Negative_words = f.readlines()
        Negative_words = [word.strip('\n') for word in Negative_words]
        print('Negative_words', len(Negative_words))
    with open(r'E:\科研训练\lexicon\neg_lexicon.txt', 'r', encoding='utf-8')as f:
        neg_lexicon = f.readlines()
        neg_lexicon = [word.strip('\n') for word in neg_lexicon]
        print('neg_lexicon', len(neg_lexicon))
    with open(r'E:\科研训练\lexicon\pos_lexicon.txt', 'r', encoding='utf-8')as f:
        pos_lexicon = f.readlines()
        pos_lexicon = [word.strip('\n') for word in pos_lexicon]
        print('pos_lexicon', len(pos_lexicon))
    with open(r'E:\科研训练\lexicon\neu_lexicon.txt', 'r', encoding='utf-8')as f:
        neu_lexicon = f.readlines()
        neu_lexicon = [word.strip('\n') for word in neu_lexicon]
        print('neu_lexicon', len(neu_lexicon))
    with open(r'E:\科研训练\lexicon\转折词.txt', 'r', encoding='utf-8')as f:
        tran_lexicon = f.readlines()
        tran_lexicon = [word.strip('\n') for word in tran_lexicon]
        print('tran_lexicon', len(tran_lexicon))
    new_lexicon = neg_lexicon + pos_lexicon + neu_lexicon
    print('new_lexicon', len(new_lexicon))
    word_polarity = get_lex_polarity(new_lexicon)

    root_path = r'E:\科研训练\ncomms pr txt round\Round=1\Biological sciences0'
    #     root_path = r'C:\Users\Han Ruxue\Desktop\新建文件夹'
    files_list, dir_list = walkFile(root_path)
    files_list = [path for path in files_list if 'Round' in os.path.basename(path) and 'txt' in path]
    print(len(files_list))
    dep_list = []

    for i in range(len(files_list)):
        if i % 100 == 0:
            print(i, '篇正在抽取中...', len(files_list))
        review_path = files_list[i]
        reviews = clean_text(review_path)
        dep_list = []
        new_sentence_list = get_new_review(reviews, data_list4, new_data_list4)  # 替换连字符
        print(len(new_sentence_list))
        for sentence in new_sentence_list:
            aspect_sentence_polarity = get_sentence_polarity(sentence)
            dep_list += (aspect_sentence_polarity)
        formatList = list(set(dep_list))  # 去掉重复的属性情感元组
        formatList.sort(key=dep_list.index)
        dep_list = formatList
        write_path = review_path.replace('.txt', '.xlsx')
        print(write_path)
        write_new_reviews(write_path, dep_list, aspects)