import numpy
def tridiag(a,b,c,d):
    N=10
    h=1/N
    a=-2*numpy.ones([N,1])
    b=(1-h^2)*numpy.ones([N,1])
    c=numpy.ones([N,1])
    d=h^2*numpy.ones([N,1])+(h^2-1)*numpy.identity([N,1])
    l=len(d)
    v=numpy.zeros([n,1])
    y=v
    w=a(1)
    y(1)=d(1)/w
    for i in [list(range(2,n))]:
        v(i-1)=c(i-1)/w
        w=a(i)-b(i)*v(i-1)
        y(i)=(f(i)-b(i)*y(i-1))/w
    for j in [list(range(n-1,1))]:
        y(j)=y(j)-v(j)*y(j+1)
        j=j-1
    return y