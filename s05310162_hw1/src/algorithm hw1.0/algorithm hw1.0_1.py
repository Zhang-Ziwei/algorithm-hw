# 作者：张子威
# 完成日期：2019/10/29
# 输入：数组长度，数组内容
# 功能：invertion计算.所有i < j and A[i] > A[j], 的 pair (i, j)个数
# 输出：invertion个数
# merge sort 主程序
def merge_sort(fin, p, r, ans):    # ans = 0 ,用于储存每次合并中大前数与小后数交换次数,
    # 注意如果ans为常数python不会回传值，容易覆盖，这里建立list再累加
    if p < r:
        q = (p+r)//2
        merge_sort(fin, p, q, ans)
        merge_sort(fin, q + 1, r, ans)
        merge(fin, p, q, r, ans)

def merge(fin, p, q, r, ans_m):
    num1 = q - p + 1
    num2 = r - q
    left = [fin[p + i] for i in range(num1)]    # 注意不能-1了，p和i都已经被-1了，range(1)=[0]
    right = [fin[q + j+1] for j in range(num2)]
    left.append(100000)
    right.append(100000)
    i = 0
    j = 0
    count = len(left) - 1
    for k in range(p, r+1):
        if left[i]<=right[j]:
            fin[k]=left[i]
            i = i + 1
            count = count - 1       # 当右节点(靠前)的数合并时(s说明此数相对于没有合并的数较小)，count减小(下一个待合并的数可以形成的pair数-1)
        else:
            fin[k]=right[j]
            j=j+1
            ans_m.append(count)        # 当左节点合并，形成count个pair，count为右节点未合并的数

############
# 主程序
############
# 资料读取
# 注意！！！要运行的话记得改这里的address！！！
f = open("D:\IT\演算法\演算法课\作业\作业1\input_100.txt")
fin = []  # list fin，用于储存待排数据资料
ans = 0
tnum = int(f.readline())  # 按行读取文件内容,第一次需要额外读取
# 建立list
for x in range(tnum):
    fin.append(int(f.readline()))  # 接下来也要逐行读取，知道之后没有数据
f.close()
# print(fin)
ans = []
merge_sort(fin, 0, tnum-1, ans)
print(sum(ans))
# print(fin)