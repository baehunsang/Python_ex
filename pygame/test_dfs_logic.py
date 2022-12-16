map = [
    # '/' 는 bubble이 들어갈 수 없는 곳
    # '.' 은 빈칸
            list("RRYYBBGG"),
            list("RRYYBBG/"), 
            list("BBGGRRYY"),
            list("BGGRRYY/"),
            list(".....Y.."),
            list("......./"),
            list("........"),
            list("......./"),
            list("........"),
            list("......./"),
            list("........")
        ]

MAP_ROW = 11
MAP_COL = 8

def remove_adj_bubble(map, row, col, color):
    visited = []
    def visit(map, row, col, color):
        if row < 0 or row >= MAP_ROW or col < 0 or col >= MAP_COL:
            return
        curr_color = map[row][col]
        if curr_color != color:
            return
        if (row, col) in visited:
            return 

        if curr_color in [".", "/"]:
            return

        visited.append((row, col))

        if row % 2 ==1:
            visit(map, row, col+1, color)
            visit(map, row, col-1, color)
            visit(map, row+1, col, color)
            visit(map, row-1, col, color)
            visit(map, row+1, col+1, color)
            visit(map, row-1, col+1, color)
        
        visit(map, row, col+1, color)
        visit(map, row, col-1, color)
        visit(map, row+1, col, color)
        visit(map, row-1, col, color)
        visit(map, row-1, col-1, color)
        visit(map, row+1, col-1, color)
        
    visit(map, row, col, color)
    return visited

remove_adj_bubble(map, 4,5, "Y")

for row in map:
    for col in row:
        print(col+" ", end="")
    print("")


