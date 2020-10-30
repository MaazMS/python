# map() function returns a map object(which is an iterator) of the results after applying the given function to each item
# of a given iterable (list, tuple etc.)
# The sorted() function returns a sorted list of the specified iterable object.
# set function is use to convert list list set.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print (sorted(set(arr))[-2])
