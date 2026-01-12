import torch


# 张量表示一个由数值组成的数组，这个数组可能有多个维度。 
# 具有一个轴的张量对应数学上的向量（vector）； 
# 具有两个轴的张量对应数学上的矩阵（matrix）。

# 创建一个行向量x
x = torch.arange(12)

# 输出行向量内部内容
print(x)

# 访问张量（沿每个轴的长度）的形状 。
print("s.shape="+x.shape)

# 输出张量的元素总数
print(x.numel())

# 改变张量形状，将x变为3x4的矩阵
X = x.reshape(3,4)
print(X)
print(X.shape)