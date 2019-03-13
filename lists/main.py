
list=[]

def _insert(i,e):
    list.insert(i,e)

def _print():
    print(list)

def _remove(e):
    list.remove(e)

def _append(e):
    list.append(e)

def _sort():
    list.sort()

def _pop():
    list.pop()

def _reverse():
    list.reverse()

if __name__ == "__main__":
    N = int(input())
    j=0
    for i in range(N):
        strIng=input().split()
        if 'insert' in strIng[0]:
            _insert(int(strIng[1]),int(strIng[2]))
        elif 'print' in strIng[0]:
            _print()
        elif 'remove' in strIng[0]:
            _remove(int(strIng[1]))
        elif 'append' in strIng[0]:
            _append(int(strIng[1]))
        elif 'sort' in strIng[0]:
            _sort()
        elif 'pop' in strIng[0]:
            _pop()
        elif 'reverse' in strIng[0]:
            _reverse()






