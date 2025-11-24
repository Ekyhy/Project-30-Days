# =============== CREATING A SET ==================
# Syntax
# st = set()

# Creating set with in a initial items
# st = {'item1','item2','item3'}


# =============== GETTING SET'S LENGTH ============
st = {'banana','apple','water melon','grape','coconut'}
print(st)
print(len(st))

# ============ ACCESSING ITEMS IN A SETS ==========
# Checking an item, to check if an item exist in a list we use in membership operator
st = {'banana','apple','water melon','orange','lime'}
print(st)
print('Does set st contain banana?', 'banana' in st)

# ========= ADDING ITEMS TO A SETS ==============
st = {'banana','apple','water melon','orange','lime'}
print(st)
st.add('avocado')
print(st)

# ======== MULTIPLE ADD ITEMS TO A SETS ===========
# Syntax :
# st.update()
st = {'Jakarta','Yogyakarta','Palembang'}
print(st)
st.update(['Bandar Lampung','Purwokerto','Balikpapan'])
print(st)

# ======== REMOVING ITEMS FROM A SET =============
# Using remove()
print(st)
st.remove('Palembang')
print(st)
# Using pop() remove random item from a list
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
print(fruits)
removed_item = fruits.pop()
print(fruits)
print(removed_item)

# ======== CLEARING ITEMS IN A SET ================
# Clearing value a set
st = {'item1','item2','item3'}
st.clear()
print(st)

# ================= DELETING A SET ================
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits # An Error output

# ============= CONVERTING LIST TO SET ============
countries = ['England','Russia','India','Pakistan']
print(countries)
st = set(countries)
print(st)

# ===========-- JOINING SETS ===============
# Using union()
countries = {'England','Russia','India','Pakistan'}
capital_City = {'London','Moskow','New Delhi','Islamabad'}

countriesAndCapitalCity = countries.union(capital_City)
print(countriesAndCapitalCity)

# Using update()
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# ========== FINDING INTERSECTION ITEMS ==========
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

# ========= CHECKING SUBSET AND SUPER SET
# issubset()
# issuperset()
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))

# ========== CHECKING THE DIFFERENCE BETWEEN TWO SETS ===========
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
after10_numbers = {10,12,13,14,15,16}
print(whole_numbers.difference(after10_numbers)) # take number 10
print(after10_numbers.difference(whole_numbers)) # take number 10


# == FINDING SYMMETRIC DIFFERENCE BETWEEN TWO SETS ==
whole_numbers = {1,2,3,4,5,6,7,8,9,10}
some_numbers = {1,5,7,9}
print(whole_numbers.symmetric_difference(some_numbers))

# ====== ISDISJOIN SETS =========
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}