#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
数据来源：https://wallstreetcn.com/
'''

import requests

def getAll():
    
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
    return data['000001.SS'], data['USDCNH.OTC']
    


def getUSDCNH():

    url = "https://api-ddc-wscn.awtmt.com/market/kline?prod_code=USDCNH.OTC&tick_count=1&period_type=300&adjust_price_type=forward&fields=tick_at,open_px,close_px,high_px,low_px,turnover_volume,turnover_value,average_px,px_change,px_change_rate,avg_px,ma2"
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
    val = data['data']['candle']['USDCNH.OTC']['lines'][0][1]
    print('USDCNH:', val)
    return val

