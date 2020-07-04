"""
Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
"""

lioftuples=[('Shruti','Poudel',25),('Sam','lama',22),('sr','khan',20)]
l=[]
total=0
for i in range(len(lioftuples)):
    li=lioftuples[i][2]
    l.append(li)
print(l)
for ele in range(0, len(l)):
    total = total + l[ele]
avg=total/len(l)
print(avg)

for i in lioftuples:
    if i[2]>avg:
        print(i[0]+' '+i[1]+' is older')
    else:
        print(i[0]+' '+i[1]+' is younger')
