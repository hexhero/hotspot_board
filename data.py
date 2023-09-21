#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
数据来源：https://wallstreetcn.com/
格式
[
    ['a','b','c']
]
'''

import requests


def getData():

    url = "https://api-ddc-wscn.awtmt.com/market/real?fields=prod_name%2Cpreclose_px%2Clast_px%2Cpx_change%2Cpx_change_rate%2Cprice_precision&prod_code=000001.SS%2CDXY.OTC%2CUS10YR.OTC%2CUSDCNH.OTC%2C399001.SZ%2C399006.SZ"

    payload = {}
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://wallstreetcn.com',
        'Pragma': 'no-cache',
        'Referer': 'https://wallstreetcn.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    data = data['data']['snapshot']
    print(data)
    rst = [
        [
            'USDCNH',
            str(data['USDCNH.OTC'][2]),
            '/',
            str(data['USDCNH.OTC'][3])
        ],
        [
            'SS',
            str(data['000001.SS'][2]),
            '/',
            str(round(data['000001.SS'][4], 2))
        ]
    ]
    return rst
