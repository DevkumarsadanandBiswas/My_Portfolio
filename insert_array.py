print("\n How many elements are there in Array?")
n = int(input())
array=[]
i=0
for i in range(n):
    print("\n Enter element in array")
    item = int(input())
    array.append(item)
print("Enter the location where you want to insert an element")
position = int(input())

print("Enter the value to insert")
value = int(input())
array =array[:position]+[value]+array[position:]
print("Resutant array is")
print(array)