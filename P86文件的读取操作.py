# 打开文件
import time


f = open("H:/03Python/01学习笔记/P86文件的读取操作.txt","r",encoding="UTF-8")
print(type(f))
# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取文件的结果：{f.read()}")
print("-------------------------------")
# 读取文件 - readLines()
# lines = f.readlines()
# print(f"lines对象类型是：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"line对象类型是：{type(line1)}")
# print(f"line1对象的内容是：{line1}")
# print(f"line2对象的内容是：{line2}")
# print(f"line3对象的内容是：{line3}")

# for循环读取文件行
# for line in f:
#     print(f"每一行数据是：{line}")

# 文件的关闭
# f.close()
# with.open 语法操作文件
with open("H:/03Python/01学习笔记/P86文件的读取操作.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")

time.sleep(50000)