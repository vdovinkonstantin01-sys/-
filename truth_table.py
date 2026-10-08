def truth_table(n) :
    table=[]
    for mask in range (1 << n):
        row =[]
        for i in range (n-1,-1,-1):
            
            row.append((mask>>i)&1)
        table.append(tuple(row))
    return table
        
