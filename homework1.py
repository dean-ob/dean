import pandas as pd
import numpy as np
import xlwt
import csv

traindata = pd.read_csv('E:/pycharm 2020.1.5\pattern recognition/train.csv')
testdata = pd.read_csv('E:/pycharm 2020.1.5\pattern recognition/test.csv')
data = pd.read_csv('E:/pycharm 2020.1.5\pattern recognition/gender_submission.csv')
sex = traindata[['Sex','Survived']]
pclass = traindata[['Pclass','Survived']]
age = traindata[['Age','Survived']]
num = traindata[['Cabin','Survived']]

#性别
x1 = traindata[traindata['Sex'].isin(['male'])]
x2 = traindata[traindata['Sex'].isin(['female'])]
man = len(x1)
woman = len(x2)
all = man + woman
mans = 0;womans = 0
i = 0;S = 0
while i < all:
    if sex['Sex'][i] == 'male':
        if int(sex['Survived'][i]) == 1:
            mans = mans + 1
    else:
        if int(sex['Survived'][i]) == 1:
            womans = womans + 1
    if int(sex['Survived'][i]) == 1:
        S = S + 1
    i = i + 1
PS = (mans + womans)/all
S1 = mans/(mans + womans)
S2 = womans/(mans + womans)
S11 = (man - mans)/(all - mans - womans)
S22 = (woman - womans)/(all - mans - womans)

#客舱等级
i = 0;pclass1 = 0;pclass2 = 0;pclass3 = 0
while i < all:
    if int(pclass['Pclass'][i]) == 1:
        pclass1 = pclass1 + 1
    elif int(pclass['Pclass'][i]) == 2:
        pclass2 = pclass2 + 1
    else:
        pclass3 = pclass3 + 1
    i = i + 1
i = 0;pclass1S = 0;pclass2S = 0;pclass3S = 0
while i < all:
    if int(pclass['Pclass'][i]) == 1:
        if int(pclass['Survived'][i]) == 1:
            pclass1S = pclass1S + 1
    elif int(pclass['Pclass'][i]) == 2:
        if int(pclass['Survived'][i]) == 1:
            pclass2S = pclass2S + 1
    elif int(pclass['Pclass'][i]) == 3:
        if int(pclass['Survived'][i]) == 1:
            pclass3S = pclass3S + 1
    i = i + 1
P1 = pclass1S/(pclass1S + pclass2S + pclass3S)
P2 = pclass2S/(pclass1S + pclass2S + pclass3S)
P3 = pclass3S/(pclass1S + pclass2S + pclass3S)
P11 = (pclass1 - pclass1S)/(all - pclass1S - pclass2S - pclass3S)
P22 = (pclass2 - pclass2S)/(all - pclass1S - pclass2S - pclass3S)
P33 = (pclass3 - pclass3S)/(all - pclass1S - pclass2S - pclass3S)

#年龄
i = 0;sum = 0
all1 = all
while i < all:
    if pd.isnull(age['Age'][i]):#判断是否为空
        all1 = all1 - 1
    else:
        sum = sum + age['Age'][i]
    i = i + 1
a1 = sum/all1
if a1 < 15:
    a1 = 'young'
elif 15 <= a1 < 55:
    a1 = 'middle'
else:
    a1 = 'old'

age1 = {}
i = 0;young = 0;middle = 0;old = 0
while i < all:
    if float(age['Age'][i]) < 15:
        age1[i] = 'young'
        young = young + 1
    elif 15 <= float(age['Age'][i]) < 55:
        age1[i] = 'middle'
        middle = middle + 1
    elif float(age['Age'][i]) >= 55:
        age1[i] = 'old'
        old = old + 1
    elif pd.isnull(age['Age'][i]):
        age1[i] = a1
        if a1 == 'young':
            young = young + 1
        elif a1 == 'middle':
            middle = middle + 1
        else:
            old = old + 1
    i = i + 1
i = 0;youngs = 0;middles = 0;olds = 0
while i < all:
    if age1[i] == 'young':
        if int(age['Survived'][i]) == 1:
            youngs = youngs + 1
    elif age1[i] == 'middle':
        if int(age['Survived'][i]) == 1:
            middles = middles + 1
    else:
        if int(age['Survived'][i]) == 1:
            olds = olds + 1
    i = i + 1
