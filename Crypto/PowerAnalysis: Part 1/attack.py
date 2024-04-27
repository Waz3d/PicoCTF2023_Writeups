from pwn import *
import numpy as np
import scared

context.log_level = 'error'

host = "saturn.picoctf.net"
port = 56134

my_index = 0

list = []
formats = []
for i in range(0, 300):
	
	plaintext = np.random.randint(0, 256, 16, dtype='uint8')
	formats.append( plaintext )
	c = remote(host, port)
	plaintext = plaintext.tobytes().hex()
	c.sendline(plaintext)
	
	res = c.recvline()
	#print(res)
	res = str(res)
	res = res.split("[")[1]
	res = res.split("]")[0]
	res = res.split(", ")
	res = [int(x) for x in res] 	# convert string values into list of integers
	
	list.append(res)
	c.close()
		
		
ths = scared.traces.read_ths_from_ram(samples=np.array(list), plaintext=np.array(formats))

attack = scared.CPAAttack(selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(), 
                          model=scared.HammingWeight(), 
                          discriminant=scared.maxabs)
attack.run(scared.Container(ths))
found_key = np.nanargmax(attack.scores, axis=0).astype('uint8')
print(found_key.tobytes().hex())

