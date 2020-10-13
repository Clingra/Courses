#The purpose of this code is to use the tri-diagonal (Thomas) algorithm
#to solve the Helmholtz equation using N equally-spaced points
import numpy
def triDiagHelm(a,b,c,d):
    N=10 #equally spaced internal points
    h=1/N #distance between points
    #now the matrices for a,b,c,d must be made
    a=-2*numpy.ones([N,1])
    b=(1-h**2)*numpy.ones([N,1])
    c=numpy.ones([N,1])
    d=h**2*numpy.ones(N)+(h**2-1)*numpy.identity(N)
    #next are calculations for helmholtz solution
    n=len(d)
    v=numpy.zeros(n)
    y=v
    w=a[1]
    y[1]=d[1]/w
    for i in [list(range(2,n))]:
        v[i-1]=c[i-1]/w
        w=a[i]-b[i]*v[i-1]
        y(i)=(f[i]-b[i]*y[i-1]/w
    for j in [list(range(n-1,1))]:
        y[j]=y[j]-v[j]*y[j+1]
        j=j-1
    return y