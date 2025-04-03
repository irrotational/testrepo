from numpy.random import randint

def mangle_string(input_string,N):
	str_len = len(input_string)
	idxs_to_mangle = [ randint(0,str_len-1) for i in range(N) ]
	idxs_to_mangle = set(idxs_to_mangle)
	out_string = ""
	for i,ch in enumerate(input_string):
		if (i in idxs_to_mangle):
			ascii_num = randint(97,122)
			out_string += chr(ascii_num)
		else:
			out_string += ch
	return out_string
