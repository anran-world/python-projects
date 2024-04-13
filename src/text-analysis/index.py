import os
import utils as u
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def main():
    # 记录开始时间
    t0 = time.time()
    directory_path = os.getcwd() + '/../../data'

    # text = ''.join(u.read_file_lines(file_path))
    text = u.read_files(directory_path)
    print(len(text))

    # 记录读取时间
    t1 = time.time()
    read_time = t1 - t0
    print(f"文件读取：{read_time} 秒")

    # 创建词云对象
    wordcloud = WordCloud(font_path="msyh.ttc", width=1920, height=1080, background_color='white').generate(text)
    print()

    t2 = time.time()
    execution_time = t2 - t1
    print(f"生成词云：{execution_time} 秒")
    u.re()

    # 显示词云图像
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    total_time = t2 - t0
    print(f"总耗时：{total_time} 秒")


if __name__ == '__main__':
    main()
