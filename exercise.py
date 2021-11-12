"""

練習寫入檔案

    假設有一些整數裝在 data 清單裡,你想要一行一行的把這些數字

 寫到 text.txt 檔去,請寫出這樣的程式碼

 exercise.py

"""

data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫 "寫入檔案" 的程式碼

with open('text.txt', 'w') as f:
    for d in data:
        print(d)
        f.write(str(d) + '\n')