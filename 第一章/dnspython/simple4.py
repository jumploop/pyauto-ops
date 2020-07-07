#!/usr/bin/env python
import dns.resolver


def main():
    domain = input('Please input an domain: ')
    cname = dns.resolver.query(domain, 'CNAME')  # CNAME记录，指别名记录，实现域名间的映射
    for i in cname.response.answer:
        for j in i.items:
            print(j.to_text())


if __name__ == '__main__':
    main()
# 运行结果如下
# Please input an domain: www.baidu.com
# www.a.shifen.com.
