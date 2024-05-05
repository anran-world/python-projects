import os, sys, re
from datetime import datetime, timezone, timedelta

IP_PATTERN = r'(?:\d{1,3}\.){3}\d{1,3}'
TIME_PATTERN = r'(?<=\[).*0800'
URL_PATTERN = r'(?:GET|POST|PUT|DELETE|HEAD|PATCH|OPTIONS) \S+'
PROTOCOL_PATTERN = r'HTTP[^"]*'
STATUS_PATTERN = r'\d{3} \d+'
REFER_PATTERN = r'https?://[^"]+'
UA_PATTERN = r'(?<=")[A-Z][a-z].*(?=")'


def read_file(path='/static/log'):
    abs_path = os.getcwd() + path
    contents = os.listdir(abs_path)
    all_list = []

    for filename in contents:
        file_path = os.path.join(abs_path, filename)
        if os.path.isfile(file_path):
            time = os.path.getmtime(file_path)
            print(1, time)
            # 获取当前时间
            current_time = datetime.now().timestamp()
            print('current_time', filename, current_time)
            continue
            if filename.endswith('error.log'):
                # 错误日志的处理
                print('[错误 filename] -> ', filename)
            else:
                # 普通日志的处理
                with open(file_path, 'r') as f:
                    for line in f:
                        # 处理行
                        all_list.append(split_line(line))
    return all_list

    # print("Current Time:", current_time)


def split_line(
        str='162.158.86.104 - - [25/Apr/2024:12:39:38 +0800] "GET /favicon.ico HTTP/2.0" 404 548 "https://jx.3kla.top/" "Mozilla/5.0 (Linux; U; Android 10; zh-Hans-CN; ELE-AL00 Build/HUAWEIELE-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Quark/6.11.6.541 Mobile Safari/537.36"'):
    res = str.split('"')
    if (len(res) == 7):
        method_url = get_val(re.search(URL_PATTERN, str)).split()
        status_length = get_val(re.search(STATUS_PATTERN, str)).split()
        print(111, status_length, len(status_length))
        obj = {
            'ip': get_val(re.search(IP_PATTERN, str)),
            'time': get_time(re.search(TIME_PATTERN, str)),
            'method': method_url[0] if len(method_url) == 2 else '',
            'url': method_url[1] if len(method_url) == 2 else '',
            'protocol': get_val(re.search(PROTOCOL_PATTERN, str)),
            'status': status_length[0] if len(status_length) == 2 else '',
            'length': status_length[1] if len(status_length) == 2 else '',
            'refere': get_val(re.search(REFER_PATTERN, str)),
            'ua': get_val(re.search(UA_PATTERN, str)),
        }
        for a, b in enumerate(obj):
            print(a, b, obj[b])
        return obj
    else:
        return {}


def get_time(str_time):
    print('str_time', str_time)
    if str_time:
        # 将字符串转换为时间对象
        dt = datetime.strptime(str_time.group(), '%d/%b/%Y:%H:%M:%S %z')
        # 获取 UTC 时间
        utc_time = dt.astimezone(timezone.utc)
        # 将时间对象转换为时间戳
        return int(utc_time.timestamp())
    else:
        return 'null'


def get_val(re_result):
    return re_result.group() if re_result else ''


if __name__ == '__main__':
    read_file()
