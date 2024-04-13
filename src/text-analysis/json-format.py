import json


def main():
    input_file_path = '../../data/result.json'
    output_file_path = '../../data/result.txt'

    with open(input_file_path, 'r', encoding='utf-8') as f:
        data_from_file = json.load(f)

    arr = []
    if isinstance(data_from_file['messages'], list) and len(data_from_file['messages']) > 0:
        for message in data_from_file['messages']:
            for key, value in message.items():
                if key in ['text'] and isinstance(value, str):
                    arr.append(value)
        text = ' '.join(arr)
        # 使用空格分割文本，并统计每个单词的出现次数
        word_count = {}
        for word in text.split():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # 对统计结果进行排序，按照单词出现的次数降序排列
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=False)

        # 输出排序后的结果
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(text)


if __name__ == '__main__':
    main()
