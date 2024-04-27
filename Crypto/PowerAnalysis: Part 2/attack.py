from pwn import *
import numpy as np
import scared

context.log_level = 'error'


my_index = 0

list = []
formats = []
index = ''
for i in range(0, 100):
	
	index = str(i)
	if i < 10:
		index = '0' + str(i)
		
	with open('traces/trace' + index + '.txt') as openfileobject:
		for line in openfileobject:
			if "text" in line:
				plaintext = line.split(": ")[1]
				plaintext = bytearray.fromhex(plaintext)
				plaintext = np.frombuffer(plaintext, dtype=np.uint8)
				formats.append(plaintext)
			else:
				traces = line.split("[")[1]
				traces = traces.split("]")[0]
				traces = traces.split(", ")
				traces = [int(x) for x in traces] 
				list.append(traces)
				
		
	
ths = scared.traces.read_ths_from_ram(samples=np.array(list), plaintext=np.array(formats))

attack = scared.CPAAttack(selection_function=scared.aes.selection_functions.encrypt.FirstSubBytes(), 
                          model=scared.HammingWeight(), 
                          discriminant=scared.maxabs)
attack.run(scared.Container(ths))
found_key = np.nanargmax(attack.scores, axis=0).astype('uint8')
print(found_key.tobytes().hex())

