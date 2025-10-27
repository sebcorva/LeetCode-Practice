#richest customer wealth 

def maximumWealth(self, accounts):
        best_wealth = 0
        for i in range(len(accounts)): #we use range(len(accounts)) to iterates through all the accounts(list of customers) ( in this case it was two)
            totalWealth = sum(accounts[i]) #then we sum all the items of the list i was in the iteration
            best_wealth = max(best_wealth, totalWealth) #max() compare two values and return the max value
        return best_wealth
    
solution = maximumWealth(accounts=[[1,2,3],[3,2,1]])
print(solution)
