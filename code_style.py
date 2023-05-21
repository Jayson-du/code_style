# -*- coding=utf_8 -*-
import os

path = "E:\\JaysonCode\\llvm_practice"

filelist = []
filetype = set()

keywords = set()

def init_file_type():
    filetype.add("cpp")
    filetype.add("txt")
    filetype.add("c")
    filetype.add("cc")
    filetype.add("py")

def init_keywords():
    keywords.add("do")
    keywords.add("while")
    keywords.add("if")
    keywords.add("else if")
    keywords.add("else")



def get_all_file(path, filelist):
    '''
    获取path目录下所有文件, 拼接成绝对路径, 存入files
    '''
    file_or_dir = os.listdir(path)

    for file_dir in file_or_dir:
        file_or_dir_path = os.path.join(path, file_dir)

        # 判断file_or_dir_path是否是路径, 如果是路径, 则递归调用get_all_file
        if os.path.isdir(file_or_dir_path):
            get_all_file(file_or_dir_path)

        else:
            # 判断是否是指定类型的文件, 如果是指定类型的文件, 则存入filelist中
            if os.path.splitext(file_or_dir_path)[-1][1:] in filetype:
                filelist.append(file_or_dir_path)


def match_keywords(line):

    for keyword in keywords:
        if line.find(keyword) != -1:
            print()

def read_file(file):
    '''
    根据传递的file, 逐行读取file中的内容, 然后按照关键字进行判断
    '''
    fp = open(file, mode = 'r')

    # 读取每行
    line = fp.readline()

    match_keywords(line)

    fp.close()

def main():
    get_all_file(path)




if __name__ == "__main__":
    init_file_type()

    init_keywords()

    main()
