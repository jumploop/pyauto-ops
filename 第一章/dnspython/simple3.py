#!/usr/bin/env python
import dns.resolver


def main():
    domain = input('Please input an domain: ')
    ns = dns.resolver.query(domain, 'NS')  # NS记录，标记区域的域名服务器及授权子域
    for i in ns.response.answer:
        for j in i.items:
            print(j.to_text())


if __name__ == '__main__':
    main()

# 运行结果如下
# Please input an domain: baidu.com
# dns.baidu.com.
# ns4.baidu.com.
# ns3.baidu.com.
# ns7.baidu.com.
# ns2.baidu.com.
