def int_func(text):
    return ''.join([text[0].upper(),text[1:len(text)]])

l='dsfdsfds sfds dfdsfe2wwf fdgdgfa sfgggdfd'
lnew=l.split(' ')
res=[]
for i in lnew:
    res.append(int_func(i))
print(' '.join(res))