A1 = youngs/(youngs + middles + olds)
A2 = middles/(youngs + middles + olds)
A3 = olds/(youngs + middles + olds)
A11 = (young - youngs)/(all - youngs - middles - olds)
A22 = (middle - middles)/(all - youngs - middles - olds)
A33 = (old - olds)/(all - youngs - middles - olds)
'''
#客舱号
i = 0;S1 = 0;S2 = 0
number = {}
while i < all:#判断有无客舱号
    if pd.isnull(num['Cabin'][i]):
        number[i] = 0
        S2 = S2 + 1
    else:
        number[i] = 1
        S1 = S1 + 1
    i = i + 1
i = 0;S1S = 0;S2S = 0
while i < all:
    if number[i] == 1:
        if num['Survived'][i] == 1:
            S1S = S1S + 1
    else:
        if num['Survived'][i] == 1:
            S2S = S2S + 1
    i = i + 1
N1 = S1S/S1
N2 = S2S/S2
'''

survive = {}
i = 0
while i < all:
    if sex['Sex'][i] == 'male':
        if int(pclass['Pclass'][i]) == 1:
            if age1[i] == 'young':
                p1 = PS*S1*P1*A1
                p2 = (1-PS)*S11*P11*A11
            elif age1[i] == 'middle':
                p1 = PS*S1*P1*A2
                p2 = (1-PS)*S11*P11*A22
            else:
                p1 = PS*S1*P1*A3
                p2 = (1-PS)*S11*P11*A33
        elif int(pclass['Pclass'][i]) == 2:
            if age1[i] == 'young':
                p1 = PS*S1*P2*A1
                p2 = (1-PS)*S11*P22*A11
            elif age1[i] == 'middle':
                p1 = PS*S1*P2*A2
                p2 = (1-PS)*S11*P22*A22
            else:
                p1 = PS*S1*P2*A3
                p2 = (1-PS)*S11*P22*A33
        else:
            if age1[i] == 'young':
                p1 = PS*S1*P3*A1
                p2 = (1-PS)*S11*P33*A11
            elif age1[i] == 'middle':
                p1 = PS*S1*P3*A2
                p2 = (1-PS)*S11*P33*A22
            else:
                p1 = PS*S1*P3*A3
                p2 = (1-PS)*S11*P33*A33
    else:
        if int(pclass['Pclass'][i]) == 1:
            if age1[i] == 'young':
                p1 = PS*S2 * P1 * A1
                p2 = (1-PS)*S22*P11*A11
            elif age1[i] == 'middle':
                p1 = PS*S2 * P1 * A2
                p2 = (1-PS)*S22*P11*A22
            else:
                p1 = PS*S2 * P1 * A3
                p2 = (1-PS)*S22*P11*A33
        elif int(pclass['Pclass'][i]) == 2:
            if age1[i] == 'young':
                p1 = PS*S2 * P2 * A1
                p2 = (1-PS)*S22*P22*A11
            elif age1[i] == 'middle':
                p1 = PS*S2 * P2 * A2
                p2 = (1-PS)*S22*P22*A22
            else:
                p1 = PS*S2 * P2 * A3
                p2 = (1-PS)*S22*P22*A33
        else:
            if age1[i] == 'young':
                p1 = PS*S2 * P3 * A1
                p2 = (1-PS)*S22*P33*A11
            elif age1[i] == 'middle':
                p1 = PS*S2 * P3 * A2
                p2 = (1-PS)*S22*P33*A22
            else:
                p1 = PS*S2 * P3 * A3
                p2 = (1-PS)*S22*P33*A33
    if p1 > p2:
        survive[i] = 1
    else:
        survive[i] = 0
    i = i + 1
#计算准确率
TP = 0;TN = 0;FP = 0;FN = 0
i = 0
while i < all:
    if survive[i] == int(traindata['Survived'][i]):
        if survive[i] == 1:
            TP = TP + 1
        else:
            TN = TN + 1
    else:
        if survive[i] == 1:
            FP = FP + 1
        else:
            FN = FN + 1
    i = i + 1
Accuracy_train = (TP + TN)/(TP + TN + FP + FN)
print('Accuracy =',Accuracy_train)

#测试集
res = testdata.shape[0]
i = 0;sum = 0
res1 = res
while i < res:
    if pd.isnull(testdata['Age'][i]):#判断是否为空
        res1 = res1 - 1
    else:
        sum = sum + testdata['Age'][i]
    i = i + 1
a1 = sum/all1
if a1 < 15:
    a1 = 'young'
elif 15 <= a1 < 55:
    a1 = 'middle'
