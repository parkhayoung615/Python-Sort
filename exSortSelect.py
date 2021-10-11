import numpy as np
# 선택 정렬
arrNum = np.array([57, 33, 41, 91, 7, 18, 52, 23, 1, 4, 9], int)

def sortSelection():
    for i in range(len(arrNum)):
        minIdx = i;
        for j in range(i+1, len(arrNum)):
            if arrNum[minIdx] > arrNum[j]:
                minIdx = j
        arrNum[i], arrNum[minIdx] =  arrNum[minIdx], arrNum[i]
        print("{}번째 : {}" . format(i+1, arrNum))        

# 출력 (^_^)v
print("기본데이터: {}" .format(arrNum))
print("===============================")
sortSelection()
print("===============================")
print("선택정렬 수행결과\n{}" .format(arrNum))