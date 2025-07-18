# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_funcionario_cadastro_profissional.ui'
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

class Ui_FuncionarioCadastroProfissional(object):
    def setupUi(self, FuncionarioCadastroProfissional):
        if not FuncionarioCadastroProfissional.objectName():
            FuncionarioCadastroProfissional.setObjectName(u"FuncionarioCadastroProfissional")
        FuncionarioCadastroProfissional.resize(659, 711)
        self.widget = QWidget(FuncionarioCadastroProfissional)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 641, 681))
        self.widget.setStyleSheet(u"QPushButton#voltar_button {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgba(85, 98, 112, 255);\n"
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
"	color: rgba(155, 168, 182, 220);\n"
"}\n"
"\n"
"QPushButton#voltar_button:pressed {\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"	color: rgba(115, 128, 142, 255);\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(10, 25, 50, 230),\n"
"        stop:1 rgba(180, 180, 180, 50)\n"
"    );\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#fun_cadastrar_button {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(15, "
                        "35, 70, 230),\n"
"        stop:1 rgba(200, 200, 200, 60)\n"
"    );\n"
"    color: rgba(255, 255, 255, 230);\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#fun_cadastrar_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 240),\n"
"        stop:1 rgba(220, 220, 220, 80)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#fun_cadastrar_button:pressed {\n"
"    padding-left: 3px;\n"
"    padding-top: 3px;\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(10, 25, 50, 230),\n"
"        stop:1 rgba(180, 180, 180, 50)\n"
"    );\n"
"}\n"
"")
        self.background_4 = QLabel(self.widget)
        self.background_4.setObjectName(u"background_4")
        self.background_4.setGeometry(QRect(20, 20, 601, 641))
        self.background_4.setStyleSheet(u"border-image: url(:/resources/log_background.png);\n"
"border-radius: 20px;\n"
"")
        self.fundotransparente = QLabel(self.widget)
        self.fundotransparente.setObjectName(u"fundotransparente")
        self.fundotransparente.setGeometry(QRect(30, 30, 581, 621))
        self.fundotransparente.setStyleSheet(u"background-color: rgba( 0 ,0, 0, 100 );\n"
"border-radius: 20px;")
        self.voltar_button = QPushButton(self.widget)
        self.voltar_button.setObjectName(u"voltar_button")
        self.voltar_button.setGeometry(QRect(55, 60, 51, 51))
        self.voltar_button.setStyleSheet(u"border-image: url(:/resources/ic_voltar.png);")
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(451, 72, 141, 41))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(310, 43, 291, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.fun_email = QLineEdit(self.widget)
        self.fun_email.setObjectName(u"fun_email")
        self.fun_email.setGeometry(QRect(132, 274, 371, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.fun_email.setFont(font2)
        self.fun_email.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    border: 2px solid rgba(105, 118, 132, 220);\n"
"    border-radius: 10px;\n"
"    color: rgba(255, 255, 255, 230);\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(130, 170, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"")
        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(138, 247, 201, 20))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(374, 150, 201, 20))
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.fun_cargo = QLineEdit(self.widget)
        self.fun_cargo.setObjectName(u"fun_cargo")
        self.fun_cargo.setGeometry(QRect(130, 178, 231, 51))
        self.fun_cargo.setFont(font2)
        self.fun_cargo.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    border: 2px solid rgba(105, 118, 132, 220);\n"
"    border-radius: 10px;\n"
"    color: rgba(255, 255, 255, 230);\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(130, 170, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"")
        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(138, 150, 201, 20))
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.fun_salario = QLineEdit(self.widget)
        self.fun_salario.setObjectName(u"fun_salario")
        self.fun_salario.setGeometry(QRect(370, 178, 131, 51))
        self.fun_salario.setFont(font2)
        self.fun_salario.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    border: 2px solid rgba(105, 118, 132, 220);\n"
"    border-radius: 10px;\n"
"    color: rgba(255, 255, 255, 230);\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(130, 170, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"")
        self.fun_cadastrar_button = QPushButton(self.widget)
        self.fun_cadastrar_button.setObjectName(u"fun_cadastrar_button")
        self.fun_cadastrar_button.setGeometry(QRect(133, 560, 371, 51))
        self.fun_cadastrar_button.setFont(font3)
        self.fun_senha = QLineEdit(self.widget)
        self.fun_senha.setObjectName(u"fun_senha")
        self.fun_senha.setGeometry(QRect(132, 367, 371, 51))
        self.fun_senha.setFont(font2)
        self.fun_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    border: 2px solid rgba(105, 118, 132, 220);\n"
"    border-radius: 10px;\n"
"    color: rgba(255, 255, 255, 230);\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(130, 170, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"")
        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(138, 340, 201, 20))
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.fun_confirmar_senha = QLineEdit(self.widget)
        self.fun_confirmar_senha.setObjectName(u"fun_confirmar_senha")
        self.fun_confirmar_senha.setGeometry(QRect(132, 457, 371, 51))
        self.fun_confirmar_senha.setFont(font2)
        self.fun_confirmar_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    border: 2px solid rgba(105, 118, 132, 220);\n"
"    border-radius: 10px;\n"
"    color: rgba(255, 255, 255, 230);\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(130, 170, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"")
        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(138, 430, 201, 20))
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"color: rgba(255, 255, 255, 214);")

        self.retranslateUi(FuncionarioCadastroProfissional)

        QMetaObject.connectSlotsByName(FuncionarioCadastroProfissional)
    # setupUi

    def retranslateUi(self, FuncionarioCadastroProfissional):
        FuncionarioCadastroProfissional.setWindowTitle(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Form", None))
        self.background_4.setText("")
        self.fundotransparente.setText("")
#if QT_CONFIG(tooltip)
        self.voltar_button.setToolTip(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Voltar", None))
#endif // QT_CONFIG(tooltip)
        self.voltar_button.setText("")
        self.label_22.setText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Dados profissionais", None))
        self.label_23.setText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Cadastro de Funcion\u00e1rio", None))
        self.fun_email.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Informe email do funcion\u00e1rio", None))
        self.label_24.setText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Email:", None))
        self.label_26.setText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Sal\u00e1rio", None))
        self.fun_cargo.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Cargo do funcion\u00e1rio", None))
        self.label_27.setText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Cargo:", None))
        self.fun_salario.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"R$ 0,00", None))
        self.fun_cadastrar_button.setText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Cadastrar", None))
        self.fun_senha.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Digite sua senha", None))
        self.label_28.setText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Senha:", None))
        self.fun_confirmar_senha.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Digite a senha novamente", None))
        self.label_29.setText(QCoreApplication.translate("FuncionarioCadastroProfissional", u"Confirmar senha:", None))
    # retranslateUi

