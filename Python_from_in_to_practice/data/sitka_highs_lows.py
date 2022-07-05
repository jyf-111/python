import csv
import matplotlib.pyplot as plt
from datetime import datetime
 
# filename = "Python_from_in_to_practice/data/sitka_weather_07-2014.csv"
filename = "Python_from_in_to_practice/data/sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    print(highs)

print(header_row[:5])
# for index,column_header in enumerate(header_row[:10]):
#     print(index,column_header)

# from datetime import datetime
# first_data = datetime.strptime("2022-7-3",'%Y-%m-%d')
# print(first_data)


fig,ax = plt.subplots()
ax.plot(dates,highs,c='red',alpha = 0.5)
ax.plot(dates,lows,c='blue',alpha = 0.5)

ax.fill_between(dates,highs,lows,facecolor='blue',alpha = 0.1)

ax.set_title("2018年7月每日最高温度",fontsize=24)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel('温度(F)',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

fig.autofmt_xdate() # 绘制倾斜日期

plt.show()

