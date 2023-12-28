# 演示多种传参的格式

def user_info(name, age, gender):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")

# 位置参数 - 默认使用格式
user_info('小明', 20, '男')

# 关键字参数
user_info(name='小王', age=11, gender='女')
user_info(age=2, name='小龙', gender='男')

def user_info(*args):
    print(args)
    
user_info('Tom', 19)

# **kwargs，必须为字典类型
def user_info(**kwargs):
    print(kwargs)

user_info(name='tom', age=18, id=110)