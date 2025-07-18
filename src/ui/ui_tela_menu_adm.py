# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_menu_adm.ui'
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

class Ui_MenuADM(object):
    def setupUi(self, MenuADM):
        if not MenuADM.objectName():
            MenuADM.setObjectName(u"MenuADM")
        MenuADM.resize(768, 515)
        self.widget = QWidget(MenuADM)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 731, 491))
        self.widget.setStyleSheet(u"QPushButton#logout_button {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"    border-radius: 20px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#logout_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 240),\n"
"        stop:1 rgba(220, 220, 220, 80)\n"
"    );\n"
"	color:rgba(155, 168, 182, 220);\n"
"}\n"
"\n"
"QPushButton#logout_button:pressed {\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color:rgba(115, 128, 142, 255);\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(10, 25, 50, 230),\n"
"        stop:1 rgba(180, 180, 180, 50)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#cliente_button, QPushButton#relatorio_button, QPushButton#produtos_button, QPushButton#funcionario_button {\n"
"    background-color: qlineargradient(\n"
"        spread"
                        ":pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(15, 35, 70, 120), \n"
"        stop:1 rgba(200, 200, 200, 40)\n"
"    );\n"
"    color: rgba(255, 255, 255, 180);  \n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#cliente_button:hover, QPushButton#relatorio_button:hover, QPushButton#produtos_button:hover,\n"
"QPushButton#funcionario_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 150),\n"
"        stop:1 rgba(220, 220, 220, 50)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#cliente_button:pressed, QPushButton#relatorio_button:pressed, QPushButton#produtos_button:pressed,\n"
"QPushButton#funcionario_button:pressed {\n"
"    padding-left: 3px;\n"
"    padding-top: 3px;\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(10, 25, 50, 150),\n"
" "
                        "       stop:1 rgba(180, 180, 180, 30)\n"
"    );\n"
"}\n"
"")
        self.background = QLabel(self.widget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(10, 20, 711, 451))
        self.background.setStyleSheet(u"border-image: url(:/resources/log_background.png);\n"
"border-radius: 20px;")
        self.fundo_transparente = QLabel(self.widget)
        self.fundo_transparente.setObjectName(u"fundo_transparente")
        self.fundo_transparente.setGeometry(QRect(20, 30, 691, 431))
        self.fundo_transparente.setStyleSheet(u"background-color: rgba( 0 ,0, 0, 100 );\n"
"border-radius: 20px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-40, 100, 450, 380))
        self.label_2.setStyleSheet(u"border-image: url(:/resources/logo.png);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 691, 71))
        self.label_3.setStyleSheet(u"background-color: rgba( 0 ,0, 0, 100 );\n"
"border-radius: 20px;")
        self.logout_button = QPushButton(self.widget)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setGeometry(QRect(650, 40, 50, 50))
        self.logout_button.setMaximumSize(QSize(51, 51))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet(u"border-image: url(:/resources/ic_logout.png);")
        self.cliente_button = QPushButton(self.widget)
        self.cliente_button.setObjectName(u"cliente_button")
        self.cliente_button.setGeometry(QRect(174, 45, 131, 41))
        self.funcionario_button = QPushButton(self.widget)
        self.funcionario_button.setObjectName(u"funcionario_button")
        self.funcionario_button.setGeometry(QRect(312, 45, 131, 41))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(54, 390, 111, 20))
        font1 = QFont()
        font1.setPointSize(8)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgba(255, 255, 255, 180);  ")
        self.produtos_button = QPushButton(self.widget)
        self.produtos_button.setObjectName(u"produtos_button")
        self.produtos_button.setGeometry(QRect(36, 45, 131, 41))

        self.retranslateUi(MenuADM)

        QMetaObject.connectSlotsByName(MenuADM)
    # setupUi

    def retranslateUi(self, MenuADM):
        MenuADM.setWindowTitle(QCoreApplication.translate("MenuADM", u"Form", None))
        self.background.setText("")
        self.fundo_transparente.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
#if QT_CONFIG(tooltip)
        self.logout_button.setToolTip(QCoreApplication.translate("MenuADM", u"Logout", None))
#endif // QT_CONFIG(tooltip)
        self.logout_button.setText("")
        self.cliente_button.setText(QCoreApplication.translate("MenuADM", u"Cliente", None))
        self.funcionario_button.setText(QCoreApplication.translate("MenuADM", u"Funcion\u00e1rio", None))
        self.label.setText(QCoreApplication.translate("MenuADM", u"Modo Administrador", None))
        self.produtos_button.setText(QCoreApplication.translate("MenuADM", u"Produto", None))
    # retranslateUi

