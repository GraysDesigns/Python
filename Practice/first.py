largest = None
for value in [12, 7, 94, 3, 89]:
    if largest is None or value >= largest:
        largest = value
print(largest)
