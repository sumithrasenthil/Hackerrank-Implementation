
def separateNumbers(s):
    n=len(s)
    for i in range(len(s)//2):
        a=''
        k=0
        r=int(s[0:i+1])
        f=r
       
        while(len(a)<n):
            a+=str(r)
            r=int(r)
            r+=1
        if(a==s):
            return 'YES'+' '+str(f)
    return 'NO'

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))

