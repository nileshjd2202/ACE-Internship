from collections import OrderedDict

dict1 = OrderedDict([('akshat','1'),('nikhil','2')])

dict1.update({'manjeet':'3'})
dict1.move_to_end('manjeet', last=False)

print(dict1)