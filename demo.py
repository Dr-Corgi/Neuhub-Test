# -*- coding:utf-8 -*-
"""
Created on 18/6/28 下午3:17.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

import requests

type = 3 # 1:{正面/负面} 3:{其他/愤怒/快乐/失落/焦虑/难过/害怕}
text = "物流也很快服务也很好"

url_ = 'http://ai-api.jd.com/nlp/sentiment?token=35f48390-b7f7-4e2f-b823-87e99b74a86f&type='+str(type)+'&text='+text
r = requests.get(url_)
print(r.text)
