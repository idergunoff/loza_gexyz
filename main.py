import os
import sys
import traceback
import pandas as pd

from PyQt5.QtWidgets import QFileDialog
from loza_gexyz_window import *




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_loza_gexyz()
ui.setupUi(MainWindow)

MainWindow.show()


def choose_file():
    try:
        file_name = QFileDialog.getOpenFileName(caption='Выберите общий файл привязки', filter='*.txt')[0]
        ui.lineEdit_direct.setText(file_name)
    except FileNotFoundError:
        return


def make_gexyz():
    a = pd.read_table(ui.lineEdit_direct.text(), delimiter=";", header=0)
    dir = '/'.join(ui.lineEdit_direct.text().split('/')[:-1])
    list_int = [-1]
    list_name = []
    for i_file in os.listdir(dir):
        if i_file != ui.lineEdit_direct.text().split('/')[-1] and i_file.endswith('.txt'):
            list_name.append(dir + '/' + i_file)
            with open(dir + '/' + i_file) as f:
                n = 0
                while True:
                    line = f.readline()
                    if line.strip().endswith(';0;0;'):
                        list_int.append(list_int[-1] + n - 1)
                        break
                    n += 1
    ui.progressBar.setMaximum(len(list_int) - 1)
    for i in range(len(list_int) - 1):
        print(a[['X', 'Y', 'Z']].loc[list_int[i] + 1: list_int[i + 1]])
        a[['X', 'Y', 'Z']].loc[list_int[i] + 1: list_int[i + 1]].to_csv(str(list_name[i]) + '.gexyz', sep=' ', header=None, index=None)
        ui.progressBar.setValue(i + 1)






def log_uncaught_exceptions(ex_cls, ex, tb):
    """ Вывод ошибок программы """
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)
    sys.exit()


ui.pushButton_file.clicked.connect(choose_file)
ui.pushButton_gexyz.clicked.connect(make_gexyz)


sys.excepthook = log_uncaught_exceptions

sys.exit(app.exec_())