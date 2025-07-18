# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_funcionario_cadastro_pessoal.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_FuncionarioCadastroPessoal(object):
    def setupUi(self, FuncionarioCadastroPessoal):
        if not FuncionarioCadastroPessoal.objectName():
            FuncionarioCadastroPessoal.setObjectName(u"FuncionarioCadastroPessoal")
        FuncionarioCadastroPessoal.resize(659, 818)
        self.widget = QWidget(FuncionarioCadastroPessoal)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 641, 791))
        self.widget.setStyleSheet(u"QPushButton#voltar_button, QPushButton#cep_button {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgba(85, 98, 112, 255);\n"
"    border-radius: 20px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#voltar_button:hover, QPushButton#cep_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 240),\n"
"        stop:1 rgba(220, 220, 220, 80)\n"
"    );\n"
"	color: rgba(155, 168, 182, 220);\n"
"}\n"
"\n"
"QPushButton#voltar_button:pressed, QPushButton#cep_button:pressed {\n"
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
"QPushButton#seguir_button {\n"
"    background-color: qlineargradient(\n"
"     "
                        "   spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(15, 35, 70, 230),\n"
"        stop:1 rgba(200, 200, 200, 60)\n"
"    );\n"
"    color: rgba(255, 255, 255, 230);\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#seguir_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 240),\n"
"        stop:1 rgba(220, 220, 220, 80)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#seguir_button:pressed {\n"
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
        self.background = QLabel(self.widget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(20, 20, 601, 751))
        self.background.setStyleSheet(u"border-image: url(:/resources/log_background.png);\n"
"border-radius: 20px;")
        self.fundotransparente = QLabel(self.widget)
        self.fundotransparente.setObjectName(u"fundotransparente")
        self.fundotransparente.setGeometry(QRect(30, 30, 581, 731))
        self.fundotransparente.setStyleSheet(u"background-color: rgba( 0 ,0, 0, 100 );\n"
"border-radius: 20px;")
        self.voltar_button = QPushButton(self.widget)
        self.voltar_button.setObjectName(u"voltar_button")
        self.voltar_button.setGeometry(QRect(55, 57, 51, 51))
        self.voltar_button.setStyleSheet(u"border-image: url(:/resources/ic_voltar.png);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 40, 291, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.fun_nome = QLineEdit(self.widget)
        self.fun_nome.setObjectName(u"fun_nome")
        self.fun_nome.setGeometry(QRect(130, 178, 371, 51))
        font1 = QFont()
        font1.setPointSize(12)
        self.fun_nome.setFont(font1)
        self.fun_nome.setStyleSheet(u"QLineEdit {\n"
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
        self.fun_rua = QLineEdit(self.widget)
        self.fun_rua.setObjectName(u"fun_rua")
        self.fun_rua.setGeometry(QRect(130, 431, 371, 51))
        self.fun_rua.setFont(font1)
        self.fun_rua.setStyleSheet(u"QLineEdit {\n"
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
        self.fun_cpf = QLineEdit(self.widget)
        self.fun_cpf.setObjectName(u"fun_cpf")
        self.fun_cpf.setGeometry(QRect(130, 270, 231, 51))
        self.fun_cpf.setFont(font1)
        self.fun_cpf.setStyleSheet(u"QLineEdit {\n"
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
        self.fun_aniversario = QLineEdit(self.widget)
        self.fun_aniversario.setObjectName(u"fun_aniversario")
        self.fun_aniversario.setGeometry(QRect(370, 270, 131, 51))
        self.fun_aniversario.setFont(font1)
        self.fun_aniversario.setStyleSheet(u"QLineEdit {\n"
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
        self.fun_numero = QLineEdit(self.widget)
        self.fun_numero.setObjectName(u"fun_numero")
        self.fun_numero.setGeometry(QRect(130, 494, 121, 51))
        self.fun_numero.setFont(font1)
        self.fun_numero.setStyleSheet(u"QLineEdit {\n"
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
        self.fun_cep = QLineEdit(self.widget)
        self.fun_cep.setObjectName(u"fun_cep")
        self.fun_cep.setGeometry(QRect(130, 368, 311, 51))
        self.fun_cep.setFont(font1)
        self.fun_cep.setStyleSheet(u"QLineEdit {\n"
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
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(138, 341, 201, 20))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(377, 243, 201, 20))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(138, 244, 201, 20))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(138, 150, 201, 20))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(481, 69, 111, 41))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.seguir_button = QPushButton(self.widget)
        self.seguir_button.setObjectName(u"seguir_button")
        self.seguir_button.setGeometry(QRect(450, 702, 131, 31))
        self.seguir_button.setFont(font2)
        self.fun_complemento = QLineEdit(self.widget)
        self.fun_complemento.setObjectName(u"fun_complemento")
        self.fun_complemento.setGeometry(QRect(260, 493, 241, 51))
        self.fun_complemento.setFont(font1)
        self.fun_complemento.setStyleSheet(u"QLineEdit {\n"
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
        self.cep_button = QPushButton(self.widget)
        self.cep_button.setObjectName(u"cep_button")
        self.cep_button.setGeometry(QRect(447, 367, 51, 51))
        self.cep_button.setMaximumSize(QSize(51, 51))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.cep_button.setFont(font4)
        self.cep_button.setStyleSheet(u"border-image: url(:/resources/ic_local.png);")
        self.fun_bairro = QLineEdit(self.widget)
        self.fun_bairro.setObjectName(u"fun_bairro")
        self.fun_bairro.setGeometry(QRect(130, 557, 371, 51))
        self.fun_bairro.setFont(font1)
        self.fun_bairro.setStyleSheet(u"QLineEdit {\n"
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
        self.fun_estado = QComboBox(self.widget)
        self.fun_estado.setObjectName(u"fun_estado")
        self.fun_estado.setGeometry(QRect(130, 620, 121, 51))
        self.fun_cidade = QComboBox(self.widget)
        self.fun_cidade.setObjectName(u"fun_cidade")
        self.fun_cidade.setGeometry(QRect(260, 620, 241, 51))

        self.retranslateUi(FuncionarioCadastroPessoal)

        QMetaObject.connectSlotsByName(FuncionarioCadastroPessoal)
    # setupUi

    def retranslateUi(self, FuncionarioCadastroPessoal):
        FuncionarioCadastroPessoal.setWindowTitle(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Form", None))
        self.background.setText("")
        self.fundotransparente.setText("")
#if QT_CONFIG(tooltip)
        self.voltar_button.setToolTip(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Voltar", None))
#endif // QT_CONFIG(tooltip)
        self.voltar_button.setText("")
        self.label_2.setText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Cadastro de Funcion\u00e1rio", None))
        self.fun_nome.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Informe nome do funcion\u00e1rio", None))
        self.fun_rua.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Rua / Avenida", None))
        self.fun_cpf.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Insira o CPF do funcion\u00e1rio", None))
        self.fun_aniversario.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"DD/MM/AAAA", None))
        self.fun_numero.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"N\u00famero", None))
        self.fun_cep.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"CEP", None))
        self.label_3.setText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Endere\u00e7o:", None))
        self.label_6.setText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Anivers\u00e1rio:", None))
        self.label_7.setText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"CPF:", None))
        self.label_8.setText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Nome (completo):", None))
        self.label_4.setText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Dados pessoais", None))
        self.seguir_button.setText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Seguir  >", None))
        self.fun_complemento.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Complemento", None))
#if QT_CONFIG(tooltip)
        self.cep_button.setToolTip(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Procurar CEP", None))
#endif // QT_CONFIG(tooltip)
        self.cep_button.setText("")
        self.fun_bairro.setPlaceholderText(QCoreApplication.translate("FuncionarioCadastroPessoal", u"Bairro", None))
    # retranslateUi

