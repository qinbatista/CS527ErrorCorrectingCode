def Phi(n):
    n = n
    count = 0
    for i in range(1,n+1):
        value = n/i
        if value.is_integer()==False or i ==1:
            find=False
            for j in range(1,i):
                if (n/j).is_integer() and (i/j).is_integer() and j!=1:
                    # print("n/j"+str(n/j)+" "+str((n/j).is_integer()))
                    # print("i/j"+str(i/j)+" "+str((i/j).is_integer))
                    # print("has:"+str(i)+ " "+str(j!=1))
                    find = True
                    continue
            if find != True:
                # print(i)
                count = count+1
    print("φ(" +str(n) +")="+str(count))

def Divisor(n):
    for i in range(1,n+1):
        value = n/i
        if value.is_integer():
            print(str(n)+" s divisor:"+str(i))
            
            
def MinDegree(orderList):
    # orderList = [1,3,11,31,33,93,341,1023]
    # orderList = [1,3,7,9,21,63]
    for j in orderList:
        for i in range(1,9999999):
            # print("kn-1="+str(2**i-1))
            if ((2**i-1)/j).is_integer() == True:
                print(str(i))
                break

if __name__ == "__main__":
    # MinDegree([1,3,7,9,21,63])
    Divisor(1023)
    Phi(1)
    Phi(3)
    Phi(11)
    Phi(31)
    Phi(33)
    Phi(93)
    Phi(341)
    Phi(1023)
    # MinDegree([1,3,11,31,33,93,341,1023])
