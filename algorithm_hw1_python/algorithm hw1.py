import random
# 作者：张子威
# 完成日期：2019/10/29
# 输入：数组长度，数组内容
# 功能：invertion计算.所有i < j and A[i] > A[j], 的 pair (i, j)个数
# 输出：invertion个数
# quick_sort主程序
def quick_sort(fin, fin2, p=0, r=100):
    if p < r:
        q = partition_pro(fin, fin2, p, r)
        quick_sort(fin, fin2, p, q - 1)
        quick_sort(fin, fin2, q + 1, r)

# 排列list使得keyvalue的左侧均为小于keyvalue的值，右侧均为大于
def partition_pro(fin, fin2, p_p, r_p):
    #
    k = random.randint(p_p, r_p)
    exchange(fin, k, r_p)
    exchange(fin2, k, r_p)     # 记录数值位置变化
    key_value = fin[r_p]
    i = p_p - 1
    for j in range(p_p, r_p):   # range(1,11)是跑出1，2，3..10,所以这里不用-1
        if fin[j] <= key_value:
            i = i + 1
            exchange(fin, i, j)
            exchange(fin2, i, j)
    exchange(fin, i + 1, r_p)
    exchange(fin2, i + 1, r_p)
    return i + 1

# 交换一个list中两个数的值
def exchange(fin, p_e, r_e):
    a = fin[p_e]
    fin[p_e] = fin[r_e]
    fin[r_e] = a
############
# 主程序
############
# 资料读取
f = open("D:\IT\演算法\演算法课\作业\作业1\input_100.txt")
fin = []    # list fin，用于储存待排数据资料
fin2 = []   # list fin2，用于储存原资料在list中位置，
ans = 0
tnum = int(f.readline())  # 按行读取文件内容,第一次需要额外读取
# 建立list
for x in range(tnum):
    fin.append(int(f.readline()))  # 接下来也要逐行读取，知道之后没有数据
f.close()
for num in range(tnum):
    fin2.append(num)
    num = num+1
# print(fin)
# print(fin2)
quick_sort(fin, fin2, 0, tnum-1)
# print(fin2)
# print(fin)
# 计算inversion pair的个数
for x in range(tnum):
    if fin2[x] > x:
        ans = ans + fin2[x] - x
print(ans)