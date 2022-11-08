# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())

mat = "WELCOME".center(M, "-")
for i in range((N-1)//2, 0, -1):
    mat = (".|."*(2*i-1)).center(M, "-")+"\n"+mat+"\n"+(".|."*(2*i-1)).center(M, "-")
print(mat)