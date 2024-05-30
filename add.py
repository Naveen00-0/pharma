lst= [4,7,9,2,5]

tot=0
count=0

while count<len(lst):
    tot=tot+lst[count]
    count=count+1

avg=tot/count

print("Average =",avg)
