#job sequencing with deadlines

def inser_profit(max_profit,profit_array,D,i):             #Recursive_function that put profit in max_profit_arra
    if D>=0:
        if max_profit[D-1]==0:                                 #D is a deadline, and "D-1" happen because index of max_profitt_array start 
            max_profit[D-1]=profit_array[i]                    #--with 0 index but deadline does not contain 0
            return
         else:
             inser_profit(max_profit,profit_array,D-1,i)
      else:
        return
if __name__=='__main__':
    job_profit={200:'j1',180:'j2',190:'j3',300:'j4',120:'j5',100:'j6'}  #don't put same value of profit
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
    # print start the real thing
    print("sequence of job for max profit","==",[job_profit[i] for i in max_profit_array] )
    print("maximum profit","==",sum(max_profit_array))

