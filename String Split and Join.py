def split_and_join(line):
    s=line.split(' ')
    joinStr='-'.join(s)
    return joinStr

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
