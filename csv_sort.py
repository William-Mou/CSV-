
# coding: utf-8

# In[ ]:

import csv
al=[
   'SQRC522016_Sep_21_1425.csv',
   'SQRC532016_Sep_21_1601.csv',
   'SQRC542016_Sep_26_1220.csv',
   'SQRC552016_Sep_26_1329.csv',
   'SQRC562016_Sep_26_1719.csv',
   'SQRC572016_Sep_27_1123.csv',
   'SQRC582016_Sep_27_1306.csv',
   'SQRC592016_Sep_28_1211.csv',
   'SQRC602016_Sep_28_1334.csv',
   'SQRC612016_Sep_28_1456.csv',
   'SQRC622016_Sep_30_1138.csv',
   'SQRC632016_Sep_30_1300.csv',
   'SQRC642016_Sep_30_1447.csv',
   'SQRC652016_Sep_30_1559.csv',
   'SQRC662016_Sep_30_1735.csv',
   'SQRC672016_Sep_30_1858.csv',
   'SQRC682016_Oct_01_1058.csv',
   'SQRC692016_Oct_01_1234.csv',
   'SQRC702016_Oct_01_1355.csv',
   'SQRC712016_Oct_01_1500.csv',
   'SQRC722016_Oct_01_1829.csv',
   'SQRC732016_Oct_02_1113.csv',
   'SQRC742016_Oct_02_1228.csv',
   'SQRC752016_Oct_02_1357.csv',
   'SQRC762016_Oct_07_1103.csv',
   'SQRC772016_Oct_07_1231.csv',
   'SQRC782016_Oct_07_1356.csv',
   'SQRC792016_Oct_07_1530.csv',
   'SQRC802016_Oct_07_1653.csv',
   'SQRC812016_Oct_07_1837.csv',
   'SQRC822016_Oct_08_1125.csv',
   'SQRC832016_Oct_08_1243.csv',
   'SQRC842016_Oct_08_1358.csv',
   'SQRC852016_Oct_08_1551.csv',
   'SQRC862016_Oct_08_1707.csv',
   'SQRC872016_Oct_08_1837.csv',
   'SQRC882016_Oct_09_1115.csv',
   'SQRC892016_Oct_09_1410.csv',
   'SQRC902016_Oct_09_1539.csv',
   'SQRC912016_Oct_14_1515.csv',
   'SQRC922016_Oct_14_1644.csv',
   'SQRC932016_Oct_14_1814.csv',
   'SQRC942016_Oct_15_1119.csv',
   'SQRC952016_Oct_15_1258.csv',
   'SQRC962016_Oct_15_1415.csv',
   'SQRC972016_Oct_15_1546.csv',
   'SQRC982016_Oct_15_1719.csv',
   'SQRC992016_Oct_15_1914.csv','SQRC1002016_Oct_16_1117.csv',
   'SQRC1012016_Oct_16_1400.csv',
   'SQRC1022016_Oct_16_1545.csv',
   'SQRC1032016_Oct_16_1915.csv',
   'SQRC1042016_Oct_17_1255.csv',
   'SQRC1052016_Oct_17_1426.csv',
   'SQRC1062016_Oct_17_1603.csv',
   'SQRC1062016_Oct_17_1604.csv',
   'SQRC1072016_Oct_21_1158.csv',
   'SQRC1082016_Oct_21_1502.csv',
   'SQRC1092016_Nov_20_1157.csv',
   'SQRC1102016_Nov_20_1321.csv',
   'SQRC1112016_Nov_20_1457.csv',
   'SQRC1122016_Nov_20_1625.csv',
   'SQRC1132016_Nov_20_1927.csv',
   'SQRC1142016_Nov_21_1339.csv',
   'SQRC1152016_Nov_21_1525.csv',
   'SQRC1162016_Nov_28_1303.csv',
   'SQRC1172016_Nov_28_1404.csv',
   'SQRC1182016_Nov_30_1235.csv',
   'SQRC1192016_Nov_30_1405.csv',
   'SQRC1202016_Nov_30_1546.csv',
   'SQRC1212016_Dec_09_1231.csv',
   'SQRC1222016_Dec_09_1353.csv',
   'SQRC1232016_Dec_09_1533.csv',
   'SQRC1242016_Dec_09_1659.csv',
   'SQRC1252016_Dec_09_1830.csv',
   'SQRC1262017_Jan_27_1355.csv',
   'SQRC1272017_Jan_27_1545.csv',
   'SQRC1282017_Jan_27_1724.csv',
   'SQRC1292017_Jan_27_1852.csv',
   'SQRC1302017_Jan_28_1322.csv',
   'SQRC1312017_Jan_28_1500.csv',
   'SQRC1322017_Jan_28_1612.csv',
   'SQRC1332017_Jan_28_1928.csv',
   'SQRC1342017_Jan_29_1313.csv',
   'SQRC1352017_Jan_29_1451.csv',
   'SQRC1362017_Jan_29_1603.csv',
   'SQRC1372017_Jan_29_1736.csv',
   'SQRC1382017_Jan_29_1924.csv',
   'SQRC1392017_Jan_30_1327.csv',
   'SQRC1402017_Jan_30_1444.csv',
   'SQRC1412017_Jan_30_1613.csv',
   'SQRC1422017_Jan_30_1758.csv',
   'SQRC1432017_Feb_01_1438.csv',
   'SQRC1442017_Feb_01_1620.csv',
   'SQRC1452017_Feb_15_1442.csv',
   'SQRC1462017_Feb_15_1623.csv',
   'SQRC1472017_Feb_15_1733.csv',
   'SQRC1482017_Feb_16_1651.csv',
   'SQRC1492017_Feb_17_1416.csv',
   'SQRC1502017_Feb_20_1336.csv',
   'SQRC1512017_Feb_20_1454.csv',
   'SQRC1522017_Feb_20_1615.csv',
   'SQRC1532017_Feb_20_1739.csv']
for file in al:
    print(file)
    f = open(file,"r")
    data=[]
    head=['Block', 'Trial', 'Mean', ' Variance', ' Actual Color', 'Button Response', 'Color Response', 'Reaction Time', 'Stimulus Presented', 'Accuracy', 'CP1', 'CP2', 'CP3', 'CP4', 'CP5', 'CP6', 'CP7', 'CP8']
    for row in csv.reader(f):
        data_sort=[]
        data_each=row

        if row==[] or row[10]=="CP1" or row[10]=='':
            continue
        else:
            for j in range(8):
                data_sort.append(float(row[10+j]))
                data_sort.sort()
            for j in range(8):
                data_each[10+j]=str(data_sort[j])
            data.append(data_each)
    f.close()

    if file[4]=='1':
        total=open(str(file[4:7])+'.csv','w',newline='')
        print(str(file[4:7]))
    else:
        total=open(str(file[4:6])+'.csv','w',newline='')
        print(str(file[4:6]))
    dtotal=csv.writer(total)
    dtotal.writerow(head)
    for fn in data:
        dtotal.writerow(fn)
    total.close()


