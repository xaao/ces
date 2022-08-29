# def Sum(a=1,b=0):
#     try:
#         c=a/b
#     except Exception as e:
#         print(e)
#     else:
#         print(12)
#     finally:
#         print("是否出错误我都执行")
#     # assert (a+b)==2
#         print(1)
#     # except Exception as e:
#     #     print(e)
#     # else:
#     #     print("执行出错")
#     #     print("-----")
# Sum()
import json

import requests
reponse=requests.get(url="http://192.168.6.227:5000/v2/_catalog").json()
# reponsejson=json.loads(reponse)
print(reponse)
print(reponse['repositories'][0])
print(type(reponse))
# print(reponsejson.repositories)