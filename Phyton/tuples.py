# Create Tuples
# Tuples are immutable 


# ==================== TUPLES LENGTH =========================
# SYNTAX
tuple = ('item1','item2','item3')
print(len(tuple))


# ==================== ACCESSING TUPLES VALUE ===================
# With Positive Index
tpl = ('Banana','Apple','Orange','Lime')
print(tpl[2])
last_tuple = len(tuple)-2
print(tpl[last_tuple])

# With Negative Index
tpl = ('Norway','Germany','Canada','Iceland')
print('Second Negative: ',tpl[-2])


# ================== SLICING TUPLES ==========================
# Syntax
# Positive Index
tpl = ('index1','index2','index3','index4')
all_items = tpl[0:4]
print(all_items)
all_items = tpl[0:]
print(all_items)
middle_two_items = tpl[1:3]
print(middle_two_items)

# Negative Index
tpl = ('CSS','Javascript','NextJS','Rust','Solidity')
all_items = tpl[-4:]
print(all_items)
print(len(tpl))

# ====================== CHANGING TUPLES TO LIST =====================
tpl = ('Index1','Index2','Index3','Index4')
lst = list(tpl)
lst[0] = 'Index4'
print(lst)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']

# ===================== JOINING TUPLES ===============================
fruits = (('banana','orange','mango','lime','avocado'))
vegetables = ('Tomato', 'Cabbage', 'Onion', 'Carrot', 'Potato')
print(fruits + vegetables)
print(len(fruits+vegetables))

# ===================== DELETING TUPLES ==============================
countries = ('Malaysia','Singapore','Myanmar', 'Russia', 'England')
del countries
