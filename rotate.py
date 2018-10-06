def rotate(a,b):
    temp = a[0:b]
    a = a[b:]
    a +=temp
    return a

