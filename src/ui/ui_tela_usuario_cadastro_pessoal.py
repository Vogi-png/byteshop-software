# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_usuario_cadastro_pessoal.ui'
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

class Ui_UsuarioCadastroPessoal(object):
    def setupUi(self, UsuarioCadastroPessoal):
        if not UsuarioCadastroPessoal.objectName():
            UsuarioCadastroPessoal.setObjectName(u"UsuarioCadastroPessoal")
        UsuarioCadastroPessoal.resize(659, 818)
        self.widget = QWidget(UsuarioCadastroPessoal)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 641, 791))
        self.widget.setStyleSheet(u"QPushButton#voltar_button{\n"
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
"QPushButton#usu_cadastrar_button {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(15, 3"
                        "5, 70, 230),\n"
"        stop:1 rgba(200, 200, 200, 60)\n"
"    );\n"
"    color: rgba(255, 255, 255, 230);\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#usu_cadastrar_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 240),\n"
"        stop:1 rgba(220, 220, 220, 80)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#usu_cadastrar_button:pressed {\n"
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
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 601, 731))
        self.label.setStyleSheet(u"border-image: url(:/resources/log_background.png);\n"
"border-radius: 20px;")
        self.fundotransparente = QLabel(self.widget)
        self.fundotransparente.setObjectName(u"fundotransparente")
        self.fundotransparente.setGeometry(QRect(30, 30, 581, 711))
        self.fundotransparente.setStyleSheet(u"background-color: rgba( 0 ,0, 0, 100 );\n"
"border-radius: 20px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 40, 241, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(481, 69, 111, 41))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.voltar_button = QPushButton(self.widget)
        self.voltar_button.setObjectName(u"voltar_button")
        self.voltar_button.setGeometry(QRect(55, 57, 51, 51))
        self.voltar_button.setStyleSheet(u"border-image: url(:/resources/ic_voltar.png);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(138, 150, 201, 20))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.usu_nome = QLineEdit(self.widget)
        self.usu_nome.setObjectName(u"usu_nome")
        self.usu_nome.setGeometry(QRect(130, 178, 371, 51))
        font3 = QFont()
        font3.setPointSize(12)
        self.usu_nome.setFont(font3)
        self.usu_nome.setStyleSheet(u"QLineEdit {\n"
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
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(138, 241, 201, 20))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.usu_cpf = QLineEdit(self.widget)
        self.usu_cpf.setObjectName(u"usu_cpf")
        self.usu_cpf.setGeometry(QRect(130, 267, 371, 51))
        self.usu_cpf.setFont(font3)
        self.usu_cpf.setStyleSheet(u"QLineEdit {\n"
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
        self.usu_email = QLineEdit(self.widget)
        self.usu_email.setObjectName(u"usu_email")
        self.usu_email.setGeometry(QRect(130, 357, 371, 51))
        self.usu_email.setFont(font3)
        self.usu_email.setStyleSheet(u"QLineEdit {\n"
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
        self.label_24.setGeometry(QRect(138, 330, 201, 20))
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.usu_senha = QLineEdit(self.widget)
        self.usu_senha.setObjectName(u"usu_senha")
        self.usu_senha.setGeometry(QRect(130, 445, 371, 51))
        self.usu_senha.setFont(font3)
        self.usu_senha.setStyleSheet(u"QLineEdit {\n"
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
        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(138, 418, 201, 20))
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.usu_senha_confirmar = QLineEdit(self.widget)
        self.usu_senha_confirmar.setObjectName(u"usu_senha_confirmar")
        self.usu_senha_confirmar.setGeometry(QRect(130, 534, 371, 51))
        self.usu_senha_confirmar.setFont(font3)
        self.usu_senha_confirmar.setStyleSheet(u"QLineEdit {\n"
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
        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(138, 507, 201, 20))
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.usu_cadastrar_button = QPushButton(self.widget)
        self.usu_cadastrar_button.setObjectName(u"usu_cadastrar_button")
        self.usu_cadastrar_button.setGeometry(QRect(129, 635, 371, 51))
        self.usu_cadastrar_button.setFont(font2)

        self.retranslateUi(UsuarioCadastroPessoal)

        QMetaObject.connectSlotsByName(UsuarioCadastroPessoal)
    # setupUi

    def retranslateUi(self, UsuarioCadastroPessoal):
        UsuarioCadastroPessoal.setWindowTitle(QCoreApplication.translate("UsuarioCadastroPessoal", u"Form", None))
        self.label.setText("")
        self.fundotransparente.setText("")
        self.label_2.setText(QCoreApplication.translate("UsuarioCadastroPessoal", u"Cadastro de Usu\u00e1rio", None))
        self.label_4.setText(QCoreApplication.translate("UsuarioCadastroPessoal", u"Dados pessoais", None))
#if QT_CONFIG(tooltip)
        self.voltar_button.setToolTip(QCoreApplication.translate("UsuarioCadastroPessoal", u"Voltar", None))
#endif // QT_CONFIG(tooltip)
        self.voltar_button.setText("")
        self.label_8.setText(QCoreApplication.translate("UsuarioCadastroPessoal", u"Nome:", None))
        self.usu_nome.setPlaceholderText(QCoreApplication.translate("UsuarioCadastroPessoal", u"Informe seu nome", None))
        self.label_7.setText(QCoreApplication.translate("UsuarioCadastroPessoal", u"CPF:", None))
        self.usu_cpf.setPlaceholderText(QCoreApplication.translate("UsuarioCadastroPessoal", u"Insira seu CPF", None))
        self.usu_email.setPlaceholderText(QCoreApplication.translate("UsuarioCadastroPessoal", u"Informe email de contato", None))
        self.label_24.setText(QCoreApplication.translate("UsuarioCadastroPessoal", u"Email:", None))
        self.usu_senha.setPlaceholderText(QCoreApplication.translate("UsuarioCadastroPessoal", u"********", None))
        self.label_25.setText(QCoreApplication.translate("UsuarioCadastroPessoal", u"Senha:", None))
        self.usu_senha_confirmar.setText("")
        self.usu_senha_confirmar.setPlaceholderText(QCoreApplication.translate("UsuarioCadastroPessoal", u"********", None))
        self.label_26.setText(QCoreApplication.translate("UsuarioCadastroPessoal", u"Confirmar senha:", None))
        self.usu_cadastrar_button.setText(QCoreApplication.translate("UsuarioCadastroPessoal", u"Cadastrar", None))
    # retranslateUi

