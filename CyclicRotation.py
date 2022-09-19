def solution(A, K):
    # write your code in Python 3.6
    if K != None or A != []:
        for i in range(K):
            kosong = []
            for j in range(len(A)+1):
                if j == 0:
                    kosong.append(A[-1])
                else:
                    if j == len(A):
                        continue
                    else:
                        kosong.append(A[j-1])
            A=kosong
    else:
        A=[]
    return A
