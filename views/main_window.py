# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Maquinaexpendedora_form(object):
    def setupUi(self, Maquinaexpendedora_form):
        if not Maquinaexpendedora_form.objectName():
            Maquinaexpendedora_form.setObjectName(u"Maquinaexpendedora_form")
        Maquinaexpendedora_form.resize(760, 523)
        self.Maquinaexpendedora = QFrame(Maquinaexpendedora_form)
        self.Maquinaexpendedora.setObjectName(u"Maquinaexpendedora")
        self.Maquinaexpendedora.setGeometry(QRect(0, 420, 761, 101))
        self.Maquinaexpendedora.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.Maquinaexpendedora.setFrameShape(QFrame.StyledPanel)
        self.Maquinaexpendedora.setFrameShadow(QFrame.Raised)
        self.productoEntregado_label = QLabel(self.Maquinaexpendedora)
        self.productoEntregado_label.setObjectName(u"productoEntregado_label")
        self.productoEntregado_label.setGeometry(QRect(80, 0, 191, 51))
        font = QFont()
        font.setPointSize(12)
        self.productoEntregado_label.setFont(font)
        self.productoEntregado_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.productoEntregado_label.setAlignment(Qt.AlignCenter)
        self.cambio_label = QLabel(self.Maquinaexpendedora)
        self.cambio_label.setObjectName(u"cambio_label")
        self.cambio_label.setGeometry(QRect(570, 0, 191, 51))
        self.cambio_label.setFont(font)
        self.cambio_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cambio_label.setAlignment(Qt.AlignCenter)
        self.productoEntregadoNombre_label = QLabel(self.Maquinaexpendedora)
        self.productoEntregadoNombre_label.setObjectName(u"productoEntregadoNombre_label")
        self.productoEntregadoNombre_label.setGeometry(QRect(80, 40, 191, 51))
        self.productoEntregadoNombre_label.setFont(font)
        self.productoEntregadoNombre_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.productoEntregadoNombre_label.setAlignment(Qt.AlignCenter)
        self.cambioCantidad_label = QLabel(self.Maquinaexpendedora)
        self.cambioCantidad_label.setObjectName(u"cambioCantidad_label")
        self.cambioCantidad_label.setGeometry(QRect(620, 40, 131, 51))
        self.cambioCantidad_label.setFont(font)
        self.cambioCantidad_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cambioCantidad_label.setAlignment(Qt.AlignCenter)
        self.simboloCambio_label = QLabel(self.Maquinaexpendedora)
        self.simboloCambio_label.setObjectName(u"simboloCambio_label")
        self.simboloCambio_label.setGeometry(QRect(580, 40, 41, 51))
        self.simboloCambio_label.setFont(font)
        self.simboloCambio_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.simboloCambio_label.setAlignment(Qt.AlignCenter)
        self.Monedas_Frame = QFrame(Maquinaexpendedora_form)
        self.Monedas_Frame.setObjectName(u"Monedas_Frame")
        self.Monedas_Frame.setGeometry(QRect(0, 300, 761, 121))
        self.Monedas_Frame.setStyleSheet(u"background-color: rgb(176, 176, 176);")
        self.Monedas_Frame.setFrameShape(QFrame.StyledPanel)
        self.Monedas_Frame.setFrameShadow(QFrame.Raised)
        self.Moneda5_pushButton = QPushButton(self.Monedas_Frame)
        self.Moneda5_pushButton.setObjectName(u"Moneda5_pushButton")
        self.Moneda5_pushButton.setGeometry(QRect(20, 30, 61, 61))
        self.Moneda5_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"./assets/5_pesos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Moneda5_pushButton.setIcon(icon)
        self.Moneda5_pushButton.setIconSize(QSize(60, 60))
        self.Moneda5_pushButton.setFlat(True)
        self.Moneda10_pushButton = QPushButton(self.Monedas_Frame)
        self.Moneda10_pushButton.setObjectName(u"Moneda10_pushButton")
        self.Moneda10_pushButton.setGeometry(QRect(100, 20, 71, 71))
        self.Moneda10_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"./assets/10_pesos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Moneda10_pushButton.setIcon(icon1)
        self.Moneda10_pushButton.setIconSize(QSize(70, 70))
        self.Moneda10_pushButton.setFlat(True)
        self.billete20_pushButton = QPushButton(self.Monedas_Frame)
        self.billete20_pushButton.setObjectName(u"billete20_pushButton")
        self.billete20_pushButton.setGeometry(QRect(200, 20, 171, 91))
        self.billete20_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"./assets/20_pesos.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.billete20_pushButton.setIcon(icon2)
        self.billete20_pushButton.setIconSize(QSize(200, 90))
        self.billete20_pushButton.setFlat(True)
        self.billete50_pushButton = QPushButton(self.Monedas_Frame)
        self.billete50_pushButton.setObjectName(u"billete50_pushButton")
        self.billete50_pushButton.setGeometry(QRect(400, 10, 211, 101))
        self.billete50_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"./assets/50-pesos.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.billete50_pushButton.setIcon(icon3)
        self.billete50_pushButton.setIconSize(QSize(200, 150))
        self.billete50_pushButton.setFlat(True)
        self.sacarDinero_pushButton = QPushButton(self.Monedas_Frame)
        self.sacarDinero_pushButton.setObjectName(u"sacarDinero_pushButton")
        self.sacarDinero_pushButton.setGeometry(QRect(640, 30, 101, 61))
        self.sacarDinero_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sacarDinero_pushButton.setStyleSheet(u"QpushButton:hover{\n"
"border-radius:20px;}")
        self.sacarDinero_pushButton.setFlat(False)
        self.Coca235_pushButton = QPushButton(Maquinaexpendedora_form)
        self.Coca235_pushButton.setObjectName(u"Coca235_pushButton")
        self.Coca235_pushButton.setGeometry(QRect(50, 80, 81, 151))
        self.Coca235_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"./assets/Coca_235ml-PhotoRoom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Coca235_pushButton.setIcon(icon4)
        self.Coca235_pushButton.setIconSize(QSize(70, 200))
        self.Coca235_pushButton.setFlat(True)
        self.Coca355_pushButton = QPushButton(Maquinaexpendedora_form)
        self.Coca355_pushButton.setObjectName(u"Coca355_pushButton")
        self.Coca355_pushButton.setGeometry(QRect(190, 0, 91, 231))
        self.Coca355_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"./assets/Coca_355ml-PhotoRoom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Coca355_pushButton.setIcon(icon5)
        self.Coca355_pushButton.setIconSize(QSize(250, 300))
        self.Coca355_pushButton.setFlat(True)
        self.Redbull_pushButton = QPushButton(Maquinaexpendedora_form)
        self.Redbull_pushButton.setObjectName(u"Redbull_pushButton")
        self.Redbull_pushButton.setGeometry(QRect(340, 10, 91, 231))
        self.Redbull_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"./assets/RedBull_250ml-PhotoRoom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Redbull_pushButton.setIcon(icon6)
        self.Redbull_pushButton.setIconSize(QSize(250, 300))
        self.Redbull_pushButton.setFlat(True)
        self.Dinero_frame = QFrame(Maquinaexpendedora_form)
        self.Dinero_frame.setObjectName(u"Dinero_frame")
        self.Dinero_frame.setGeometry(QRect(500, 0, 261, 141))
        self.Dinero_frame.setStyleSheet(u"background-color: rgb(130, 255, 85);")
        self.Dinero_frame.setFrameShape(QFrame.StyledPanel)
        self.Dinero_frame.setFrameShadow(QFrame.Raised)
        self.tituloDinero_label = QLabel(self.Dinero_frame)
        self.tituloDinero_label.setObjectName(u"tituloDinero_label")
        self.tituloDinero_label.setGeometry(QRect(0, 0, 261, 61))
        font1 = QFont()
        font1.setPointSize(14)
        self.tituloDinero_label.setFont(font1)
        self.tituloDinero_label.setScaledContents(False)
        self.tituloDinero_label.setAlignment(Qt.AlignCenter)
        self.dineroDisponible_label = QLabel(self.Dinero_frame)
        self.dineroDisponible_label.setObjectName(u"dineroDisponible_label")
        self.dineroDisponible_label.setGeometry(QRect(70, 70, 191, 71))
        font2 = QFont()
        font2.setPointSize(16)
        self.dineroDisponible_label.setFont(font2)
        self.dineroDisponible_label.setAlignment(Qt.AlignCenter)
        self.simboloDineroDisponible_label = QLabel(self.Dinero_frame)
        self.simboloDineroDisponible_label.setObjectName(u"simboloDineroDisponible_label")
        self.simboloDineroDisponible_label.setGeometry(QRect(0, 65, 55, 71))
        self.simboloDineroDisponible_label.setFont(font2)
        self.simboloDineroDisponible_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.alertas_label = QLabel(Maquinaexpendedora_form)
        self.alertas_label.setObjectName(u"alertas_label")
        self.alertas_label.setGeometry(QRect(500, 140, 261, 161))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.alertas_label.setFont(font3)
        self.alertas_label.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.alertas_label.setAcceptDrops(True)
        self.alertas_label.setAutoFillBackground(False)
        self.alertas_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.alertas_label.setTextFormat(Qt.MarkdownText)
        self.alertas_label.setScaledContents(False)
        self.alertas_label.setAlignment(Qt.AlignCenter)
        self.alertas_label.setWordWrap(True)
        self.nombreC235_label = QLabel(Maquinaexpendedora_form)
        self.nombreC235_label.setObjectName(u"nombreC235_label")
        self.nombreC235_label.setGeometry(QRect(30, 240, 121, 21))
        self.nombreC235_label.setAlignment(Qt.AlignCenter)
        self.costoC235_label = QLabel(Maquinaexpendedora_form)
        self.costoC235_label.setObjectName(u"costoC235_label")
        self.costoC235_label.setGeometry(QRect(60, 270, 55, 16))
        self.costoC235_label.setAlignment(Qt.AlignCenter)
        self.costoC355_label = QLabel(Maquinaexpendedora_form)
        self.costoC355_label.setObjectName(u"costoC355_label")
        self.costoC355_label.setGeometry(QRect(200, 270, 55, 16))
        self.costoC355_label.setAlignment(Qt.AlignCenter)
        self.nombreC355_label = QLabel(Maquinaexpendedora_form)
        self.nombreC355_label.setObjectName(u"nombreC355_label")
        self.nombreC355_label.setGeometry(QRect(170, 240, 121, 21))
        self.nombreC355_label.setAlignment(Qt.AlignCenter)
        self.nombreC235_label_3 = QLabel(Maquinaexpendedora_form)
        self.nombreC235_label_3.setObjectName(u"nombreC235_label_3")
        self.nombreC235_label_3.setGeometry(QRect(330, 240, 121, 21))
        self.nombreC235_label_3.setAlignment(Qt.AlignCenter)
        self.costoRed_label = QLabel(Maquinaexpendedora_form)
        self.costoRed_label.setObjectName(u"costoRed_label")
        self.costoRed_label.setGeometry(QRect(360, 266, 55, 20))
        self.costoRed_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Maquinaexpendedora_form)

        QMetaObject.connectSlotsByName(Maquinaexpendedora_form)
    # setupUi

    def retranslateUi(self, Maquinaexpendedora_form):
        Maquinaexpendedora_form.setWindowTitle(QCoreApplication.translate("Maquinaexpendedora_form", u"M\u00e1quina expendedora", None))
        self.productoEntregado_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"Producto entregado", None))
        self.cambio_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"Cambio", None))
        self.productoEntregadoNombre_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"nada", None))
        self.cambioCantidad_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"0", None))
        self.simboloCambio_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"$", None))
        self.Moneda5_pushButton.setText("")
        self.Moneda10_pushButton.setText("")
        self.billete20_pushButton.setText("")
        self.billete50_pushButton.setText("")
        self.sacarDinero_pushButton.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"Sacar dinero", None))
        self.Coca235_pushButton.setText("")
        self.Coca355_pushButton.setText("")
        self.Redbull_pushButton.setText("")
        self.tituloDinero_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"Dinero disponible", None))
        self.dineroDisponible_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"0", None))
        self.simboloDineroDisponible_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"$", None))
        self.alertas_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"A ver tenemos que ver si esto se llena", None))
        self.nombreC235_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"Coca-cola 235 ml", None))
        self.costoC235_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"$15", None))
        self.costoC355_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"$20", None))
        self.nombreC355_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"Coca-cola 355 ml", None))
        self.nombreC235_label_3.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"Red bull 250 ml", None))
        self.costoRed_label.setText(QCoreApplication.translate("Maquinaexpendedora_form", u"$40", None))
    # retranslateUi

