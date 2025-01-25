import pgzrun
cxk = False
print('--------------------------------------------------------------------------------')
music.play('蔡徐坤完整版')
WIDTH, HEIGHT = 600, 316
bg = Actor('蔡徐坤篮球背景1.png', (WIDTH / 2, HEIGHT / 2))
kun = Actor('蔡徐坤.png', (WIDTH / 2, HEIGHT / 2))
def draw():
    bg.draw()
    kun.draw()
def on_key_down(key):
    print('按下',key)
    if cxk:
        if key == keys.J:
            print('J被按下了')
            print('只因')
            music.play_once('鸡')
        elif key == keys.N:
            print('N被按下了')
            print('你')
            music.play_once('你')
        elif key == keys.T:
            print('T被按下了')
            print('太')
            music.play_once('太')
        elif key == keys.M:
            print('M被按下了')
            print('美！')
            music.play_once('美')
        elif key == keys.LCTRL or key == keys.RCTRL:
            print('Ctrl被按下了')
            print('唱跳rap篮球')
            music.play_once('唱跳rap篮球')
        else:
            print('你干嘛嗨嗨哎哟~')
            music.play_once('你干嘛嗨嗨哎哟~')
    else:
        if key == keys.C:
            print('C被按下了')
            print('唱')
            music.play_once('唱')
        elif key == keys.T:
            print('T被按下了')
            print('跳')
            music.play_once('跳')
        elif key == keys.R:
            print('R被按下了')
            print('Rap')
            music.play_once('rap')
        elif key == keys.L:
            print('L被按下了')
            print('篮球')
            music.play_once('篮球')
        elif key == keys.LCTRL or key == keys.RCTRL:
            print('Ctrl被按下了')
            print('唱跳rap篮球')
            music.play_once('唱跳rap篮球')
        else:
            print('你干嘛嗨嗨哎哟~')
            music.play_once('你干嘛嗨嗨哎哟~')
pgzrun.go()