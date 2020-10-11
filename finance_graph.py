from oauth2client.service_account import ServiceAccountCredentials
import gspread

import pandas as pd
import datetime
from matplotlib import pyplot as plt

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'C:/Users/customer/Desktop/investment_program/invest-292113-cd0f11733463.json', scope)
gc = gspread.authorize(credentials)

gc1 = gc.open("finance_data").worksheet('KOSPI')
gc2 = gc1.get_all_values()
kospi_data = pd.DataFrame(gc2[1:], columns = gc2[0])

# print(kospi_data)



# Data 전처리
for i in range(len(kospi_data)):
    year = int(kospi_data["Date"][i].split(".")[0])
    month = int(kospi_data["Date"][i].split(".")[1])
    date = int(kospi_data["Date"][i].split(".")[2].split(" ")[1])
    kospi_data['Date'][i] = datetime.date(year, month, date)


def show_graph(data, interaval = 1):
    # print(kospi_data['Date'])
    # print(datetime.date(2015,10,12))
    condition1 = data['Date'] >= datetime.date(2015,10,12)


    
    # print(condition1)

    print(data['Close'][condition1])
    plt.title("KOSPI_INDEX")
    plt.ylabel("KOSPI")
    plt.xlabel("Date")
    plt.plot(data['Close'][condition1], data['Date'][condition1])   
    plt.show()


show_graph(kospi_data)