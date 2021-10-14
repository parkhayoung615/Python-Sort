import numpy as np
#===== 버블 정렬 =====
arrNum = np.array([57, 33, 41, 91, 7, 18, 52, 23], int)

def sortInsertion():
    for i in range(1, len(arrNum)):
        print(i)
        
        for j in range(i, 0, -1):
            if arrNum[j - 1] > arrNum[j]:
                arrNum[j - 1], arrNum[j] = arrNum[j], arrNum[j - 1]
            
        print("{}번째: {}" .format(i, arrNum))
            
print("기본데이터: {}" .format(arrNum))
print("================================")
sortInsertion()
print("================================")
print("삽입정렬 수행결과\n{}" .format(arrNum))