#%%
a = [1,2,3,4,]
a.append(5)
print(a)
# %%

def test():
    pass

class Person:
    pass
bob = Person()
cathy = Person()

a = list()
b = list()
# %%
# 생성자 
class Person:
    def __init__(self):
        print(self,'is generated')
        self.name = 'Kate'
        self.age = 10
p1 = Person()
p2 = Person()

p1.name = 'arron'
p1.age = 20
print(p1.name, p1.age)
# %%
# %%
class Person:
    def __init__(self,name,age):
        print(self,'is generated')
        self.name = name
        self.age = age
p1 = Person('Bob',30)
p2 = Person('Kate',20)

print(p1.name,p1.age)
print(p2.name, p2.age)
# %%
