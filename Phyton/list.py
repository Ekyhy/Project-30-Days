# ===================== CREATE A LIST ======================
# Create list using 2 ways
#  1. Using list built-in function
firstList = list('banana')
print(len(firstList))
#  2. Using list bracket
secondList = ['Indonesia','Malaysia','Singapore']
print(list(secondList))
print(len(secondList))
web_tech = ['HTML','CSS','React','Javascript','C#']
print(list(web_tech))
print(len(web_tech))

# ============ ACCESING LIST ITEMS USING POSITIVE INDEXING =================
web_tech = ['HTML','CSS','React','Javascript','C#']
first_webTech = web_tech[0]
print(first_webTech)
second_webTech = web_tech[1]
print(second_webTech)
last_index = len(web_tech)-1
print(web_tech[last_index])

# ============ ACCESING LIST ITEMS USING NEGATIVE INDEXING =================
fruits = ['banana','melon','mango','apple','orange']
first_fruits = fruits[-4]
second_fruits = fruits[-3]
last_fruits = fruits[-1]
print(first_fruits)
print(second_fruits)
print(last_fruits)

# ============ UNPACKING LIST ITEMS =======================
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)             #Germany
print(fr)             #France
print(bg)             #Belgium
print(sw)             #Sweden
print(scandic)        #Denmark,Finland,Norway,Iceland
print(es)             #Estonia
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

# ============ SLICING ITEMS FROM A LIST =======================
# Remamber index can start value from zero (0)
# Positive Index
fruits = ['banana','melon','mango','apple','orange']
all_fruits = fruits[0:5]
print(all_fruits)
# We can also add 0: without stoping value
all_fruits_no_stop = fruits[0:]
print(all_fruits_no_stop)

# Negative Index
fruits = ['banana','melon','mango','apple','orange']
all_fruits = fruits[-5:]
print(all_fruits)
# We can also add 0: without stoping value
all_fruits_no_stop = fruits[-5:]
print(all_fruits_no_stop)
reversed_fruits = fruits[::-1]
print(reversed_fruits)

# =============== MODIFYING LIST =========================
fruits = ['banana','melon','mango','apple','orange']
fruits[3] = 'avocado'
print(fruits)
print(len(fruits))
last_fruits_index = len(fruits)-1
fruits[last_fruits_index] = 'watermelon'
print(fruits)

# ================ CHECKING ITEMS IN A LIST ===============
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
does_exits = 'Indonesia' in countries
print(does_exits)   #False
does_exits = 'Denmark' in countries
print(does_exits)   #True

# ================= ADDING ITEMS TO A LIST ===================
# append()  -> add value to last index
# Syntax :
# first = list()
# first.append(item)
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
print(len(countries))   #9
countries.append('Indonesia')
print(countries)
print(len(countries))   #10

# ============= INSERT ITEMS INTO A LIST =======================
# insert() -> Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.
# Styntax
# lst = ['item1', 'item2']
# lst.insert(index, item)

fruits = ['banana','melon','mango','apple','orange']
fruits.insert(3,'lime')
print(fruits)
print(len(fruits))  #6


# ============= REMOVING ITEMS FROM A LIST =======================
# syntax
# lst = ['item1', 'item2']
# lst.remove(item)
fruits = ['banana','melon','mango','apple','orange']
fruits.remove('banana')
print(fruits)

# ============= REMOVING ITEMS USING POP =======================
# syntax
# lst = ['item1', 'item2']
# lst.pop()       # last item
# lst.pop(index)
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
countries.pop()
print(countries)
countries.pop(6)
print(countries)

# ============= REMOVING ITEMS USING DEL =======================
# # syntax
# lst = ['item1', 'item2']
# del lst[index] # only a single item
# del lst        # to delete the list completely
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
del countries[3]
print(countries)
del countries[0:6]
print (countries)


# =============== CLEARING LIST ITEMS =======================
# # syntax
# lst = ['item1', 'item2']
# lst.clear()
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
countries.clear()
print(countries)

#  =============== COPYING A LIST ==========================
# # syntax
# lst = ['item1', 'item2']
# lst_copy = lst.copy()
fruits = ['banana','melon','mango','apple','orange']
fruits_copy = fruits.copy()
print(fruits_copy)
# ============= JOINIG LIST =======================
# Using (+)
# # syntax
# list3 = list1 + list2
fruits = ['banana','melon','mango','apple','orange']
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']

fruits_and_countries = fruits + countries
print(fruits_and_countries)

# Using extend
# syntax
# list1 = ['item1', 'item2']
# list2 = ['item3', 'item4', 'item5']
# list1.extend(list2)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# ============= COUNTING ITEMS IN A LIST =======================
# syntax
# lst = ['item1', 'item2']
# lst.count(item)
fruits = ['banana','melon','mango','apple','orange']
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
fruits_and_countries = fruits + countries
print(fruits_and_countries.count('Belgium'))

# ============= REVERSING A LIST =======================
## syntax
# lst = ['item1', 'item2']
# lst.reverse()

vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
vegetables.reverse()
print(vegetables)


# ========== SORTING ITEMS =========================
# Using sort()
# Syntax
# lst= ['item1','item2']
# last.sort()               ascending
# last.sort(reverse=true)   descending
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
countries.sort()
print(countries)    # Sorted in alphabet
countries.sort(reverse=True)
print(countries)

# Using sorted()
fruits = ['banana','melon','mango','apple','orange']
print(sorted(fruits)) #ascending
print(sorted(fruits,reverse=True)) #descending