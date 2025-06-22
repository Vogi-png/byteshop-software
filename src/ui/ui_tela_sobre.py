# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_sobre.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class Ui_Sobre(object):
    def setupUi(self, Sobre):
        if not Sobre.objectName():
            Sobre.setObjectName(u"Sobre")
        Sobre.resize(476, 586)
        self.widget = QWidget(Sobre)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 451, 561))
        self.widget.setStyleSheet(u"QPushButton#voltar_button {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"    border-radius: 20px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#voltar_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 240),\n"
"        stop:1 rgba(220, 220, 220, 80)\n"
"    );\n"
"	color:rgba(155, 168, 182, 220);\n"
"}\n"
"\n"
"QPushButton#voltar_button:pressed {\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color:rgba(115, 128, 142, 255);\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(10, 25, 50, 230),\n"
"        stop:1 rgba(180, 180, 180, 50)\n"
"    );\n"
"}")
        self.background = QLabel(self.widget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(20, 30, 411, 511))
        self.background.setStyleSheet(u"border-image: url(:/resources/log_background.png);\n"
"border-radius: 15px;")
        self.fundo_transparente = QLabel(self.widget)
        self.fundo_transparente.setObjectName(u"fundo_transparente")
        self.fundo_transparente.setGeometry(QRect(30, 40, 391, 491))
        self.fundo_transparente.setStyleSheet(u"background-color: rgba( 0 ,0, 0, 100 );\n"
"border-radius: 15px;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(99, 148, 171, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(99, 358, 151, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(298, 50, 101, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(99, 179, 241, 171))
        self.label_4.setStyleSheet(u"color: rgba( 255, 255, 255, 230 );")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(99, 405, 301, 20))
        self.label_5.setStyleSheet(u"color: rgba( 255, 255, 255, 230 );")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 490, 71, 20))
        self.label_6.setStyleSheet(u"color: rgba( 255, 255, 255, 230 );")
        self.voltar_button = QPushButton(self.widget)
        self.voltar_button.setObjectName(u"voltar_button")
        self.voltar_button.setGeometry(QRect(56, 60, 51, 51))
        self.voltar_button.setStyleSheet(u"border-image: url(:/resources/ic_voltar.png);")
        self.background.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.fundo_transparente.raise_()
        self.voltar_button.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.label_2.raise_()
        self.label.raise_()

        self.retranslateUi(Sobre)

        QMetaObject.connectSlotsByName(Sobre)
    # setupUi

    def retranslateUi(self, Sobre):
        Sobre.setWindowTitle(QCoreApplication.translate("Sobre", u"Form", None))
        self.background.setText("")
        self.fundo_transparente.setText("")
        self.label.setText(QCoreApplication.translate("Sobre", u"Desenvolvedores:", None))
        self.label_2.setText(QCoreApplication.translate("Sobre", u"Auxiliado por:", None))
        self.label_3.setText(QCoreApplication.translate("Sobre", u"Cr\u00e9ditos", None))
        self.label_4.setText(QCoreApplication.translate("Sobre", u"Giovanna Leal de Araujo\n"
"Guilherme Barreiros Pimentel\n"
"Jo\u00e3o Pedro de Macedo Figueiredo\n"
"Jo\u00e3o Vitor Gomes Santos\n"
"Lorenzo Braiener da Cunha\n"
"Maria Luiza Fran\u00e7a Mendes\n"
"Raphael B\u00edssimos Costa Dos Santos", None))
        self.label_5.setText(QCoreApplication.translate("Sobre", u"Nelson Carlos Medeiros de Vasconcellos\n"
"\n"
"", None))
        self.label_6.setText(QCoreApplication.translate("Sobre", u"Vers\u00e3o 0.0", None))
        self.voltar_button.setText("")
    # retranslateUi

