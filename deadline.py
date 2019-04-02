#job sequencing with deadlines

def inser_profit(max_profit,profit_array,D,i):             #Recursive_function that put profit in max_profit_array
    if max_profit[D-1]==0:
        max_profit[D-1]=profit_array[i]
        return
    else:
        inser_profit(max_profit,profit_array,D-1,i)
if __name__=='__main__':
    deadline=[5,3,3,2,4,2]                              # input() for deadline
    profit_array=[200,180,190,300,120,100]              # input() for profit per job
    max_deadline=max(deadline)
    max_profit_array=[0]*max_deadline
    index=[i for i in range(0,len(profit_array))]
    index.sort(key=lambda x:profit_array[x],reverse=True)
    print(index)
    for x,i in enumerate(index):
        if x<max_deadline:
            inser_profit(max_profit_array,profit_array,deadline[i],i)
        else:
            print(sum(max_profit_array))

