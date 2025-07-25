# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_tabela_usuario_adm.ui'
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

class Ui_TabelaUsuarioAdm(object):
    def setupUi(self, TabelaUsuarioAdm):
        if not TabelaUsuarioAdm.objectName():
            TabelaUsuarioAdm.setObjectName(u"TabelaUsuarioAdm")
        TabelaUsuarioAdm.resize(742, 814)
        self.widget = QWidget(TabelaUsuarioAdm)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 721, 801))
        self.widget.setStyleSheet(u"QPushButton#buscar_button, QPushButton#logout_button, QPushButton#add_button, QPushButton#editar_button, QPushButton#deletar_button  {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"    border-radius: 20px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#buscar_button:hover,  QPushButton#logout_button:hover,\n"
"QPushButton#add_button:hover,\n"
"QPushButton#editar_button:hover,\n"
"QPushButton#deletar_button:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25, 55, 100, 240),\n"
"        stop:1 rgba(220, 220, 220, 80)\n"
"    );\n"
"	color:rgba(155, 168, 182, 220);\n"
"}\n"
"\n"
"QPushButton#buscar_button:pressed, QPushButton#logout_button:pressed,\n"
"QPushButton#add_button:pressed,\n"
"QPushButton#editar_button:pressed,\n"
"QPushButton#deletar_button:pressed {\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color:rgba(115, 128, 142, 2"
                        "55);\n"
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
"        spread:pad,\n"
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
"        stop:1 rgba(220,"
                        " 220, 220, 50)\n"
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
"        stop:1 rgba(180, 180, 180, 30)\n"
"    );\n"
"}\n"
"")
        self.background = QLabel(self.widget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(10, 10, 701, 771))
        self.background.setStyleSheet(u"border-image: url(:/resources/log_background.png);\n"
"border-radius: 20px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 680, 71))
        self.label_3.setStyleSheet(u"background-color: rgba( 0 ,0, 0, 100 );\n"
"border-radius: 20px;")
        self.produtos_button = QPushButton(self.widget)
        self.produtos_button.setObjectName(u"produtos_button")
        self.produtos_button.setGeometry(QRect(30, 30, 131, 41))
        self.cliente_button = QPushButton(self.widget)
        self.cliente_button.setObjectName(u"cliente_button")
        self.cliente_button.setGeometry(QRect(170, 30, 131, 41))
        self.funcionario_button = QPushButton(self.widget)
        self.funcionario_button.setObjectName(u"funcionario_button")
        self.funcionario_button.setGeometry(QRect(310, 30, 131, 41))
        self.logout_button = QPushButton(self.widget)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setGeometry(QRect(640, 20, 50, 50))
        self.logout_button.setMaximumSize(QSize(51, 51))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet(u"border-image: url(:/resources/ic_logout.png);")
        self.buscar_button = QPushButton(self.widget)
        self.buscar_button.setObjectName(u"buscar_button")
        self.buscar_button.setGeometry(QRect(630, 212, 51, 51))
        self.buscar_button.setMaximumSize(QSize(51, 51))
        self.buscar_button.setFont(font)
        self.buscar_button.setStyleSheet(u"border-image: url(:/resources/ic_busca.png);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(46, 165, 481, 31))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255, 214);")
        self.deletar_button = QPushButton(self.widget)
        self.deletar_button.setObjectName(u"deletar_button")
        self.deletar_button.setGeometry(QRect(646, 285, 35, 35))
        self.deletar_button.setMaximumSize(QSize(35, 35))
        self.deletar_button.setFont(font)
        self.deletar_button.setStyleSheet(u"border-image: url(:/resources/ic_deletar.png);")
        self.fundotransparente_3 = QLabel(self.widget)
        self.fundotransparente_3.setObjectName(u"fundotransparente_3")
        self.fundotransparente_3.setGeometry(QRect(30, 280, 661, 45))
        self.fundotransparente_3.setStyleSheet(u"background-color: rgba( 113 ,118, 145, 200 );\n"
"border-radius: 5px;")
        self.barra_pesquisa = QLineEdit(self.widget)
        self.barra_pesquisa.setObjectName(u"barra_pesquisa")
        self.barra_pesquisa.setGeometry(QRect(35, 212, 581, 51))
        font2 = QFont()
        font2.setPointSize(11)
        self.barra_pesquisa.setFont(font2)
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
        self.editar_button = QPushButton(self.widget)
        self.editar_button.setObjectName(u"editar_button")
        self.editar_button.setGeometry(QRect(600, 285, 35, 35))
        self.editar_button.setMaximumSize(QSize(35, 35))
        self.editar_button.setFont(font)
        self.editar_button.setStyleSheet(u"border-image: url(:/resources/ic_editar.png);")
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
        self.cliente_table.setGeometry(QRect(30, 330, 661, 431))
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
        self.add_button = QPushButton(self.widget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(38, 285, 35, 35))
        self.add_button.setMaximumSize(QSize(35, 35))
        self.add_button.setFont(font)
        self.add_button.setStyleSheet(u"border-image: url(:/resources/ic_add.png);")
        self.background.raise_()
        self.label_3.raise_()
        self.produtos_button.raise_()
        self.cliente_button.raise_()
        self.funcionario_button.raise_()
        self.logout_button.raise_()
        self.buscar_button.raise_()
        self.label_2.raise_()
        self.fundotransparente_3.raise_()
        self.barra_pesquisa.raise_()
        self.editar_button.raise_()
        self.cliente_table.raise_()
        self.add_button.raise_()
        self.deletar_button.raise_()

        self.retranslateUi(TabelaUsuarioAdm)

        QMetaObject.connectSlotsByName(TabelaUsuarioAdm)
    # setupUi

    def retranslateUi(self, TabelaUsuarioAdm):
        TabelaUsuarioAdm.setWindowTitle(QCoreApplication.translate("TabelaUsuarioAdm", u"Form", None))
        self.background.setText("")
        self.label_3.setText("")
        self.produtos_button.setText(QCoreApplication.translate("TabelaUsuarioAdm", u"Produto", None))
        self.cliente_button.setText(QCoreApplication.translate("TabelaUsuarioAdm", u"Ciente", None))
        self.funcionario_button.setText(QCoreApplication.translate("TabelaUsuarioAdm", u"Funcion\u00e1rio", None))
#if QT_CONFIG(tooltip)
        self.logout_button.setToolTip(QCoreApplication.translate("TabelaUsuarioAdm", u"Logout", None))
#endif // QT_CONFIG(tooltip)
        self.logout_button.setText("")
#if QT_CONFIG(tooltip)
        self.buscar_button.setToolTip(QCoreApplication.translate("TabelaUsuarioAdm", u"Pesquisar", None))
#endif // QT_CONFIG(tooltip)
        self.buscar_button.setText("")
        self.label_2.setText(QCoreApplication.translate("TabelaUsuarioAdm", u"Pesquisar cliente:", None))
#if QT_CONFIG(tooltip)
        self.deletar_button.setToolTip(QCoreApplication.translate("TabelaUsuarioAdm", u"Excluir", None))
#endif // QT_CONFIG(tooltip)
        self.deletar_button.setText("")
        self.fundotransparente_3.setText("")
        self.barra_pesquisa.setPlaceholderText(QCoreApplication.translate("TabelaUsuarioAdm", u"Informe caracter\u00edstica do cliente", None))
#if QT_CONFIG(tooltip)
        self.editar_button.setToolTip(QCoreApplication.translate("TabelaUsuarioAdm", u"Editar", None))
#endif // QT_CONFIG(tooltip)
        self.editar_button.setText("")
        ___qtablewidgetitem = self.cliente_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TabelaUsuarioAdm", u"ID", None));
        ___qtablewidgetitem1 = self.cliente_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TabelaUsuarioAdm", u"CPF", None));
        ___qtablewidgetitem2 = self.cliente_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TabelaUsuarioAdm", u"Nome", None));
        ___qtablewidgetitem3 = self.cliente_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TabelaUsuarioAdm", u"Email", None));
        ___qtablewidgetitem4 = self.cliente_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TabelaUsuarioAdm", u"Desconto", None));
#if QT_CONFIG(tooltip)
        self.add_button.setToolTip(QCoreApplication.translate("TabelaUsuarioAdm", u"Adicionar cliente", None))
#endif // QT_CONFIG(tooltip)
        self.add_button.setText("")
    # retranslateUi

