s=input()
t=input()
if (leng(s)!=leng(t)):
	print("False")
s_dict={}
t_dict={}
z=len(s)
for i in range(z):
	if s[i] in s_dict.keys() and s_dict[s[i]] != t[i]:
		print("False")
	if t[i] in t_dict.keys() and t_dict[t[i]] != s[i]:
		print("False")
	s_dict[s[i]]=t[i]
	t_dict[t[i]]=s[i]
print("True")
