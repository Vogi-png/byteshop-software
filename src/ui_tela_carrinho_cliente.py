# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_carrinho_cliente.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import res_rc

class Ui_CarrinhoCliente(object):
    def setupUi(self, CarrinhoCliente):
        if not CarrinhoCliente.objectName():
            CarrinhoCliente.setObjectName(u"CarrinhoCliente")
        CarrinhoCliente.resize(742, 829)
        self.widget = QWidget(CarrinhoCliente)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 721, 801))
        self.widget.setStyleSheet(u"QPushButton#buscar_button,\n"
"QPushButton#voltar_button {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"    border-radius: 20px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#buscar_button:hover,  \n"
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
"QPushButton#buscar_button:pressed, QPushButton#voltar_button:pressed {\n"
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
"QPushButton#seguir_button {\n"
"    background-color: qlineargradient(\n"
" "
                        "       spread:pad,\n"
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
"\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 701, 771))
        self.label.setStyleSheet(u"border-image: url(:/resources/log_background.png);\n"
"border-radius: 20px;")
        self.buscar_button = QPushButton(self.widget)
        self.buscar_button.setObjectName(u"buscar_button")
        self.buscar_button.setGeometry(QRect(630, 250, 51, 51))
        self.buscar_button.setMaximumSize(QSize(51, 51))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.buscar_button.setFont(font)
        self.buscar_button.setStyleSheet(u"border-image: url(:/resources/ic_busca.png);")
        self.barra_pesquisa = QLineEdit(self.widget)
        self.barra_pesquisa.setObjectName(u"barra_pesquisa")
        self.barra_pesquisa.setGeometry(QRect(35, 250, 581, 51))
        font1 = QFont()
        font1.setPointSize(11)
        self.barra_pesquisa.setFont(font1)
        self.barra_pesquisa.setStyleSheet(u"\n"
"QLineEdit {\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    border: 2px solid rgba(105, 118, 132, 220);\n"
"    border-radius: 20px;\n"
"    color: rgba(255, 255, 255, 230);\n"
"    padding: 7px 13px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgba(130, 170, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(46, 203, 481, 31))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.seguir_button = QPushButton(self.widget)
        self.seguir_button.setObjectName(u"seguir_button")
        self.seguir_button.setGeometry(QRect(550, 724, 131, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.seguir_button.setFont(font3)
        self.cliente_table = QTableWidget(self.widget)
        if (self.cliente_table.columnCount() < 5):
            self.cliente_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.cliente_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cliente_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cliente_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cliente_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.cliente_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.cliente_table.setObjectName(u"cliente_table")
        self.cliente_table.setGeometry(QRect(30, 320, 661, 381))
        self.cliente_table.setStyleSheet(u"\n"
"\n"
"QTableWidget {\n"
"    background-color: rgba( 133 ,139, 174, 51 );\n"
"	border-radius: 20px;\n"
"    color: rgba(255, 255, 255, 230);\n"
"    gridline-color: rgba(255, 255, 255, 80);\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(40, 60, 110, 200);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    padding: 3px;\n"
"    border: 1px solid rgba( 133 ,139, 174, 51 );\n"
"}\n"
"\n"
"")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(48, 148, 601, 61))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(False)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgba(157, 169, 223, 100);")
        self.voltar_button = QPushButton(self.widget)
        self.voltar_button.setObjectName(u"voltar_button")
        self.voltar_button.setGeometry(QRect(55, 60, 51, 51))
        self.voltar_button.setStyleSheet(u"border-image: url(:/resources/ic_voltar.png);")

        self.retranslateUi(CarrinhoCliente)

        QMetaObject.connectSlotsByName(CarrinhoCliente)
    # setupUi

    def retranslateUi(self, CarrinhoCliente):
        CarrinhoCliente.setWindowTitle(QCoreApplication.translate("CarrinhoCliente", u"Form", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.buscar_button.setToolTip(QCoreApplication.translate("CarrinhoCliente", u"Pesquisar", None))
#endif // QT_CONFIG(tooltip)
        self.buscar_button.setText("")
        self.barra_pesquisa.setPlaceholderText(QCoreApplication.translate("CarrinhoCliente", u"Informe caracter\u00edstica do funcion\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("CarrinhoCliente", u"Pesquisar cliente:", None))
        self.seguir_button.setText(QCoreApplication.translate("CarrinhoCliente", u"Seguir  >", None))
        ___qtablewidgetitem = self.cliente_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CarrinhoCliente", u"ID", None));
        ___qtablewidgetitem1 = self.cliente_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CarrinhoCliente", u"CPF", None));
        ___qtablewidgetitem2 = self.cliente_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CarrinhoCliente", u"Nome", None));
        ___qtablewidgetitem3 = self.cliente_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CarrinhoCliente", u"Email", None));
        ___qtablewidgetitem4 = self.cliente_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CarrinhoCliente", u"Desconto", None));
        self.label_4.setText(QCoreApplication.translate("CarrinhoCliente", u"Selecione o cliente para o qual voc\u00ea deseja cadastrar a compra.", None))
#if QT_CONFIG(tooltip)
        self.voltar_button.setToolTip(QCoreApplication.translate("CarrinhoCliente", u"Voltar", None))
#endif // QT_CONFIG(tooltip)
        self.voltar_button.setText("")
    # retranslateUi

