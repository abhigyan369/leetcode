class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        items = []
        for i in range(len(val)):
            ratio = val[i] / wt[i]
            items.append((val[i], wt[i], ratio))
            
        items.sort(key=lambda item: item[2], reverse=True)
        
        profit = 0.0
        
        for item in items:
            value = item[0]
            weight = item[1]
            
            if weight <= capacity:
                profit += value
                capacity -= weight
            else:
                profit += value * (capacity / weight)
                break
        return profit
            
            