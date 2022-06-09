# -*- coding: utf-8 -*-
# @File  : update_data.py
# @Author: AaronJny
# @Date  : 2019/10/29
# @Desc  :
import requests
import settings
from io import StringIO
import pandas as pd

print('开始尝试从 {} 获取最新的双色球数据...'.format(settings.LOTTO_DOWNLOAD_URL))
try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    resp = requests.get(settings.LOTTO_DOWNLOAD_URL, headers=headers)
    if resp.status_code == 200:
        # 解析数据，查看数据集中最新的数据期数
        lines = resp.content.decode('utf-8').split('\n')
        total_list = len(lines) - 2
        last_No = lines[total_list]
        print('获取成功！开始更新文件...')
        col = [
        "no", "date",
        "red_1", "red_2", "red_3", "red_4", "red_5", "red_6",
        "blue",
        #"red_r_1", "red_r_2", "red_r_3", "red_r_4", "red_r_5", "red_r_6"
        ]
        data = pd.read_csv(StringIO(resp.text), usecols=[
                        0, 1, 2, 3, 4, 5, 6, 7, 8 ], sep=" ")
        data.columns = pd.Series(col)
        data.drop(['date'], axis=1, inplace=True)
        data = data.iloc[::-1]
        data.to_csv(settings.DATASET_PATH, header=False, index=False) 

        print('完成！当前最新期数为{}期，请确认期数是否正确！'.format(last_No))
    else:
        raise Exception('获取数据失败！')
except Exception as e:
    print(e)
