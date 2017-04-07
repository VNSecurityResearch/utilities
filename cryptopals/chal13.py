
def profile_for(s):
	isString = isinstance(s,str)
	if isString == False:
		return None
	# check legit string
	while '&' in s:
		s = s.replace('$','')
	while '=' in s:
		s = s.replace('=','')

# this is 1 dump challenge