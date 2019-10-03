def getSolution(inp):
	from collections import defaultdict
	import math
	import random
	import pprint

	def read_grid():
		f = open("inp.txt", "r")
		grid=[]
		for x in f:
			grid.append(list(map(int,x.strip().split())))
		return(grid)

	def input_blocks(grid):
		written_blocks=defaultdict(lambda : 0)
		for i in range(9):
			for j in range(9):
				if(grid[i][j]!=0):
					written_blocks[(i,j)] = grid[i][j]

		return(written_blocks)


	def isPossibleTowrite(grid,x,y,written_blocks):
		return(not(written_blocks[(x,y)]))


	def numbersWritable(grid,x,y,written_blocks):
		if(not isPossibleTowrite(grid,x,y,written_blocks)):
			return([grid[x][y]])

		blocks={0:0,1:0,2:0,3:3,4:3,5:3,6:6,7:6,8:6}
		all_nums=set(list(range(1,10)))
		###################BLOCK LEVEL############
		nums_b=set()
		possible_in_blks=set()
		for row in range(blocks[x],blocks[x]+3):
			for col in range(blocks[y],blocks[y]+3):
				if(grid[row][col]==0):
					continue
				nums_b.add(grid[row][col])
		possible_in_blks=all_nums-nums_b
		##########################################
		#print('blocks',possible_in_blks)

		###############ROW LEVEL################
		nums_r=set()
		possible_in_row=set()
		for col in range(0,9):
			if(grid[x][col]==0):
					continue
			nums_r.add(grid[x][col])
		possible_in_row=all_nums-nums_r
		##########################################
		#print('row',possible_in_row)

		##############COL LEVEL################
		nums_c=set()
		possible_in_col=set()
		for row in range(0,9):
			if(grid[row][y]==0):
					continue
			nums_c.add(grid[row][y])
		possible_in_col=all_nums-nums_c
		#########################################
		#print('col',possible_in_col)


		return(sorted(list(possible_in_blks.intersection(possible_in_row).intersection(possible_in_col))))


	def fun(grid, i, j):
		#print(i, j)
		m= len(grid)- 1
		flag= 0
		if (i, j)== (m, m) and len(numbersWritable(grid, i, j, written_blocks))== 1:
			grid[i][j]= numbersWritable(grid, i, j, written_blocks)[0]
			return grid
		l= numbersWritable(grid, i, j, written_blocks)
		print(l)
		for k in l:            
				flag= 1
				print('-'*80)
				print(k, i, j)
				grid[i][j]= k
				if j== m:
					i= i+ 1
					j= -1
				if fun(grid, i, j+ 1)== -1:
					continue
				else:
					return fun(grid, i, j+ 1)
		if grid[i][j]!= 0 and flag== 0:
			if j== m:
				i= i+ 1
				j= -1        
			return fun(grid, i, j+1)
		return -1

	def backtrack_sudoko(grid,row,col):
		if((row,col)==(8,8) and len(numbersWritable(grid, row, col, written_blocks))== 1):
			grid[row][col]= numbersWritable(grid, row, col, written_blocks)[0]
			return(True)
		elif((row,col)==(8,8) and len(numbersWritable(grid, row, col, written_blocks))== 0):
			return(False)

		if col == 9:
			row = row + 1
			col = 0
			
		possiblities= numbersWritable(grid, row, col, written_blocks)
		if(possiblities==[]):
			return(False)
			
		for ele in possiblities:
			grid[row][col]=ele
			if(backtrack_sudoko(grid,row,col+1)):
				return(True)
			grid[row][col]= written_blocks[(row,col)]
		return(False)
			

		

	global grid 
	grid= inp.copy()

	global written_blocks
	written_blocks= input_blocks(grid)
	#print(numbersWritable(grid,8,6,written_blocks))
	backtrack_sudoko(grid,0,0)
	#pprint.pprint(grid)
	return(grid)
		
		
