# a=[1,1,2,2,3,3,4,5,6,7,8,9,10]
#
# # convert this to set
# # iterate a loop compare each one
# b=[]
#
# for i in a:
#     if i not in b:
#         b.append(i)
#
#
#
# # find the pair with sum 7
# c=[3,5,2,-4,8,11]
d=[-4,2,3,5,7,8,11]

# nested loops and verify the sum
#

#
#
# for i in range(0,len(d)):
#     if(d[i]>7):
#         break
#     for j in range(i+1,len(d)):
#         if d[i]+d[j]>7:
#             break
#         elif d[i]+d[j]==7:
#             print(d[i],d[j])

e={}
# first approach
for i in d:
    if(i>7):
        break
    elif (7-i in d):
        print(i,7-i)

# second approach
print("second approach :")
for i in d:
    if (7-i in e):
        print(i,7-i)
    else:
        e[i]=1