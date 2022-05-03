# emp table with
#     id name intern_salary intern_age

# select sum(intern_salary)/count(intern_salary) as average_salary for emp;
#
# class emp:
#
#     def findAsubString (self,ss,entstring):
#         for i in range(len(ss)-1,1,-1):
#             temp=ss[0,i]
#             if (temp in entstring):
#                 print(temp)
#                 return temp
#                 break


def findAsubString1 (ss,entstring):
    for i in range(len(ss),1,-1):
        temp=ss[:i]
        if (temp in entstring):
            # print(temp)
            return temp
            break


# app and apple


print(findAsubString1("appl1en","apple"))
