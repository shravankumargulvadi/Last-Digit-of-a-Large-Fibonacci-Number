
# coding: utf-8

# In[21]:


def fibn(n):
    import numpy as np
    
    if n==1:
        print(0)
    elif n==2:
        print(1)
    else:
        a=np.random.randint(1, 100, n+1)
        for i in range(2,n+1):
            
            a[0]=0
            a[1]=1
            a[i]=(a[i-1]+a[i-2])%10
        
    return(a[n])
if __name__ == '__main__':
    input_n = int(input())
    print(fibn(input_n))

