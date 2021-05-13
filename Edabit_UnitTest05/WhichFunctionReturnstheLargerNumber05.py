def which_is_larger(f, g):
    if f > g:
        return 'f'
    elif f < g:
        return 'g'
    else:
        return 'neither'

print(which_is_larger(5, 10))
print(which_is_larger(25, 25))
print(which_is_larger(505050, 5050))