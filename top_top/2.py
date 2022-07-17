import time
from concurrent.futures import ThreadPoolExecutor


def t_1(time_=1, y='www:'):
	for i in range(1, 5):
		time.sleep(time_)
		print(y, i)


o = ['a', 'b', 'c', 'd']
#
# with ThreadPoolExecutor(4) as t:
# 	for i in o:
# 		t.submit(t_1, 5, i)
k = []
for i in range(1, 152):
	k.append(i)


for f in k:
	
	if f == k[-1::]:
		print(f)
		break
	else:
		print(f)

print(k[-1::])
hh = k[-1::]
print(type(k[-1::]))
print(type(hh))
print(int(str(hh)))
print(str(hh))
print(hh)
print(type(hh))
#print(int(hh))
print(type(hh))
