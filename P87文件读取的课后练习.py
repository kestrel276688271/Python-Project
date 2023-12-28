# 打开文件，以读取模式打开
f = open("H:/03Python/01学习笔记/P87文件读取的课后练习.txt","r",encoding="UTF-8")
# 方式1，读取全部内容，通过字符count方式统计itheima单词数量
# content = f.read()
# count = content.count("itheima")
# print(f"itheima在文件中出现了：{count}次")

# 方式2，读取内容，一行一行读数
count = 0   # 变量统计
for line in f:
    line = line.strip() # 去除开头和结尾的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1  # 出现一次+1
# 判断单词出现次数并统计
print(f"itheima出现的次数是：{count}")
