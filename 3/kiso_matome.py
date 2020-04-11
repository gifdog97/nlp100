import re
import json

def extract_kiso_jouhou(text):
    kiso_pat = re.compile(r"""
        ^\{\{基礎情報 .*?$  # 基礎情報のスタート行
        (.*?)               # 中身, DOTALL フラグを立てて改行も含める
        ^\}\}$              # 終了
        """, re.MULTILINE + re.VERBOSE + re.DOTALL)

    kiso_text = kiso_pat.search(text).group(1)

    kiso_map_pat = re.compile(r"""
        ^\|     # 先頭文字
        (.*)    # field
        \s=\s   # = のマッチ
        (.*)$   # value
        """, re.MULTILINE + re.VERBOSE)

    kiso_match_list = kiso_map_pat.findall(kiso_text)

    #  強調を表すクオーテーションをナイーブに取り除く
    def remove_enhance(value):
        enhance_pat = re.compile(r"""
            (?:''''')  # ?: でグループから外す
            |
            (?:''')
            |
            (?:'')
            """, re.VERBOSE)
        return enhance_pat.sub('', value)
    
    def remove_file(value):
        file_pat = re.compile(r"""
            \[\[
            (?:File|ファイル):
            (.*)
            \]\]
            """, re.MULTILINE + re.VERBOSE)
        bar_pat = re.compile(r"(.*?)\|.*")
        m = file_pat.search(value)
        if m == None:
            return value
        else:
            m_text = m.group(1)
            m_bar = bar_pat.search(m_text)
            if m_bar == None:
                return m_text
            else:
                return m_bar.group(1)

    def remove_link(value):
        link_pat = re.compile(r"""
            (?:\[\[)
            |
            (?:\]\])
            """, re.VERBOSE)
        return link_pat.sub('', value)

    def remove_others(value):
        lang_pat = re.compile(r"\{\{lang\|(.*)\|(.*)\}\}")
        url_pat = re.compile(r"\[https?:\/\/.*\]")
        tag_pat = re.compile(r"<.*?>")
        value = lang_pat.sub(r"\2", value)
        value = url_pat.sub("", value)
        value = tag_pat.sub("", value)
        return value

    kiso_dict = {}

    for field, value in kiso_match_list:
        value = remove_enhance(value)
        value = remove_file(value)
        value = remove_link(value)
        value = remove_others(value)
        kiso_dict[field] = value

    return kiso_dict

with open("./jawiki-country.json", 'r') as f:
    for line in f:
        json_data = json.loads(line)
        if json_data['title'] == "イギリス":
            uk_text = json_data['text']
            break

kiso_dict = extract_kiso_jouhou(uk_text)

from pprint import pprint
pprint(kiso_dict)

import requests

image_file = kiso_dict["国旗画像"]

S = requests.Session()

URL = "https://www.mediawiki.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop": "url",
    "titles": "File:" + image_file
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

url = DATA['query']['pages'].popitem()[1]['imageinfo'][0]['url']

print(url)
