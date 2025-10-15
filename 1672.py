#richest customer wealth 

def maximumWealth(accounts: list[list[int]]) -> int:
    maxWealth = 0
    for i in range(len(accounts)):
        totalWealth = sum(accounts[i])
        maxWealth = max(maxWealth, totalWealth)
    return maxWealth
    
solution = maximumWealth(accounts=[[1,2,3],[3,2,1]])
print(solution)
