#Curtis Ingram, ID 1388990
#Assignment 4 - Computing Problem
#goal of this assignment is to solve the Helmholtz 
#equation with the tri-diagonal algorithm

#import math
#L=None #interval length
#x=None #internal points
#h=None #increment h=L/(N+1)
#N=10
import numpy
def triDiagMat(a,b,c,f):
    numEq = len(f)
    ap,bp,cp,dp = map(numpy.array, (a,b,c,f))
    for i in range(1,numEq):
        mp=ap[i-1]/bp[i-1]
        bp[i]=bp[i]-mp*cp[i-1]
        dp[i]=dp[i]-mp*dp[i-1]
    xp=bp
    xp[-1]=dp[numEq-2,-1,-1]
    for i2 in range(numEq-2,-1,-1):
        xp[i2]=(dp[i2]-cp[i2]*xp[i2+1])/bp[i2]
    return xp

