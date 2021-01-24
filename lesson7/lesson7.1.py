# Первый вариант, когда создаётся новая матрица-сумма как объект, но тогда нельзя написать просто print(a+b)
# class Matrix:
#     def __init__(self,l):
#         self.data=l
#     def __str__(self):
#         lout2=''
#         for l1 in self.data:
#             lout1 = ''
#             for l2 in l1:
#                 lout1=lout1+' '+str(l2)
#             lout2=lout2+'\n'+lout1
#         return lout2
#     def __add__(self,other):
#         new=[]
#         for i in range(len(self.data)):
#             newline=[]
#             for j in range(len(self.data[i])):
#                 newline.append(int(self.data[i][j])+int(other.data[i][j]))
#             new.append(newline)
#         return(new)
#
#
# m1=[3,5,32]
# m2=[2,4,6]
# m3=[-1,64,-8]
# m=[m1,m2,m3]
# k1=[3,5,32]
# k2=[2,4,6]
# k3=[-1,64,-8]
# k=[k1,k2,k3]
# a=Matrix(m)
# b=Matrix(k)
# print(a)
# print(b)
# c=Matrix(a+b)
# print(c)

# Второй вариант, когда не создаётся новый объект, а тупо выводится сумма двух матриц
class Matrix:
    def __init__(self,l):
        self.data=l
    def __str__(self):
        lout2=''
        for l1 in self.data:
            lout1 = ''
            for l2 in l1:
                lout1=lout1+' '+str(l2)
            lout2=lout2+'\n'+lout1
        return lout2
    def __add__(self,other):
        new=''
        for i in range(len(self.data)):
            newline=''
            for j in range(len(self.data[i])):
                newline=newline+' '+str(int(self.data[i][j])+int(other.data[i][j]))
            new=new+'\n'+newline
        return(new)


m1=[3,5,32]
m2=[2,4,6]
m3=[-1,64,-8]
m=[m1,m2,m3]
k1=[3,5,32]
k2=[2,4,6]
k3=[-1,64,-8]
k=[k1,k2,k3]
a=Matrix(m)
b=Matrix(k)
print(a)
print(b)
print(a+b)