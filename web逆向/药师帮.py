import gzip
import time
import zlib

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import time
def getEx1(ts):
    array1 = [9,5,2,7]
    array2 = [int(char) for char in ts]
    num1 = 7*sum(i for i in array2)%10
    len_array1 = len(array1)
    len_array2 = len(array2)
    array3 = []
    for i, value_b in enumerate(array2):
        index_a = i % len_array1  # Calculate the index for array a using modulus
        array3.append((array1[index_a]+value_b)%10)
    array4 = array3[-1*((len_array1%len_array2)):]
    array5 = array3[:-1*((len_array1%len_array2))]
    array4.reverse()
    array5.reverse()
    array4.append(num1)
    totalArray = array4+array5
    print(array1)
    print(array2)
    print(array3)
    print(array4)
    print(array5)
    print(totalArray)
    p = int(''.join(map(str, totalArray)))
    print(p)
    newArray = []
    strmap = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z"
    ]

    while p:
        tmp = p%36
        print(tmp)
        newArray.append(strmap[tmp])
        p = int(p /36)
    newArray.reverse()
    return "".join(map(str, newArray))
def inflate_bytes(data):
    return zlib.decompress(data)
# AES加密函数
def aes_ecb_encrypt(key, plaintext):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size, style='pkcs7')
    ciphertext = cipher.encrypt(padded_plaintext)
    return base64.b64encode(ciphertext).decode('utf-8')
def aes_ecb_decrypt(key, ciphertext):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext)
    decrypted_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_text, AES.block_size,style='pkcs7')
    return gzip.decompress(plaintext).decode()


url = "https://dian.ysbang.cn/wholesale-drug/sales/getWholesaleList/v4270"
ts = str(int((time.time())*1000))
ex1 = getEx1(ts)
print(ts)
key = "1AA00F7BB06A4E25"
# 进行加密
oParams = aes_ecb_encrypt(key, ts)
print("加密后的结果:", oParams)
payload = {
    "platform": "pc",
    "version": "5.37.0",
    "ua": "Chrome126",
    "ex": "2024-7-4 20:17 supplierstore 07-11 06:29:58 07-11 06:29:58",
    "trafficType": 4,
    "ex1": ex1,
    "o": oParams,
    "page": 1,
    "pagesize": 60,
    "operationtype": 2,
    "provider_id": 3178,
    "mustStockAvailable": 0,
    "sort": "默认",
    "tagId": "",
    "searchkey": "",
    "elevatedId": 26809311,
    "factoryNames": "",
    "saleTypes": [],
    "activityTypes": [],
    "specs": "[]",
    "needCancel": True,
    "token": "75c63111cdab40278b05e4085170cbc3"
}
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sentry-trace": "7c1e81fe11bb4bc3a4ac57371bdf7ec3-8491bffea72a8c3a-1",
    "cookie": "__snaker__id=NmyyBWmd2MCETvAJ; Token=75c63111cdab40278b05e4085170cbc3; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22887618%22%2C%22first_id%22%3A%221909c89a70a708-052a23d1a566308-26001f51-3686400-1909c89a70bbb5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwOWM4OWE3MGE3MDgtMDUyYTIzZDFhNTY2MzA4LTI2MDAxZjUxLTM2ODY0MDAtMTkwOWM4OWE3MGJiYjUiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI4ODc2MTgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22887618%22%7D%7D; gdxidpyhxdE=7Cl4%2BgVVjWfySSyD4WAfJQBB3UGZxAwcLjsa%5C8Jd9mz49Pipusjn3k0GWZXh%2B9rEeinShqTHLb7NkAAUY6wV2HL9qdesw5d8whYymRDLao%2B5IgN2gK1diLR2w0%5CayElZR%2BUC1tgDqv6%2B9RwNmHD16lIHYCTDAbyL0zIhrc0m%2FvhqMygC%3A1720615944039",
    "Referer": "https://dian.ysbang.cn/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
    "Connection": "keep-alive"
}

response = requests.request("POST", url, json=payload, headers=headers).json()

oReturn = response['data']['o']
print(oReturn)
result = aes_ecb_decrypt("69091A0C978D8060",oReturn)
print(result)
# 要加密的明文和秘钥
