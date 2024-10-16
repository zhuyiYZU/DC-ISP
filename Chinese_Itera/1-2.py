import os
import time

start_time = time.time()

save_path1 = "hc3_finance_label0.csv"
read_path1 = 'hc3_finance_prelabel0.csv'
f_1 = open(save_path1, 'w', encoding='utf8',errors='ignore')
with open(read_path1, 'r', encoding='utf8',errors='ignore') as f:
    for ii, label in enumerate(f):
        label = int(label)
        label = label + 1
        label = str(label)
        f_1.write('"' + label + '"'+'\n')
    f.close()
f_1.close()

read_path2 = './datasets/TextClassification/hc3_finance/test.csv'
f_2 = open("hc3_finance_test.csv", 'w', encoding='utf8',errors='ignore')
with open(read_path2, 'r', encoding='utf8',errors='ignore') as t:
    for ii, text in enumerate(t):
        text = text.split(',')
        text = ' '.join(text[1:])
        f_2.write(text)
    t.close()
f_2.close()

with open('hc3_finance_label0.csv', 'r', encoding='utf8',errors='ignore') as fa:
    with open('hc3_finance_test.csv', 'r', encoding='utf8',errors='ignore') as fb:
        with open('hc3_finance_pre0.csv', 'w', encoding='utf8',errors='ignore') as fc:
            for line in fa:
                fc.write(line.strip('\r\n'))
                fc.write(',')
                fc.write(fb.readline())
            fc.close()


save_path2 = "hc3_finance_test0.csv"
save_path3 = "hc3_finance_testall.csv"
read_path3 = 'hc3_finance_pre0.csv'

f_w = open(save_path2, 'w', encoding='utf8',errors='ignore')
t_w = open(save_path3, 'w', encoding='utf8',errors='ignore')
with open(read_path3, 'r', encoding='utf8',errors='ignore') as f:
    for ii, text in enumerate(f):
        text = text.split(',')
        label = text[0]
        text = ' '.join(text[1:]).replace('\n', '')
        if label == '"1"':
            with open(read_path2, 'r', encoding='utf8',errors='ignore') as t:
                for jj, text1 in enumerate(t):
                    if ii == jj:
                        text1 = text1.split(',')
                        label1 = text1[0]
                        text1 = ' '.join(text1[1:]).replace('\n', '')
                        t_w.write(label1 + ',' + text1 + '\n')
            f_w.write(label + ',' + text + '\n')

f_w = open(save_path2, 'a', encoding='utf8',errors='ignore')
t_w = open(save_path3, 'a', encoding='utf8',errors='ignore')
with open(read_path3, 'r', encoding='utf8',errors='ignore') as t:
    for ii, text in enumerate(t):
        # print(text)
        text = text.split(',')
        label = text[0]
        text = ' '.join(text[1:]).replace('\n', '')
        if label == '"2"':
            with open(read_path2, 'r', encoding='utf8',errors='ignore') as t:
                for jj, text1 in enumerate(t):
                    if ii == jj:
                        text1 = text1.split(',')
                        label1 = text1[0]
                        text1 = ' '.join(text1[1:]).replace('\n', '')
                        t_w.write(label1 + ',' + text1 + '\n')
            f_w.write(label + ',' + text + '\n')

os.remove("hc3_finance_label0.csv")
os.remove("hc3_finance_test.csv")
os.remove("hc3_finance_pre0.csv")

# 划分数据集hc3_finance（5train，5val）
read_path = 'hc3_finance_test0.csv'
m = 0
n = 0

with open(read_path, 'r', encoding='utf8',errors='ignore') as f:
    for ii, text in enumerate(f):
        text = text.split(',')
        label = text[0]
        if label == '"1"':
            m += 1
        else:
            n += 1
print(m, n)
k = 0
j = m
for i in range(1, 11):
    save_path = "hc3_finance_train" + str(i) + ".csv"
    f_w = open(save_path, 'w', encoding='utf8',errors='ignore')
    print('----------')
    with open(read_path, 'r', encoding='utf8',errors='ignore') as f:
        for ii, text in enumerate(f):
            text = text.split(',')
            label = text[0]
            text = ' '.join(text[1:]).replace('\n', '')
            if k+5 <= m:
                if k <= ii < k+5:    #train1
                    f_w.write(label + ',' + text + '\n')
            elif m-k < 5:
                if k <= ii < m or 0 <= ii < 5-m+k:
                    f_w.write(label + ',' + text + '\n')

            if j+5 <= m+n:
                if j <= ii < j+5:   #train1
                    f_w.write(label + ',' + text + '\n')
            elif m+n-j < 5:
                if j <= ii < m+n or m <= ii < j + 5 - n:
                    f_w.write(label + ',' + text + '\n')
    if k+5 <= m:
        print("train{}:{}-{}".format(i, k, k + 5))
    elif m - k < 5:
        print("train{}:{}-{},{}-{}".format(i, k, m, 0, 5-m+k))

    if j + 5 <= m + n:
        print("train{}:{}-{}".format(i, j, j + 5))
    elif m + n - j < 5:
        print("train{}:{}-{},{}-{}".format(i, j, m + n, m, j + 5 - n))

    k += 5
    if k > m:
        k = k-m
    j += 5
    if j > m+n:
        j = j-n
end_time = time.time()
run_time = end_time - start_time
with open('time.csv', 'a+', encoding='utf8',errors='ignore') as t:
    t.write('hc3_finance, step1-2 runtime: ' + str(run_time) + '\n')


# 1515 2710
# ----------
# train1:0-5
# train1:1515-1715
# ----------
# train2:5-400
# train2:1715-1915
# ----------
# train3:400-600
# train3:1915-2115
# ----------
# train4:600-800
# train4:2115-2315
# ----------
# train5:800-1000
# train5:2315-2515
# ----------
# train6:1000-15
# train6:2515-2715
# ----------
# train7:15-1400
# train7:2715-2915
# ----------
# train8:1400-1515,0-85
# train8:2915-3115
# ----------
# train9:85-285
# train9:3115-3315
# ----------
# train10:285-485
# train10:3315-3515

# 2889 3850
# ----------
# train1:0-5
# train1:2889-3189
# ----------
# train2:5-600
# train2:3189-3489
# ----------
# train3:600-900
# train3:3489-3789
# ----------
# train4:900-1200
# train4:3789-4089
# ----------
# train5:1200-1500
# train5:4089-4389
# ----------
# train6:1500-1800
# train6:4389-4689
# ----------
# train7:1800-2100
# train7:4689-4989
# ----------
# train8:2100-2400
# train8:4989-5289
# ----------
# train9:2400-2700
# train9:5289-5589
# ----------
# train10:2700-2889,0-111
# train10:5589-5889





