l = set()

print(type(l))

# 1. Union

set1 ={1,2,3,4,5}
set2 ={4,5,6,7,8}

union_set =set1.union(set2)

print(union_set)
print()

# 2. Intersection

set1 ={1,2,3,4,5}
set2 ={4,5,6,7,8}

intersection =set1.intersection(set2)

print(intersection)
print()# {4,5}

#2.1. intersection Update

#set1.intersection_update(set2)

print(set1)

# 3. Difference 


set1 ={1,2,3,4,5}
set2 ={4,5,1,7,8}

difference =set1.difference(set2)

print(difference)# {1,2,3}
print()

#  4. Symmetric Difference : different Element

set1 ={1,2,3,4,5}
set2 ={4,5,6,7,8}

symmetric_differnecr_set=set1.symmetric_difference(set2)

print(symmetric_differnecr_set)# {1,2,3,6,7,8}
print()

# 5.Subset

a = {1,2,3}
b = {1,2,3,4,5,6}

sub_set = a.issubset(b)#True
print(sub_set)
print()

# 6.Superset

a = {1,2,3,4,56,5}
b = {1,2,3,56}

sup_set= a.issuperset(b)#true
print(sup_set)
print()

#  7. Disjoint Set:there are no common elements in both sets.

a = {1,2,3,4,56,5}
b = {9,5,6}

disjoint_set = a.isdisjoint(b)

print(disjoint_set) #Flase
print()
