def split_and_join(line):
    # write your code here
    hasil = line.split()
    hasil = '-'.join(hasil)
    return hasil

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)