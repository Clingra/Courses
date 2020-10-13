import numpy
def tridiag(a,b,c,f):
    N=10
    h=1/N
    a=-2*numpy.ones([N,1])
    b=(1-h^2)*numpy.ones([N,1])
    c=numpy.ones([N,1])
    f=