def spaces_to_http(s):
	new_str = ""
	for i in range(len(s)):
		if s[i]==" ": 
			new_str += "%20"
		else:
			new_str += s[i]

	return new_str
print spaces_to_http("hey whats up")