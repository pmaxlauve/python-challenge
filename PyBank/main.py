

filepath = "C:\\Users\\pmaxl\\OneDrive\\Desktop\\BootCamp\\Homework\\wk3_HW\\python-challenge\\PyBank\\Resources\\PyBank_data.csv"




import pandas as pd

bank_data = pd.read_csv(filepath)


total_months = len(bank_data["Date"])



acc_profit_loss = sum(bank_data["Profit/Losses"])


    
        
        
Profit_Change = [0]

for i in range(len(bank_data["Profit/Losses"]) - 1):
    
    
    month_change = int(bank_data["Profit/Losses"][i+1] - bank_data["Profit/Losses"][i])
    Profit_Change.append(month_change)



bank_data["Profit Change"] = Profit_Change
avg_change = bank_data["Profit Change"].mean()
avg_change_rounded = "{:.2f}".format(avg_change)



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











