

def read_file(filename):
	lines = []
	with open(filename,'r',encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines):
	person = None #預設值 無.假如txt第一行沒人名
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_pic_count = 0
	viki_pic_count = 0

	for line in lines:
		s = line.split(' ')#遇到空白建做切割並成為清單
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_pic_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_pic_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen說了',allen_word_count)
	print('allen傳了',allen_sticker_count,'個貼圖',allen_pic_count,'張圖片')
	print('Viki說了',viki_word_count)
	print('viki傳了',viki_sticker_count,'個貼圖',viki_pic_count,'張圖片')


	#return lines


def write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt',lines)


main()
