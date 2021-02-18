# %%
connection = dict(
    host='localhost', 
    keep_alive=True,
    db='northwind',
    port=3306
)
# %%
connection['db']
# %%
# лоша идея!!
conn = ['localhost', True, 'northwind',3306]
conn[2]
# %%
user = {
    'last_name':'Smith',
    'first_name':'Anna',
    'age':30,
    'mail':'anna@no.com'
}

user['age']
# %%
user.keys()
# %%
user.values()
# %%
user.items()
# %%
user['phone']
# %%
'phone' in user
# %%
user.get('phone', '000-00-00')
# %%