else:
    a1 = 'old'
age2 = {}
i = 0
while i < res:
    if float(age['Age'][i]) < 15:
        age2[i] = 'young'
    elif 15 <= float(age['Age'][i]) < 55:
        age2[i] = 'middle'
    elif float(age['Age'][i]) >= 55:
        age2[i] = 'old'
    elif pd.isnull(age['Age'][i]):
        age2[i] = a1
    i = i + 1
survive1 = testdata[['PassengerId','Sex']]
survive1 = survive1.to_dict(orient = 'records')
i = 0
while i < res:
    if testdata['Sex'][i] == 'male':
        if int(testdata['Pclass'][i]) == 1:
            if age2[i] == 'young':
                p1 = PS * S1 * P1 * A1
                p2 = (1 - PS) * S11 * P11 * A11
            elif age2[i] == 'middle':
                p1 = PS * S1 * P1 * A2
                p2 = (1 - PS) * S11 * P11 * A22
            else:
                p1 = PS * S1 * P1 * A3
                p2 = (1 - PS) * S11 * P11 * A33
        elif int(testdata['Pclass'][i]) == 2:
            if age2[i] == 'young':
                p1 = PS * S1 * P2 * A1
                p2 = (1 - PS) * S11 * P22 * A11
            elif age2[i] == 'middle':
                p1 = PS * S1 * P2 * A2
                p2 = (1 - PS) * S11 * P22 * A22
            else:
                p1 = PS * S1 * P2 * A3
                p2 = (1 - PS) * S11 * P22 * A33
        else:
            if age2[i] == 'young':
                p1 = PS * S1 * P3 * A1
                p2 = (1 - PS) * S11 * P33 * A11
            elif age2[i] == 'middle':
                p1 = PS * S1 * P3 * A2
                p2 = (1 - PS) * S11 * P33 * A22
            else:
                p1 = PS * S1 * P3 * A3
                p2 = (1 - PS) * S11 * P33 * A33
    else:
        if int(testdata['Pclass'][i]) == 1:
            if age2[i] == 'young':
                p1 = PS * S2 * P1 * A1
                p2 = (1 - PS) * S22 * P11 * A11
            elif age2[i] == 'middle':
                p1 = PS * S2 * P1 * A2
                p2 = (1 - PS) * S22 * P11 * A22
            else:
                p1 = PS * S2 * P1 * A3
                p2 = (1 - PS) * S22 * P11 * A33
        elif int(testdata['Pclass'][i]) == 2:
            if age2[i] == 'young':
                p1 = PS * S2 * P2 * A1
                p2 = (1 - PS) * S22 * P22 * A11
            elif age2[i] == 'middle':
                p1 = PS * S2 * P2 * A2
                p2 = (1 - PS) * S22 * P22 * A22
            else:
                p1 = PS * S2 * P2 * A3
                p2 = (1 - PS) * S22 * P22 * A33
        else:
            if age2[i] == 'young':
                p1 = PS * S2 * P3 * A1
                p2 = (1 - PS) * S22 * P33 * A11
            elif age2[i] == 'middle':
                p1 = PS * S2 * P3 * A2
                p2 = (1 - PS) * S22 * P33 * A22
            else:
                p1 = PS * S2 * P3 * A3
                p2 = (1 - PS) * S22 * P33 * A33
    if p1 < p2:
        survive1[i]['Survived'] = 0
        survive1[i].pop('Sex')
    else:
        survive1[i]['Survived'] = 1
        survive1[i].pop('Sex')
    i = i + 1
print(survive1)
#导出
header = ['PassengerId', 'Survived']
with open('E:/pycharm 2020.1.5\pattern recognition/submission1.csv', 'a', newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=header) # 提前预览列名，当下面代码写入数据时，会将其一一对应。
    writer.writeheader()  # 写入列名
    writer.writerows(survive1)
'''
pd.DataFrame(survive1).to_csv('E:/pycharm 2020.1.5\pattern recognition/submission.csv')
'''
'''
pf = pd.DataFrame(list(survive1))#将字典列表转换为DataFrame
order = ['PassengerId','Survived']
pf = pf[order]
file_path = pd.ExcelWriter('E:/pycharm 2020.1.5\pattern recognition/submission.csv')#指定生成的Excel表格名称
pf.fillna(' ',inplace = True)#替换空单元格
pf.to_excel(file_path, encoding='utf-8', index=False)# 输出
file_path.save()#保存表格
'''