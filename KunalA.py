a=str(input("Enter the currency value: ")) 


def currency(a):
    Single=[" ", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    double=["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
    tens=[" "," ","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
    
    n=float(a)
    
    if n<0 or n>=999999.99:
        print("please enter the value below 999999.99")
    else:
        x=[0,0,0,0,0,0]
        i=0
        p=int(n)
        while p>0:
            x[i]=p%10
            i+=1
            p=p//10
        
        num="Rs."
        
        if x[5]!=0:
            num+=Single[x[5]]+" Lakh "
               
        if x[4]!=0:
            if x[4]==1:
                num+=double[x[3]]+" Thousand "
                
            else:
                num+=tens[x[4]]+" "+Single[x[3]]+" Thousand "
                
        else:
            if x[3]!=0:
                num+=Single[x[3]]+" Thousand "
                
        if x[2]!=0:
            num+=Single[x[2]]+" Hundred "
    
        if x[1]!=0:
            if x[1]==1:
                if x[2]==x[3]==x[4]==x[5]==0:
                    num+=double[x[0]]
                else:
                    num+="And"+double[x[0]]
            else:
                if x[2]==x[3]==x[4]==x[5]==0:
                    num+=tens[x[1]]+" "+Single[x[0]]
                else:
                    num+="And "+tens[x[1]]+" "+Single[x[0]]
        else:
            if x[0]!=0:
                if x[1]==x[2]==x[3]==x[4]==x[5]==0:
                    num+=Single[x[0]]
                else:
                    num+="And "+Single[x[0]]
                    
        try:
            b=a.split('.')[1] 
        except:
            b=0
            
        
        t=int(b)
        if t==0:
            print(num+" ONLY")
        else:
            print(num,b+'/'+str(10**len(b))+" ONLY")
               
currency(a)
