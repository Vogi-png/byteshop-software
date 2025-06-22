# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_cadastro_produto.ui'
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

class Ui_CadastroProduto(object):
    def setupUi(self, CadastroProduto):
        if not CadastroProduto.objectName():
            CadastroProduto.setObjectName(u"CadastroProduto")
        CadastroProduto.resize(521, 622)
        self.widget = QWidget(CadastroProduto)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 501, 601))
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
"}\n"
"\n"
"QPushButton#prod_cadastrar_button {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(15, 35, 70, 230),\n"
""
                        "        stop:1 rgba(200, 200, 200, 60)\n"
"    );\n"
"    color: rgba(255, 255, 255, 230);\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#prod_cadastrar_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 240),\n"
"        stop:1 rgba(220, 220, 220, 80)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#prod_cadastrar_button:pressed {\n"
"    padding-left: 3px;\n"
"    padding-top: 3px;\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(10, 25, 50, 230),\n"
"        stop:1 rgba(180, 180, 180, 50)\n"
"    );\n"
"}")
        self.background = QLabel(self.widget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(11, 11, 471, 571))
        self.background.setStyleSheet(u"border-image: url(:/resources/log_background.png);\n"
"border-radius: 20px;")
        self.fundo_transparente = QLabel(self.widget)
        self.fundo_transparente.setObjectName(u"fundo_transparente")
        self.fundo_transparente.setGeometry(QRect(20, 20, 451, 551))
        font = QFont()
        font.setPointSize(12)
        self.fundo_transparente.setFont(font)
        self.fundo_transparente.setStyleSheet(u"background-color: rgba( 0 ,0, 0, 100 );\n"
"border-radius: 20px;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(115, 48, 311, 41))
        font1 = QFont()
        font1.setPointSize(23)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.nome_produto = QLineEdit(self.widget)
        self.nome_produto.setObjectName(u"nome_produto")
        self.nome_produto.setGeometry(QRect(60, 186, 371, 51))
        self.nome_produto.setFont(font)
        self.nome_produto.setStyleSheet(u"QLineEdit {\n"
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
        self.preco_produto = QLineEdit(self.widget)
        self.preco_produto.setObjectName(u"preco_produto")
        self.preco_produto.setGeometry(QRect(60, 286, 171, 51))
        self.preco_produto.setStyleSheet(u"QLineEdit {\n"
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
        self.quantidade_produto = QLineEdit(self.widget)
        self.quantidade_produto.setObjectName(u"quantidade_produto")
        self.quantidade_produto.setGeometry(QRect(260, 286, 171, 51))
        self.quantidade_produto.setStyleSheet(u"QLineEdit {\n"
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
        self.marca_produto = QLineEdit(self.widget)
        self.marca_produto.setObjectName(u"marca_produto")
        self.marca_produto.setGeometry(QRect(60, 385, 371, 51))
        self.marca_produto.setStyleSheet(u"QLineEdit {\n"
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
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(65, 159, 201, 20))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(66, 255, 63, 31))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(266, 255, 121, 31))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(66, 355, 63, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.prod_cadastrar_button = QPushButton(self.widget)
        self.prod_cadastrar_button.setObjectName(u"prod_cadastrar_button")
        self.prod_cadastrar_button.setGeometry(QRect(88, 470, 311, 51))
        self.prod_cadastrar_button.setStyleSheet(u"QPushButton#prod_cadastrar_button {\n"
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
"QPushButton#prod_cadastrar_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 240),\n"
"        stop:1 rgba(220, 220, 220, 80)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#prod_cadastrar_button:pressed {\n"
"    padding-left: 3px;\n"
"    padding-top: 3px;\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(10, 25, 50, 230),\n"
"        stop:1 rgba(180, 180, 180, 50)\n"
"    );\n"
"}")
        self.voltar_button = QPushButton(self.widget)
        self.voltar_button.setObjectName(u"voltar_button")
        self.voltar_button.setGeometry(QRect(40, 45, 51, 51))
        self.voltar_button.setStyleSheet(u"border-image: url(:/resources/ic_voltar.png);")

        self.retranslateUi(CadastroProduto)

        QMetaObject.connectSlotsByName(CadastroProduto)
    # setupUi

    def retranslateUi(self, CadastroProduto):
        CadastroProduto.setWindowTitle(QCoreApplication.translate("CadastroProduto", u"Form", None))
        self.background.setText("")
        self.fundo_transparente.setText("")
        self.label.setText(QCoreApplication.translate("CadastroProduto", u"Cadastro de Produto", None))
        self.nome_produto.setPlaceholderText(QCoreApplication.translate("CadastroProduto", u"Informe nome do produto", None))
        self.preco_produto.setText("")
        self.preco_produto.setPlaceholderText(QCoreApplication.translate("CadastroProduto", u"Valor do produto", None))
        self.quantidade_produto.setPlaceholderText(QCoreApplication.translate("CadastroProduto", u"Quantidade ", None))
        self.marca_produto.setPlaceholderText(QCoreApplication.translate("CadastroProduto", u"Informe a marca do produto", None))
        self.label_2.setText(QCoreApplication.translate("CadastroProduto", u"T\u00edtulo do Produto:", None))
        self.label_3.setText(QCoreApplication.translate("CadastroProduto", u"Pre\u00e7o:", None))
        self.label_4.setText(QCoreApplication.translate("CadastroProduto", u"Estoque:", None))
        self.label_5.setText(QCoreApplication.translate("CadastroProduto", u"Marca:", None))
        self.prod_cadastrar_button.setText(QCoreApplication.translate("CadastroProduto", u"Cadastrar", None))
#if QT_CONFIG(tooltip)
        self.voltar_button.setToolTip(QCoreApplication.translate("CadastroProduto", u"Voltar", None))
#endif // QT_CONFIG(tooltip)
        self.voltar_button.setText("")
    # retranslateUi

