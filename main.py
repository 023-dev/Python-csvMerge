import csv
import glob
import os

input_path = r'./'
output_path = r'./파일이름.csv'

file_list = glob.glob(input_path+'파일이름*.csv')

with open(output_path, 'w') as f:
        for i, file in enumerate (file_list):
            if i ==0:
                with open(file, 'r') as f2:
                    while True:
                        line = f2.readline()

                        if not line:
                            break

                        f.write(line)

                    print(file.split('\\')[-1])

            else:
                with open(file, 'r') as f2:
                    n = 0
                    while True:
                        line = f2.readline()
                        if n != 0 and n != 1:
                            f.write(line)
                        if not line:  
                            break
                        n+= 1
                    print(file.split('\\')[-1])
print('end')
