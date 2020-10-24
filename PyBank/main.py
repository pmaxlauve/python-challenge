
    #file path name
filepath = "C:\\Users\\pmaxl\\OneDrive\\Desktop\\BootCamp\\Homework\\wk3_HW\\python-challenge\\PyBank\\Resources\\PyBank_data.csv"



    #import pandas
import pandas as pd

    #read filepath csv
bank_data = pd.read_csv(filepath)

    #determine total months
total_months = len(bank_data["Date"])


    #determine total profits/losses
acc_profit_loss = sum(bank_data["Profit/Losses"])

        
      #initialize 'Profit_Change' with 0 in the first row since we dont have previous data
Profit_Change = [0]


    #iterate over 'Profit/Losses'
for i in range(len(bank_data["Profit/Losses"]) - 1):
    
        #determine change from month to month
    month_change = int(bank_data["Profit/Losses"][i+1] - bank_data["Profit/Losses"][i])
    
        #append to 'Profit_Change'
    Profit_Change.append(month_change)


    #add 'Profit Change' to the 'bank_data' DF
bank_data["Profit Change"] = Profit_Change

    #calculate the mean of 'bank_data["Profit Change"]'
avg_change = bank_data["Profit Change"].sum()/85

    #format 'avg_change'
avg_change_rounded = "{:.2f}".format(avg_change)


    #print report
print("Financial Analysis")
print("----------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${acc_profit_loss}')
print(f'Average Change: ${avg_change_rounded}')

    
for row in range(len(bank_data["Profit Change"])):
    if bank_data["Profit Change"][row] == bank_data["Profit Change"].max():
        print(f'Greatest increase in profits: {bank_data["Date"][row]} (${bank_data["Profit Change"][row]})')
    
    if bank_data["Profit Change"][row] == bank_data["Profit Change"].min():
        print(f'Greatest decrease in profits: {bank_data["Date"][row]} (${bank_data["Profit Change"][row]})')











