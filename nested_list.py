""" input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""
if __name__ == '__main__':
    data=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])
    score_sorted=sorted(list(set([x[1] for x in data])))
    low_2 = score_sorted[1]
    hasil = []
    for i in data:
        if low_2 == i[1]:
            hasil.append(i[0])
    
    for h in sorted(hasil):
        print(h)