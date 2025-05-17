
def partition(arr:[],start,last):
    i = start
    j = last
    index = arr[len(arr)//2]
    while True:
        while arr[i]<index:
            i+=1
        while arr[j]>index:
            j-=1
        arr[i], arr[j] = arr[j], arr[i]
        if i>=j:
            return j

def my_quicksort(arr:[],left:int, right:int):
    if left < right:
        partition_index:int = partition(arr,left,right)
        my_quicksort(arr,left,partition_index-1)
        my_quicksort(arr,partition_index+1,right)

try:
    # arr = list(map(float, input().split(" ")))
    arr = [1,3,1,5,1,3,8]
except ValueError:
    print("Вводите только числа")
    numbers = []
even = []

my_quicksort(arr,0,len(arr)-1)
print(arr)
print(arr[0],arr[-1])

