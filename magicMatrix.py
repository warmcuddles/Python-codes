import numpy as np
import sys
color=sys.stdout.shell
def f(n):
    if(n%2==1):
        shift = np.array([k//n for k in range(0 , (n*n-1)+1)])
        c = np.array(np.subtract([q for q in range(1,n*n+1)],shift))
        c[:]+=(n-3)//2
        c[:]%=n
        r = np.array(np.add([w for w in range(n*n,0,-1)],shift[:]*2))
        r[:]%=n
        k=np.add(c[:]*n,r)+1
        A=np.zeros(n*n,dtype='int')
        A[np.add(c[:]*n,r)]= np.array([d for d in range(1,n*n+1)])
        A=A.reshape(n,n)
        color.write(A,"STRING")
        print("\n")
        print("Sum of rows:",np.sum(A,axis=0))
        print("Sum of col:",np.sum(A,axis=1))

    elif(n%4==0):
        A=np.arange(1,n*n+1)
        A=A.reshape(n,n)
        I1 = np.array([k for k in range(1,n+1,4)])
        I2 = np.array([k for k in range(4,n+1,4)])
        I=np.array([I1,I2]).reshape(n//2)
        J=np.array(list(I[::-1]))
        s=np.repeat([np.array(I-1)], n//2, axis=0)
        d=np.repeat([np.array(J-1)], n//2, axis=0)
        A[s.T,s]=A[d.T,d]

        I1 = np.array([k for k in range(2,n+1,4)])
        I2 = np.array([k for k in range(3,n+1,4)])
        I=np.array([I1,I2]).reshape(n//2)

        J=np.array(list(I[::-1]))

        s=np.repeat([np.array(I-1)], n//2, axis=0)
        d=np.repeat([np.array(J-1)], n//2, axis=0)
        A[s.T,s]=A[d.T,d]
        color.write(A,"COMMENT")
        print("\n")
        print("Sum of rows:",np.sum(A,axis=0))
        print("Sum of col:",np.sum(A,axis=1))
print()
color.write("DING DONG lets create a magic square","COMMENT")
print('\n')
color.write('''A magic square is a matrix where all of its element
ROW WISE,COLUMN WISE,DIAGONALLY add up to same no.''',"KEYWORD")
print("\n")

user=int(input("Enter no greater than 2 and (a multiple of 4, or an odd no): "))
print("\n")
f(user)
