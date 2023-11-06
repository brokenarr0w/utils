# 这个程序用来修改抓包来的我在校园的json数据
# 由于经常性的导员不批假或者早上7点提交的下午6点才批。我都**的请假时间过了还用你批？
import json
import datetime
import random
import os
print(os.getcwd())
year = eval(input("请输入您想请假的年数(以4位格式)\n"))
month = eval(input("请输入您想请假的月份\n"))
day = eval(input("请输入您想在这个月的那一天请假\n"))
time = eval(input("请输入您想请假几天\n"))
reason = input("请输入你的请假理由（如果为空的话默认为扁桃体发炎）:")
if reason == '':
    reason = '扁桃体发炎'
print(reason)
x = datetime.datetime(year, month, day, 8, 00)
y = x + datetime.timedelta(days=time)
z = x + datetime.timedelta(hours=-2)
m = datetime.datetime(year, month, day, 7, 00) + datetime.timedelta(minutes=random.randint(1, 60))
beginTime = x.strftime('%Y-%m-%d %H:%M')
endTime = y.strftime('%Y-%m-%d %H:%M')
submitTime = z.strftime('%Y-%m-%d %H:%M')
agreeTime = m.strftime('%Y-%m-%d %H:%M')

print('当前假期开始时间：{}，当前假期结束时间：{}'.format(beginTime, endTime))
with open('数据.json', encoding='UTF-8') as f:
    data = json.load(f)
data['data']['leaves']['beginTime'] = beginTime
data['data']['leaves']['endTime'] = endTime
data['data']['leaves']['finalTime'] = endTime
data['data']['leaves']['reason'] = reason
data['data']['leaves']['submitTime'] = submitTime
data['data']['approveList'][0]['createTime'] = submitTime
data['data']['approveList'][1]['createTime'] = agreeTime
with open('处理结果.json', 'w+', encoding='UTF-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
