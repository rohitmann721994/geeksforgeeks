arr = [2, 7, 9, 5, 8, 7, 4]
k = 5
# output:



index=0
toSwap=0
indexOfK=False
lessThanK={}
moreThanK= {}
numberOfSwitch=0
numberOfK=len(arr)-len(lessThanK)-len(moreThanK)

for i in range(len(arr)):
    if(arr[i]==k):
        indexOfK=i
    if(arr[i]>k):
        lessThanK.update({i:arr[i]})
    if(arr[i]<k):
        moreThanK.update({i: arr[i]})

# if(indexOfK):
#     while((i<indexOfK for i in moreThanK.keys()) or ()):
#         None

    # numberOfSwitch=(len(lessThanK))

# len([i if i<indexOfK else None for i in moreThanK.keys()])

print(len([i if i>indexOfK else None for i in lessThanK.keys()])+len(arr)-(len(lessThanK)+len(moreThanK))-1)

print(  (indexOfK-len([i if i<indexOfK else None for i in lessThanK.keys()]))     )

