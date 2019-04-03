def insertionSort(a):
    i = 1

    while ( i < a.__len__() ):

        key = a[i]
        j = i-1

        while j >= 0 and (a[j] > key):
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key
        print(a)
        i = i + 1
    return a

ua = [9,4,5,2,7,3,1,6,8,0] #unsorted array
print(ua)
sa = insertionSort(ua.copy()) #sorted array
print(sa)
