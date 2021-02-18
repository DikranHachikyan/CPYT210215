# %%
s1 = 'hello'
s2 = 'hello'

id(s1) == id(s2)
# %%
class Point:
    def __init__(self,x):
        self.x = x
# %%
p1 = Point(x = 10)
p2 = Point(x = 10)

# %%
id(p1) == id(p2)
# %%
id(p1.x) == id(p2.x)

# %%

s1 = 'hello' * 3000
s2 = 'hello' * 3000

id(s1) == id(s2)
# %%
