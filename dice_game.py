while True:    
    import dice
    print('サイコロゲームを始めます\n終了するにはEnterキーを押してください')
    n=input('4,6,8,12,20のサイコロがあります\nどれで勝負しますか？:')
    if len(n)==0:
        print('終了します')
        break
    while True:
        try:  
            n=int(n)  
            my_dice=dice.Dice(n)
            CPU_dice=dice.Dice(n)
            my_pip=my_dice.shoot()
            CPU_pip=CPU_dice.shoot()

            print('CPU:{:d}'.format(CPU_pip))
            print('あなた:{:d}'.format(my_pip))

            if CPU_pip < my_pip:
                print('おめでとうございます！！あなたの勝ちです')
                break
            elif CPU_pip==my_pip:
                temp=input('引き分けです、、もう一度！！')
            else :
                print('残念、、、あなたの負けです、、、')
                break
        except:
            print('半角数字で4,6,8,12,20から選んでください')
            input('4,6,8,12,20のサイコロがあります\nどれで勝負しますか？:')

    break