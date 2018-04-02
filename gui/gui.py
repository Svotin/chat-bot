#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont,QImage,QBrush,QPalette
from PyQt5.QtCore import QCoreApplication, QSize,Qt
import time


class mainFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        message = ""

    def initUI(self):
        ## MAIN WINDOW ##
        self.statusBar().showMessage('Готов')
        self.setFixedSize(600,300)
        self.center()
        self.setWindowTitle('Бот')
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowFlags(Qt.Dialog)

        self.show()

        ## BACKGROUND ##
##        fImage = QImage("background.jpg")
##        sImage = fImage.scaled(QSize(600,300))
##        pal = QPalette()
##        pal.setBrush(10, QBrush(sImage))
##        self.setPalette(pal)

        ## REPLY ##
        self.Reply1 = QLabel("",self)
##        self.Reply1.update()    ХЗ
        self.Reply1.setFont(QFont("Times", 16))
        self.Reply1.setGeometry(20,30,560,100)
        self.Reply1.setWordWrap(True)
        self.Reply1.show()

        ## FIELD FOR TEXT ##
        self.line1 = QLineEdit("Введите ваше сообщение",self)
        self.line1.move(150, 170)
        self.line1.setFixedWidth(320)
        f = self.line1.font()
        f.setPointSize(12) # размер шрифта
        self.line1.setFont(f)
        self.line1.selectAll()

        #QToolTip.setFont(QFont('SansSerif', 10))         шрифт подсказок

        #self.setToolTip('This is a <b>QWidget</b> widget')      подсказка

        ## BUTTON ##
        btn = QPushButton('Отправить', self)
        #btn.setToolTip('This is a <b>QPushButton</b> widget')    подсказка
        btn.resize(btn.sizeHint())
        btn.move(250, 220)
        btn.clicked.connect(lambda: self.getText(self.line1.text()))

        ## SHOW ELEMENTS ##
        self.show()
        self.line1.show()
        btn.show()
##        label1.show()


    def reply(self, text):
        self.Reply1.setText(text)





    def getText(self, text):
        message = text
        ##      проверка текста на корректность    15.04  ##
        self.reply(message)
        return message





    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Выход', "Вы действительно хотите выйти?",
                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainFrame()
    sys.exit(app.exec_())