def binary(a,l,h,k):
    if(l<h):
        m=(l+h)//2
        if(a[m]==k):
            return m
        elif(a[m]<k):
            return binary(a,m+1,h,k)
        else:
            return binary(a,l,m-1,k)
    else:
        return -1
a=[1,2,3,4,5,6]
k=3
r=binary(a,0,len(a)-1,k)
if(r):
    print("the element ",k,"is present at",r)
else:
    print("the element ",k,"is not present")    
