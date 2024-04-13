import sys
import os


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_file_by_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


def read_file_lines(file_path):
    text_lines = []
    num = 0
    for line in read_file_by_line(file_path):
        num = num + 1
        print('读取第', num, '行中...')
        text_lines.append(line)
    return text_lines


def read_files(directory_path):
    words = []

    # 使用 os.walk() 遍历文件夹
    for root, dirs, files in os.walk(directory_path):
        print(root, dirs, files)
        for file in files:
            # 检查文件扩展名是否为 .txt
            if file.endswith(".txt"):
                # 如果是，将文件路径添加到列表中
                words.append(read_file(os.path.join(root, file)))
    return ''.join(words)


def re():
    # 执行一些操作
    print("人为终止")

    # 终止程序的执行
    sys.exit()


def main():
    print(__name__)


if __name__ == '__main__':
    main()
