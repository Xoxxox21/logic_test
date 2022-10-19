if __name__ == '__main__':
    N = int(input())
data=[]
for i in range(N):
    inp = input().split()
    if inp[0]=='insert':
        data.insert(int(inp[1]),int(inp[2]))
    elif inp[0]=='append':
        data.append(int(inp[1]))
    elif inp[0]=='sort':
        data.sort()
    elif inp[0]=='remove':
        data.remove(int(inp[1]))
    elif inp[0]=='print':
        print(data)
    elif inp[0]=='reverse':
        data.reverse()
    elif inp[0]=='pop':    
        data.pop()
    else:
        print('perintah salah')
    