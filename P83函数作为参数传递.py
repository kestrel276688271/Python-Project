def test_func(compute):
    result = compute(1, 2)
    print(f"compute参数的类型是：{type(compute)}")
    print(f"计算结果是：{result}")

# 定义一个函数，准备作为参数传入另一个函数
def compute(x, y):
    return x + y

# 调用，并传入函数
test_func(compute)
