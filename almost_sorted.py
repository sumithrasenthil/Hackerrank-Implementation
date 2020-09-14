
def almostSorted(a):
    n=len(a)
    b=sorted(a)
    if a==b:
        return 'yes'
    k=[]
    for i in range(n):
        if a[i]!=b[i]:
            k.append(i)
    if(len(k)==0):
        return 'yes'
    if(len(k)==1):
        return 'no'
    if(len(k)==2):
            print('yes')
            re='swap '+str(k[0]+1)+' '+str(k[-1]+1)
            return re
    for i in range(len(k)):
        if(a[k[i]]!=b[k[len(k)-i-1]]):
            return 'no'
    re='reverse '+str(k[0]+1)+' '+str(k[-1]+1)
    print('yes')
    return re

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(almostSorted(arr))

