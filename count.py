def count(sequence, item):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == item:
            count += 1
            
    return count

print count([1, 2, 1, 5, 7, 1], 1)    