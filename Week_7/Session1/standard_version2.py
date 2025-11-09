# Problem 1
def get_village_class_iterative(population):
    population_str = str(population)
    return len(population_str)


def get_village_class_recursive(population):
    pop_str = str(population)

    if len(pop_str) == 1:
        return 1
    return 1 + get_village_class_recursive(int(pop_str[1:]))
    

print(get_village_class_iterative(432))
print(get_village_class_recursive(432))
print(get_village_class_iterative(9))
print(get_village_class_recursive(9))

# Problem 2
def count_walls(walls):
    pass

walls = ["outer", ["inner", ["keep", []]]]

print(count_walls(walls))
print(count_walls([]))