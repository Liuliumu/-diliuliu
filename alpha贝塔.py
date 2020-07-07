choice = int(input('请输入您的选择：'))
if  choice==1:
    print('霍格沃茨欢迎您的到来')

else:
    print('您可是被梅林选中的孩子，我们不接受这个选项')
  



answer=input('您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？')
if answer=='需要':
    choice=input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询')
   
    if choice=='1':
        print('去存取款窗口叭')
   
    elif choice=='2':
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        money=input('请问您需要兑换多少金加隆呢？')
        print('好的，我知道了，您需要兑换'+money+'金加隆。')
        print('那么，您需要付给我'+str(int(money)*51.3)+'人民币')
    else:
         print('去咨询窗口叭')
            
else:
    print('好的，再见。')

#华氏温度摄氏温度转换
Apple=input(请输入代码)
if Apple[-1] in ['F','f']:
    C=(eval(Apple[0:-1])-32)/1.8
    print('{:.2f}C'.format(C))
elif Apple[-1] in ['C','c']:
    F=eval(Apple[0:-1])*1.8+32
    print('{:.2f}F'.format(F))
else:
    print('输入格式错误')
