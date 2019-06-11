import os, csv, random, string
import numpy as np

class CsvHanlder():
    def __init__(self):
        if not os.path.isdir('ilovecoffee'):
            os.makedirs('ilovecoffee')

    def create_csv(self):
        # 隨機英文名
        Englishname = ['John', 'Tony', 'Mary', 'Sally',
                       'Hank', 'Tom', 'Steve', 'Jason', 'Vivi', 'Lucy']

        with open('ilovecoffee/customers.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['customer_id', 'customer_name',
                             'customer_mobile', 'frequency'])
            for a in range(500):

                name = random.randint(0, 9)
                customer_id = ''.join(random.choice(string.ascii_letters) for x in range(
                    1)) + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(7))
                # list中隨機產生名字
                customer_email = Englishname[name]+'.'+customer_id

                # 測試時檢查是否有首字為數字
                if customer_id[0] is string.digits:
                    print('err')
                # 隨機產生不重複的號碼
                resultList = random.sample(
                    range(900000001, 999999999), 500)
                customer_mobile = '+886'+str(resultList[a])
                frequency = random.randint(0, 20)
                # 寫入customers.csv
                writer.writerow([customer_id, customer_email,
                                 customer_mobile, frequency])

    def calculate_csv(self):
        tmp = np.loadtxt(
            "D:/Python Codes/ilovecoffee/customers.csv", dtype=np.str, delimiter=",")
        fq = tmp[1:, 3:].astype(np.float)
        i = []
        for a in range(500):
            i.append(fq[a][0])
            counts = np.bincount(i)  # 眾數
        print(('中位數：' + str(np.median(i))), '眾數：' + str(np.argmax(counts)),
              '平均數：' + str("{:.5f}".format(np.mean(i))))

CsvHanlder().create_csv()