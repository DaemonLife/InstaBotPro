import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
import traceback

from lib import read_file

import bot_1_2, bot_3, bot_4, bot_5

# Create app
app = QtWidgets.QApplication(sys.argv)






# init app
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

login = read_file('login.txt')
ui.username.setText(login[0])
ui.password.setText(login[1])

MainWindow.show()

# logic
def start():

    login = [str(ui.username.text()), str(ui.password.text())]

    if (login[0] != '') and (login[1] != ''):
        with open('login.txt', 'w') as f:
            print(login[0], file=f)
            print(login[1], file=f)
    else:
        pass

    max_users = int(ui.max_users.text())
    pause_time = int(ui.pause_time.text())
    post_num = int(ui.post_num.text())

    device = ui.list_device.currentRow()
    d = [ # devices
        'iPhone X',
        'Galaxy S5',
        'Pixel 2',
    ]
    device = d[device]

    if ui.subscribe_on.checkState() == 2: # activated
        subscribe_on = True
    else: # deactivated
        subscribe_on = False

    if (ui.likes_on.checkState() == 2) and (ui.comments_on.checkState() == 2):
        mod = 'all'
    elif (ui.likes_on.checkState() == 2):
        mod = 'likes'
    elif (ui.comments_on.checkState() == 2):
        mod = 'comments'
    else:
        mod = None
 
    variant = int(ui.list_operation.currentRow()) + 1

    # print(f'max users {max_users}, pause time {pause_time}, post num {post_num}, device {device}, subcribe on {subscribe_on}, mod {mod}, variant {variant}, login {login}')

    if variant == 1: # * парсер подписчиков
        bot_1_2.main(bot_num=1, pause_time=pause_time, max_users=max_users, device=device)
    elif variant == 2: # * парсер подписок
        bot_1_2.main(bot_num=2, pause_time=pause_time, max_users=max_users, device=device)
    elif variant == 3: # * лайки и подписка
        bot_3.main(post_num=post_num, subscribe_on=subscribe_on, max_users=max_users, pause_time=pause_time, device=device)
    elif variant == 4: # * отписка
        bot_4.main(pause_time=pause_time, device=device)
    elif variant == 5: # * сбор активности аудитории
        bot_5.main(post_num=post_num, pause_time=pause_time, max_users=max_users, mod=mod, device=device)

    # print('Bot started!')

try:
    ui.button_start.clicked.connect(start)
    # exit
    sys.exit(app.exec_())
except:
    pass
