#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simplest possible HTTP client."""

import sys

from asyncio import *

# 协程:
@coroutine
def fetch():
    r, w = yield from open_connection('python.org', 80)
    request = 'GET / HTTP/1.0\r\n\r\n'
    print('>', request, file=sys.stderr)
    w.write(request.encode('latin-1'))
    while True:
        line = yield from r.readline()     # 异步返回
        line = line.decode('latin-1').rstrip()
        if not line:
            break
        print('<', line, file=sys.stderr)
    print(file=sys.stderr)
    body = yield from r.read()             # 异步返回
    return body


#########################################
#             主函数
#
#########################################
def main():
    loop = get_event_loop()    # 事件循环
    try:
        body = loop.run_until_complete(fetch())
    finally:
        loop.close()
    print(body.decode('latin-1'), end='')


if __name__ == '__main__':
    main()
