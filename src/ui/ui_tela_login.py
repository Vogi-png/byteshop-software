# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import res_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(450, 550)
        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 370, 480))
        self.widget.setStyleSheet(u"QPushButton#login_button {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(15, 35, 70, 230),\n"
"        stop:1 rgba(200, 200, 200, 60)\n"
"    );\n"
"    color: rgba(255, 255, 255, 230);\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#login_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 240),\n"
"        stop:1 rgba(220, 220, 220, 80)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#login_button:pressed {\n"
"    padding-left: 3px;\n"
"    padding-top: 3px;\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(10, 25, 50, 230),\n"
"        stop:1 rgba(180, 180, 180, 50)\n"
"    );\n"
"}\n"
"\n"
"\n"
"")
        self.background = QLabel(self.widget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(30, 30, 300, 420))
        self.background.setStyleSheet(u"border-image: url(:/resources/log_background.png);\n"
"border-radius: 20px;\n"
"")
        self.logo = QLabel(self.widget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(80, 0, 211, 251))
        self.logo.setStyleSheet(u"border-image: url(:/resources/ByteShopLogo.png);")
        self.fundo_transparente = QLabel(self.widget)
        self.fundo_transparente.setObjectName(u"fundo_transparente")
        self.fundo_transparente.setGeometry(QRect(40, 39, 280, 401))
        self.fundo_transparente.setStyleSheet(u"background-color: rgba( 0 ,0, 0, 100 );\n"
"border-radius: 20px;")
        self.email_usuario = QLineEdit(self.widget)
        self.email_usuario.setObjectName(u"email_usuario")
        self.email_usuario.setGeometry(QRect(80, 194, 200, 40))
        font = QFont()
        font.setPointSize(10)
        self.email_usuario.setFont(font)
        self.email_usuario.setStyleSheet(u"background-color: rgba( 0, 0, 0, 0 );\n"
"border: none;\n"
"border-bottom: 2px solid rgba( 105, 118, 132, 255 ); \n"
"color: rgba( 255, 255, 255, 230 );\n"
"padding-botton: 7px;")
        self.senha_usuario = QLineEdit(self.widget)
        self.senha_usuario.setObjectName(u"senha_usuario")
        self.senha_usuario.setGeometry(QRect(80, 254, 200, 40))
        self.senha_usuario.setFont(font)
        self.senha_usuario.setStyleSheet(u"background-color: rgba( 0, 0, 0, 0 );\n"
"border: none;\n"
"border-bottom: 2px solid rgba( 105, 118, 132, 255 ); \n"
"color: rgba( 255, 255, 255, 230 );\n"
"padding-botton: 7px;")
        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(79, 349, 200, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.login_button.setFont(font1)
        self.redefinir_button = QPushButton(self.widget)
        self.redefinir_button.setObjectName(u"redefinir_button")
        self.redefinir_button.setGeometry(QRect(77, 300, 131, 28))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.redefinir_button.setFont(font2)
        self.redefinir_button.setStyleSheet(u"QPushButton#redefinir_button {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: rgba( 255, 255, 255, 230 );\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"QPushButton#redefinir_button:hover {\n"
"    color: rgb(100, 200, 255);\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton#redefinir_button:pressed {\n"
"	background-color: transparent;\n"
"    color: rgb(150, 150, 255);\n"
"}")
        self.redefinir_button.setFlat(True)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.background.setText("")
        self.logo.setText("")
        self.fundo_transparente.setText("")
        self.email_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"Email do usu\u00e1rio", None))
        self.senha_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.login_button.setText(QCoreApplication.translate("Login", u"Login", None))
        self.redefinir_button.setText(QCoreApplication.translate("Login", u"Esqueceu sua senha?", None))
    # retranslateUi

