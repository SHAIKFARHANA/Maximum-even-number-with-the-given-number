num=int(input())
list_num=list(map(int,str(num)))
maximum=max(list_num)
minimum=min(list_num)
result=list_num[::-1]
total1=[str(i) for i in result]
total2=int("".join(total1))
max_even=[]
j=0
for x in range(num,total2):
    if x%2==0:
        max_even.append(x)
print(max(max_even))        
