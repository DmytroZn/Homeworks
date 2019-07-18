def flatten(seq):

    list_new=[]
    for x in seq:
        if type(x)!=list and type(x)!=tuple:
            list_new.append(x)
        else:
            list_new.extend(flatten(x))
    return list_new
    
print(flatten())