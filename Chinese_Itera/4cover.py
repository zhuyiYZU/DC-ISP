import time
import os
start_time = time.time()


itera = 10   # g
# 调整位置后数据
f_1 = open("hc3_finance_test.csv", 'w', encoding='gbk',errors='ignore')
with open('hc3_finance_testall.csv', 'r', encoding='gbk',errors='ignore') as t:
    for ii, text in enumerate(t):
        text = text.split(',')
        text = ' '.join(text[1:])
        f_1.write(text)
t.close()
f_1.close()



for i in range(1, itera+1):
    read_path = "hc3_finance_prelabel" + str(i) + ".csv"
    save_path = "hc3_finance_prelabel_" + str(i) + ".csv"

    f_3 = open(save_path, 'w', encoding='gbk',errors='ignore')
    with open(read_path, 'r', encoding='gbk',errors='ignore') as f:
        for ii, label1 in enumerate(f):
            label1 = int(label1)
            if label1 == 0:
                f_3.write("-1" + '\n')
            else:
                label1 = str(label1)
                f_3.write(label1 + '\n')
    f.close()
    f_3.close()

# 先将0改为-1，用0覆盖训练集
read_path1 = 'hc3_finance_test0.csv'
m = 0
n = 0
with open(read_path1, 'r', encoding='gbk',errors='ignore') as f:
    for ii, text in enumerate(f):
        text = text.split(',')
        label1 = text[0]
        if label1 == '"1"':
            m += 1
        else:
            n += 1
print(m, n)
k = 0
j = m
for i in range(1, itera + 1):
    save_path = "hc3_finance_label" + str(i) + ".csv"
    f_2 = open(save_path, 'w', encoding='gbk')
    read_path2 = "hc3_finance_prelabel_" + str(i) + ".csv"
    print('-----------')
    with open(read_path2, 'r', encoding='gbk',errors='ignore') as f:
        for ii, label in enumerate(f):
            label = int(label)
            if k+5 <= m:
                if k <= ii < k+5:    #train1
                    pass
            elif m-k < 5:
                if k <= ii < m or 0 <= ii < 5-m+k:
                    pass

            if j+5 <= m+n:
                if j <= ii < j+5:   #train1
                    pass
            elif m+n-j < 5:
                if j <= ii < m+n or m <= ii < j + 5 - n:
                    pass
    if k+5 <= m:
        print("train{}:{}-{} ".format(i, k, k + 5))
        with open(read_path2, 'r', encoding='gbk',errors='ignore') as f:
            for ii, label in enumerate(f):
                if ii < m:
                    label = int(label)
                    if k <= ii < k+5:
                        if label == 1 or label == -1:
                            f_2.write("0" + '\n')
                    else:
                        label = str(label)
                        f_2.write(label + '\n')
    elif m - k < 5:
        print("train{}:{}-{},{}-{}".format(i, k, m, 0, 5-m+k))
        with open(read_path2, 'r', encoding='gbk',errors='ignore') as f:
            for ii, label in enumerate(f):
                if ii < m:
                    label = int(label)
                    if k <= ii < m or 0 <= ii < 5-m+k:
                        if label == 1 or label == -1:
                            f_2.write("0" + '\n')
                    else:
                        label = str(label)
                        f_2.write(label + '\n')

    if j + 5 <= m + n:
        print("train{}:{}-{}".format(i, j, j + 5))
        with open(read_path2, 'r', encoding='gbk',errors='ignore') as f:
            for ii, label in enumerate(f):
                if ii >= m:
                    label = int(label)
                    if j <= ii < j+5:
                        if label == 1 or label == -1:
                            f_2.write("0" + '\n')
                    else:
                        label = str(label)
                        f_2.write(label + '\n')
    elif m + n - j < 5:
        print("train{}:{}-{},{}-{}".format(i, j, m + n, m, j + 5 - n))
        with open(read_path2, 'r', encoding='gbk',errors='ignore') as f:
            for ii, label in enumerate(f):
                if ii >= m:
                    label = int(label)
                    if j <= ii < m+n or m <= ii < j+5-n:
                        if label == 1 or label == -1:
                            f_2.write("0" + '\n')
                    else:
                        label = str(label)
                        f_2.write(label + '\n')
    k += 5
    if k > m:
        k = k-m
    j += 5
    if j > m+n:
        j = j-n

for i in range(1, itera + 1):
    os.remove("hc3_finance_prelabel_" + str(i) + ".csv")

end_time = time.time()
run_time = end_time - start_time
with open('time.csv', 'a+', encoding='gbk',errors='ignore') as t:
    t.write('hc3_finance, step4 runtime: ' + str(run_time) + '\n')

