 
def get_triplet_product(sum):
    for a in range(1, sum, 1):
        for b in range(1, sum - a, 1):
            c = sum - a - b
            if (a * a) + (b * b) == (c * c):
                return a * b * c
    return 0
 
product = get_triplet_product(1000)
 
print product