stonenumber=0
if(stonenumber>=6):
    print('你拥有了毁灭宇宙的力量')
elif(0<stonenumber<=5):
    print('绯红女巫需要亲手毁掉幻视额头上的心灵宝石')
else:
    print('需要惊奇队长逆转未来')
historyscore=26

if historyscore>=60:
    print('你已经及格')

    if historyscore>=80:
        print('你很优秀')

    else:
        print('你只是一般般')

else:
    print('不及格')
    if historyscore<30:
        print('学渣')
    else:
            print('还能抢救一下')
 

salary=80
if salary<=500:
    print('欢迎进入史塔克穷人帮前三名')
    if 100<salary<500:
        print('请找弗瑞队长加薪')
    else:
        print("恭喜您荣获'美元队长'称号！")
elif 500<salary<=1000:
    print('祝贺您至少可以温饱了。')
else:
    print('经济危机都难不倒您！')
    if 1000<salary<=20000:
        print('您快比钢铁侠有钱了！')
    else:
        print('您是不是来自于瓦坎达国？')
print('程序结束')
