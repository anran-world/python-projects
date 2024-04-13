import os
import utils as u


def main():
    # 记录开始时间
    t0 = u.mark()
    directory_path = os.getcwd() + '/../../data'

    # text = ''.join(u.read_file_lines(file_path))
    text = u.read_files(directory_path)
    print('文字长度：', len(text))

    # 记录读取时间
    t1 = u.mark()
    read_time = t1 - t0
    print(f"文件读取：{round(read_time, 5)} 秒")

    remove_list = [
        '哈',
        '好好好',
        '?',
        '阿弥陀佛善哉善哉',
        '为什么没人找我搭建啊',
    ]
    split_worlds = u.split(text, remove_list, 3)

    wordcloud = u.draw_world_cloud(split_worlds)

    t2 = u.mark()
    execution_time = t2 - t1
    print(f"生成词云：{round(execution_time, 5)} 秒")

    total_time = t2 - t0
    print(f"总耗时：{round(total_time, 5)} 秒")

    u.show_picture(wordcloud)


if __name__ == '__main__':
    main()
