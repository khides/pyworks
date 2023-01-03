while True: ###breakするまで以下を繰り返す
    print('終了するにはEnterキーを押します')
    height=input('身長は？:')  
    if len(height)==0:
        print('終了します')
        break ###身長が入力されずenterが押されたら終了
    while True:
        try:      
            height=float(height) ###シェルからの入力は文字列型なので小数型に変換
            if height<100:
                height=height
            else:
                height=height/100 ###もしcmで入力されたら、mに直す
            break
        except:
            print('半角数字で入力してください') ###エラーが起きたらもう一度
            height=input('身長は？')
        
    weight=input('体重は？:')
    if len(weight)==0:
        print('終了します')
        break ###体重が入力されずenterが押されたら終了
    while True:
        try:    
            weight=float(weight)
            break
        except:
            print('半角数字で入力してください')
            weight=input('体重は？')
    
    bmi=weight/ pow(height,2)

    print('BMIは{:.1f}です'.format(bmi))
    if bmi<18.5:
        print('少しやせすぎです')
    elif bmi <25.0:
        print('標準的な体形です')
    elif bmi<30.0:
        print('少し太っています')
    else :
        print('高度の肥満です')

    end=input('終了するにはEnterキーを押します')
    if len(end)==0:
        print('終了します')
        break
