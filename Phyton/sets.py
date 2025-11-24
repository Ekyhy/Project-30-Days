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
