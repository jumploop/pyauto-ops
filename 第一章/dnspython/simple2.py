#!/usr/bin/env python
import dns.resolver


def main():
    domain = input('Please input an domain: ')
    MX = dns.resolver.query(domain, 'MX')  # MX记录，邮件交换记录，定义邮件服务器的域名
    for i in MX:
        print('MX preference =', i.preference, 'mail exchanger =', i.exchange)


if __name__ == '__main__':
    main()
# 运行结果如下
# Please input an domain: 163.com
# MX preference = 50 mail exchanger = 163mx00.mxmail.netease.com.
# MX preference = 10 mail exchanger = 163mx01.mxmail.netease.com.
# MX preference = 10 mail exchanger = 163mx03.mxmail.netease.com.
# MX preference = 10 mail exchanger = 163mx02.mxmail.netease.com.
