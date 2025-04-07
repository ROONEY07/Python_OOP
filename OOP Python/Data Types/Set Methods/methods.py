# Union
a = {1,2,3}
b = {4,4,5}
add_two = a.union(b)
# print(add_two)




# intersection
inter_set = a.intersection(b)
# print(inter_set)




# Difference
diff = a.difference(b)
# print(diff)




# symmetric difference
sym_diff = a.symmetric_difference(b)
# print(sym_diff)

# is sub set
# sub_set = a.issubset(b)
sub_set = b.issubset(a)
# print(sub_set)   





# disjoints set
disjoin_set = a.isdisjoint(b)
# print(disjoin_set)



# frozen set
f_set = frozenset(a)
f_set.add(5)
print(f_set)

