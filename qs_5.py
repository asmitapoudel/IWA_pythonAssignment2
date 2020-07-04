""" 
 Create a tuple with your first name, last name, and age. 
 Create a list, people, and append your tuple to it.
 Make more tuples with the corresponding information from your friends
 and append them to the list. Sort the list.
 When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name,
 last name, or age.
 """

lst = []
tup1 = ('Asmita','Poudel',21)
lst.append(tup1)
tup2 = ('Aagan','Maskey',22)
lst.append(tup2)
tup3 = ('Jivan','Pun',28)
lst.append(tup3)
tup4 = ('Rima','Magar',35)
lst.append(tup4)
tup5=('Pooja','Pathak',25)
lst.append(tup5)

print("Original list is {}".format(lst))

lst.sort(key = lambda x: x[2])
print("List sorted wih third element is {}".format(lst))
