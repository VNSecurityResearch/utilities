def uncheckPKCD7(data):
	if isinstance(data,str) == False:
		raise ValueError
	i = data[-1]
	t = ord(i)
	if data[-t:] == i * t:
		return data[:-t]
	else:
		raise ValueError

print uncheckPKCD7("ICE ICE BABY\x04\x04\x04\x04")