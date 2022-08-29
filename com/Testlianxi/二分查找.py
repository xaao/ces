# print(a)
# a1=[1,2,3,4,5,6,7,8,8,8,8,1]
# a2=[2,4,1]
# print(set(a1),set(a2))
import json

# c={"name":"tom","age":18,"grade":90.5}
# d='123'
# print(type(d))
# json.dumps(d)
# # c["name"]="tom1"
# print(type(d))
# b = [{1, 2, 3, 4}, {5, 6, 7}]
# print(type(b),len(b),type(b[0]),type(c))
# for i in range(0,len(b)):
#     for j in range(len(b[i])):
#         print(list(b[i])[j],end="\t")

# while(True):
#     a = [1, 9, 2, 89, 45, 87, 44, 33, 22, 11]
#     a.sort(reverse=False)
#     left = 0
#     right = len(a)-1
#     mid = 0
#     Input = int(input("输入判断数值："))
#     while (True):
#         mid=int((left+right)/2)
#         if(a[mid]==Input):
#             print("找到下标：{}".format(mid))
#             break
#         elif(a[mid]>Input):
#             right=mid-1
#         else:
#             left=mid+1
#         if(left>right):
#             print("不存在该下标")
#             break



# 1 导入json模块
import json#(导入模块)
# 2 准备数据
data = [{"name":"孙悟空", "age":600, "address":"花果山"}, {"name":"唐僧", "age":35, "address":"东土大唐"}]#导入数据
print(data)#输出数据
print(type(data))#输出数据类型
# 3 将json对象 转成 字符串 json.dumps(...)
json_str = json.dumps(data, ensure_ascii=False)#将dict类型的数据转成str
print(json_str)#输出str格式的数据
print(type(json_str))#输出类型

# 4 将json格式的字符串 转换成 python对象  json.loads(...)
print("-" * 40)#打印横线
python_obj = json.loads(json_str)#在JSON中读取数据
print(python_obj)#输出数据
print(type(python_obj))#输出数据类型

# print("-" * 40)#打印横线
# python_obj_2 = eval(json_str)#返回字符串json_str的结果
# print(python_obj_2)#输出数据
# print(type(python_obj_2))#输出类型
