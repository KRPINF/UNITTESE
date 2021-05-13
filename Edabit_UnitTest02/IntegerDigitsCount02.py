def count(n):
    x = 0
    for i in str(n):
        if i.isdigit():
            x += 1
    return(x)

print(count(318))
print(count(-92563))
print(count(4666))
print(count(-314890))
print(count(654321))
print(count(638476))