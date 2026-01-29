def sort_by_value(item):
    return item[0]#value(profit)
def sort_by_weight(item):
    return item[1]#weight
def sort_by_ratio(item):
    return item[0]/item[1]#value/weight
def fractional_knapsack(W,items,strategy='ratio'):
    if strategy=='value':
        items.sort(key=sort_by_value,reverse=True)
    elif strategy=='weight':
        items.sort(key=sort_by_weight)
    elif strategy=='ratio':
        items.sort(key=sort_by_ratio,reverse=True)
    total_value=0.0
    result_items=[]
    for value,weight in items:
        if W==0:
            break
        if weight<=W:
            total_value+=value
            W-=weight
            result_items.append((value,weight,1.0))
        else:
            fraction=W/weight
            total_value+=value*fraction
            result_items.append((value,weight,fraction))
            W=0
            #print detailed result
    print(f'\nStrategy:{strategy.upper()}')
    print(f'\total profit{total_value:2f}')
    print('items taken(value,weight,fraction):')
    for v,w,f in result_items:
        print(f'value{v},weight{W},fraction{f:.2f}')
    return total_value
#(profit,weight) for ob 
items=[(5,1),(10,3),(15,5),(7,4),(8,1),(9,3),(4,2)]
W=15
#make a fresh copy each time to avoid side effects
print('max value',fractional_knapsack(W,items.copy(),'value'))
print('greedy by min weight',fractional_knapsack(W,items.copy(),'weight'))
print(fractional_knapsack(W,items.copy(),'ratio'))
