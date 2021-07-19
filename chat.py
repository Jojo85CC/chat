

def read_file(filename):
	lines = []
	with open(filename,'r',encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines):
	new = []
	person = None #預設值 無.假如txt第一行沒人名
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:	
			new.append(person + ': ' + line)
	return new

def write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt',lines)


main()

#with open('output.txt','w') as f:
		#f.write('商品,價格\n')
		#for p in d:
			#f.write(p[0]+ ',' + str(p[1]) +'\n') #'\n'換行

#if line == 'Alan':
			#print(':')
        #elif line == 'Tom':
        	#print(':')