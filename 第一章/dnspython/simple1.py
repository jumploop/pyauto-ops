#!/usr/bin/env python
import dns.resolver


def main():
    domain = input('Please input an domain: ')
    A = dns.resolver.query(domain, 'A')  # A记录，将主机名转换成IP地址
    for i in A.response.answer:
        for j in i.items:
            print(j.address)


if __name__ == '__main__':
    main()

# 运行结果如下
# Please input an domain: www.google.com
# 69.63.186.30
