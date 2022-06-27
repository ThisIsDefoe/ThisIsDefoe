# (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
# урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# ) для получения информации вида: (<remote_addr>, <request_datetime>,
# <request_type>, <requested_resource>, <response_code>, <response_size>)
# 93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3
# (0.8.16~exp12ubuntu10.21)"

import re

RE_DATA_LOG = re.compile(r'^((?:\d+\.){3}\d+)[ -]*\[([^\[\]]*)\]\s*\"([\w]*)\s*([^\"]*)\s[^\"]*\"\s*(\d+)\s(\d+)')


def parse_log(log_str):
    result = RE_DATA_LOG.findall(log_str)
    if result:
        return result[0]


with open('nginx_logs.txt') as log_file:
    for _ in range(50):
        line = log_file.readline()
        print(parse_log(line))