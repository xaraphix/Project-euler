def read_file():
	file_67 = open('triangle.txt','r')
	triangle_array = []
	for j in file_67:
		triangle_array.append([int(i) for i in j.split(' ')])
	return triangle_array
def max_sum(q):
	for i in range(len(q)-1,0,-1):
		for j in range(0,len(q[i])-1):
			q[i-1][j] = q[i-1][j] + max(q[i][j],q[i][j+1])

	return q[0][0]

if __name__ == '__main__':
	print max_sum(read_file())




