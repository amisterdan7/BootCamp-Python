conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
conjunto_c = {3, 4, 5}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_b.isdisjoint(conjunto_a))
print(conjunto_a.isdisjoint(conjunto_c))
print(conjunto_c.isdisjoint(conjunto_a))
