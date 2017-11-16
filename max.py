#coding = utf-8
a = [1,2,3,6,8,9,11,22,345,6543,46789,333,69,9874,99999643]
max_a = 0
sec_b = 0
for i in a:
	if i > max_a:
		sec_b = max_a 
		max_a = i
	elif i > sec_b:
		sec_b = i
print "max is %s,%s" %(max_a,sec_b)



