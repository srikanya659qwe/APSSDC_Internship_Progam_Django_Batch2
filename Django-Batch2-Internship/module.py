def Prime(n):
    factors_count=0
    for i in range(1,n+1):
        if n%i==0:
            factors_count+=1
            
    if factors_count==2:
        print("Prime")
    else:
        print("Not a Prime")
        
    