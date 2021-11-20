"""
The well known idea of solving N- queen is remenbering the position of queen.
In this situation, the diagonal position is hard to save.
    0 1 2 3         0  1  2 3
  0 0 1 2 3      0  0  1  2 3
  1 1 2 3 4      1 -1  0  1 2
  2 2 3 4 5      2 -2 -1  0 1
  3 3 4 5 6      3 -3 -2 -1 0
  
  This is the way of detacting diagonal position of queen.
  If queens are in same diagonal, each queen has same row + col index or row - col index.
  
"""
def generate_board(n: int):
	#
	if(n == 0):
		return []
	ret = []
	board = [["."]*n for _ in range(n)]
	col , Diag1, Diag2 = set(), set(), set()	
	def dfs(r):
		if(r == n):
			cboard = ["".join(row) for row in board]
			ret.append(cboard)
			return
		for c in range(n):
			if not c in col and not r + c in Diag1 and not r - c in Diag2:
				board[r][c] = 'Q'
				col.add(c)
				Diag1.add(r + c)
				Diag2.add(r - c)
				dfs(r + 1)
				board[r][c] = '.'
				col.remove(c)
				Diag1.remove(r + c)
				Diag2.remove(r - c)
	dfs(0)
	return ret
for board in generate_board(5):
	for row in board:
		print(row ,end="\n")
	print(end="\n")
	
print(len(generate_board(5)))
	

			   	
		
		
