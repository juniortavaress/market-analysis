# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1584, 1056)
        Widget.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.welcomePage = QWidget()
        self.welcomePage.setObjectName(u"welcomePage")
        self.verticalLayout_2 = QVBoxLayout(self.welcomePage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.welcomePage)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_error = QFrame(self.frame)
        self.frame_error.setObjectName(u"frame_error")
        self.frame_error.setMaximumSize(QSize(450, 30))
        self.frame_error.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border-radius: 5px;")
        self.frame_error.setFrameShape(QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 3, 10, 3)
        self.label_error = QLabel(self.frame_error)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setStyleSheet(u"color: rgb(98, 168, 254);")
        self.label_error.setAlignment(Qt.AlignCenter)
        self.label_error.setIndent(-1)

        self.horizontalLayout_6.addWidget(self.label_error)

        self.pushButton_close = QPushButton(self.frame_error)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setEnabled(True)
        self.pushButton_close.setMaximumSize(QSize(20, 20))
        self.pushButton_close.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(200, 200, 200);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_close)


        self.horizontalLayout.addWidget(self.frame_error)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.welcomePage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(600, 550))
        self.frame_9.setMaximumSize(QSize(600, 600))
        self.frame_9.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, 0, 0)
        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 90))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_64 = QLabel(self.frame_15)
        self.label_64.setObjectName(u"label_64")
        font = QFont()
        font.setPointSize(25)
        self.label_64.setFont(font)
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_64)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.InformationFrame_2 = QFrame(self.frame_9)
        self.InformationFrame_2.setObjectName(u"InformationFrame_2")
        self.InformationFrame_2.setFrameShape(QFrame.StyledPanel)
        self.InformationFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.InformationFrame_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_15 = QLabel(self.InformationFrame_2)
        self.label_15.setObjectName(u"label_15")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_15)

        self.GenderBox_2 = QFrame(self.InformationFrame_2)
        self.GenderBox_2.setObjectName(u"GenderBox_2")
        self.GenderBox_2.setStyleSheet(u"QCheckBox::indicator{\n"
"	background: #5E5E5E;\n"
"	border: 1px solid rgba(0, 170, 255, 0.71);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	background-color: rgb(69, 118, 178);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"}\n"
"\n"
"")
        self.GenderBox_2.setFrameShape(QFrame.NoFrame)
        self.GenderBox_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.GenderBox_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(170, -1, 50, -1)
        self.acoes = QCheckBox(self.GenderBox_2)
        self.acoes.setObjectName(u"acoes")
        self.acoes.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.acoes.setFont(font2)
        self.acoes.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.acoes.setIconSize(QSize(31, 30))
        self.acoes.setAutoExclusive(True)

        self.horizontalLayout_16.addWidget(self.acoes)

        self.fiis = QCheckBox(self.GenderBox_2)
        self.fiis.setObjectName(u"fiis")
        self.fiis.setFont(font2)
        self.fiis.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.fiis.setAutoExclusive(True)

        self.horizontalLayout_16.addWidget(self.fiis)


        self.verticalLayout_14.addWidget(self.GenderBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)

        self.label_16 = QLabel(self.InformationFrame_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(520, 0))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_16)

        self.KnowledgeBox_2 = QFrame(self.InformationFrame_2)
        self.KnowledgeBox_2.setObjectName(u"KnowledgeBox_2")
        self.KnowledgeBox_2.setStyleSheet(u"QCheckBox::indicator{\n"
"	background: #5E5E5E;\n"
"	border: 1px solid rgba(0, 170, 255, 0.71);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	background-color: rgb(69, 118, 178);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.KnowledgeBox_2.setFrameShape(QFrame.NoFrame)
        self.KnowledgeBox_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.KnowledgeBox_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(170, -1, 50, -1)
        self.yes = QCheckBox(self.KnowledgeBox_2)
        self.yes.setObjectName(u"yes")
        self.yes.setMinimumSize(QSize(0, 50))
        self.yes.setFont(font2)
        self.yes.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.yes.setIconSize(QSize(31, 30))
        self.yes.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.yes)

        self.no = QCheckBox(self.KnowledgeBox_2)
        self.no.setObjectName(u"no")
        self.no.setFont(font2)
        self.no.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.no.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.no)


        self.verticalLayout_14.addWidget(self.KnowledgeBox_2)

        self.verticalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_15)

        self.label_72 = QLabel(self.InformationFrame_2)
        self.label_72.setObjectName(u"label_72")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(18)
        self.label_72.setFont(font4)
        self.label_72.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_72)

        self.KnowledgeBox_4 = QFrame(self.InformationFrame_2)
        self.KnowledgeBox_4.setObjectName(u"KnowledgeBox_4")
        self.KnowledgeBox_4.setMinimumSize(QSize(0, 30))
        self.KnowledgeBox_4.setStyleSheet(u"")
        self.KnowledgeBox_4.setFrameShape(QFrame.NoFrame)
        self.KnowledgeBox_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.KnowledgeBox_4)
        self.horizontalLayout_111.setSpacing(0)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.path = QLineEdit(self.KnowledgeBox_4)
        self.path.setObjectName(u"path")
        self.path.setMaximumSize(QSize(250, 25))
        self.path.setStyleSheet(u"background: #5E5E5E;\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(0, 170, 255, 0.71);")

        self.horizontalLayout_111.addWidget(self.path)


        self.verticalLayout_14.addWidget(self.KnowledgeBox_4)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer)


        self.verticalLayout_11.addWidget(self.InformationFrame_2)

        self.ButtonFrame_2 = QFrame(self.frame_9)
        self.ButtonFrame_2.setObjectName(u"ButtonFrame_2")
        self.ButtonFrame_2.setMaximumSize(QSize(16777215, 80))
        self.ButtonFrame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:1, stop:0.2746 rgba(217, 217, 217, 255), stop:0.287185 rgba(175, 175, 175, 255));\n"
"padding-top:8px;\n"
"\n"
"")
        self.ButtonFrame_2.setFrameShape(QFrame.NoFrame)
        self.ButtonFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.ButtonFrame_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)

        self.NextWelcome = QPushButton(self.ButtonFrame_2)
        self.NextWelcome.setObjectName(u"NextWelcome")
        self.NextWelcome.setMinimumSize(QSize(185, 50))
        self.NextWelcome.setMaximumSize(QSize(185, 50))
        self.NextWelcome.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(69, 118, 178);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 22pt \"Arial\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"    background-color:rgb(98, 168, 254);\n"
"}")

        self.horizontalLayout_18.addWidget(self.NextWelcome)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_7)


        self.verticalLayout_11.addWidget(self.ButtonFrame_2)


        self.horizontalLayout_2.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.welcomePage)
        self.loadingPage = QWidget()
        self.loadingPage.setObjectName(u"loadingPage")
        self.horizontalLayout_26 = QHBoxLayout(self.loadingPage)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame2 = QFrame(self.loadingPage)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setMaximumSize(QSize(110, 110))
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_26.addWidget(self.frame2)

        self.stackedWidget.addWidget(self.loadingPage)
        self.stocksOptionsPage = QWidget()
        self.stocksOptionsPage.setObjectName(u"stocksOptionsPage")
        self.horizontalLayout_4 = QHBoxLayout(self.stocksOptionsPage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_10 = QFrame(self.stocksOptionsPage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(600, 550))
        self.frame_10.setMaximumSize(QSize(600, 600))
        self.frame_10.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)

        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 90))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_65 = QLabel(self.frame_16)
        self.label_65.setObjectName(u"label_65")
        font5 = QFont()
        font5.setPointSize(22)
        self.label_65.setFont(font5)
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_65)


        self.verticalLayout_12.addWidget(self.frame_16)

        self.InformationFrame_3 = QFrame(self.frame_10)
        self.InformationFrame_3.setObjectName(u"InformationFrame_3")
        self.InformationFrame_3.setFrameShape(QFrame.StyledPanel)
        self.InformationFrame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.InformationFrame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.GenderBox_3 = QFrame(self.InformationFrame_3)
        self.GenderBox_3.setObjectName(u"GenderBox_3")
        self.GenderBox_3.setStyleSheet(u"QCheckBox::indicator{\n"
"	background: #5E5E5E;\n"
"	border: 1px solid rgba(0, 170, 255, 0.71);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	background: rgba(50, 170, 255, 0.58);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"}\n"
"\n"
"")
        self.GenderBox_3.setFrameShape(QFrame.NoFrame)
        self.GenderBox_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.GenderBox_3)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(50, 0, 40, 0)
        self.frame_6 = QFrame(self.GenderBox_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.DY = QCheckBox(self.frame_6)
        self.DY.setObjectName(u"DY")
        self.DY.setMinimumSize(QSize(0, 0))
        self.DY.setFont(font2)
        self.DY.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.DY.setIconSize(QSize(31, 30))
        self.DY.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.DY)

        self.PL = QCheckBox(self.frame_6)
        self.PL.setObjectName(u"PL")
        self.PL.setFont(font2)
        self.PL.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.PL.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.PL)

        self.PVP = QCheckBox(self.frame_6)
        self.PVP.setObjectName(u"PVP")
        self.PVP.setFont(font2)
        self.PVP.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.PVP.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.PVP)

        self.MargemEbit = QCheckBox(self.frame_6)
        self.MargemEbit.setObjectName(u"MargemEbit")
        self.MargemEbit.setFont(font2)
        self.MargemEbit.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.MargemEbit.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.MargemEbit)

        self.Margem = QCheckBox(self.frame_6)
        self.Margem.setObjectName(u"Margem")
        self.Margem.setFont(font2)
        self.Margem.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Margem.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.Margem)

        self.P_EBIT = QCheckBox(self.frame_6)
        self.P_EBIT.setObjectName(u"P_EBIT")
        self.P_EBIT.setFont(font2)
        self.P_EBIT.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.P_EBIT.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.P_EBIT)

        self.Divida_Pat = QCheckBox(self.frame_6)
        self.Divida_Pat.setObjectName(u"Divida_Pat")
        self.Divida_Pat.setFont(font2)
        self.Divida_Pat.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Divida_Pat.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.Divida_Pat)

        self.P_Cap = QCheckBox(self.frame_6)
        self.P_Cap.setObjectName(u"P_Cap")
        self.P_Cap.setFont(font2)
        self.P_Cap.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.P_Cap.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.P_Cap)

        self.ROE = QCheckBox(self.frame_6)
        self.ROE.setObjectName(u"ROE")
        self.ROE.setFont(font2)
        self.ROE.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.ROE.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.ROE)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.GenderBox_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ROA = QCheckBox(self.frame_5)
        self.ROA.setObjectName(u"ROA")
        self.ROA.setMinimumSize(QSize(0, 0))
        self.ROA.setFont(font2)
        self.ROA.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.ROA.setIconSize(QSize(31, 30))
        self.ROA.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.ROA)

        self.ROIC = QCheckBox(self.frame_5)
        self.ROIC.setObjectName(u"ROIC")
        self.ROIC.setFont(font2)
        self.ROIC.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.ROIC.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.ROIC)

        self.PatAti = QCheckBox(self.frame_5)
        self.PatAti.setObjectName(u"PatAti")
        self.PatAti.setFont(font2)
        self.PatAti.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.PatAti.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.PatAti)

        self.PasAti = QCheckBox(self.frame_5)
        self.PasAti.setObjectName(u"PasAti")
        self.PasAti.setFont(font2)
        self.PasAti.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.PasAti.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.PasAti)

        self.CAGRR = QCheckBox(self.frame_5)
        self.CAGRR.setObjectName(u"CAGRR")
        self.CAGRR.setFont(font2)
        self.CAGRR.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.CAGRR.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.CAGRR)

        self.CAGRL = QCheckBox(self.frame_5)
        self.CAGRL.setObjectName(u"CAGRL")
        self.CAGRL.setFont(font2)
        self.CAGRL.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.CAGRL.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.CAGRL)

        self.Liquidez = QCheckBox(self.frame_5)
        self.Liquidez.setObjectName(u"Liquidez")
        self.Liquidez.setFont(font2)
        self.Liquidez.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Liquidez.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.Liquidez)

        self.PEG = QCheckBox(self.frame_5)
        self.PEG.setObjectName(u"PEG")
        self.PEG.setFont(font2)
        self.PEG.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.PEG.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.PEG)

        self.Valor = QCheckBox(self.frame_5)
        self.Valor.setObjectName(u"Valor")
        self.Valor.setFont(font2)
        self.Valor.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Valor.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.Valor)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_15.addWidget(self.GenderBox_3)

        self.verticalSpacer_6 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_6)


        self.verticalLayout_12.addWidget(self.InformationFrame_3)

        self.ButtonFrame_3 = QFrame(self.frame_10)
        self.ButtonFrame_3.setObjectName(u"ButtonFrame_3")
        self.ButtonFrame_3.setMaximumSize(QSize(16777215, 80))
        self.ButtonFrame_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:1, stop:0.2746 rgba(217, 217, 217, 255), stop:0.287185 rgba(175, 175, 175, 255));\n"
"padding-top:8px;\n"
"\n"
"")
        self.ButtonFrame_3.setFrameShape(QFrame.NoFrame)
        self.ButtonFrame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.ButtonFrame_3)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)

        self.stocksOptions = QPushButton(self.ButtonFrame_3)
        self.stocksOptions.setObjectName(u"stocksOptions")
        self.stocksOptions.setMinimumSize(QSize(185, 50))
        self.stocksOptions.setMaximumSize(QSize(185, 50))
        self.stocksOptions.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(69, 118, 178);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 22pt \"Arial\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"    background-color:rgb(98, 168, 254);\n"
"}")

        self.horizontalLayout_21.addWidget(self.stocksOptions)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_9)


        self.verticalLayout_12.addWidget(self.ButtonFrame_3)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.stocksOptionsPage)
        self.stocksFiltersPage = QWidget()
        self.stocksFiltersPage.setObjectName(u"stocksFiltersPage")
        self.horizontalLayout_9 = QHBoxLayout(self.stocksFiltersPage)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_14 = QFrame(self.stocksFiltersPage)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(600, 700))
        self.frame_14.setMaximumSize(QSize(600, 700))
        self.frame_14.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_14)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_10)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(34, 0, 25, 0)
        self.label_68 = QLabel(self.frame_19)
        self.label_68.setObjectName(u"label_68")
        font6 = QFont()
        font6.setPointSize(17)
        self.label_68.setFont(font6)
        self.label_68.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_68)

        self.label_2 = QLabel(self.frame_19)
        self.label_2.setObjectName(u"label_2")
        font7 = QFont()
        font7.setPointSize(15)
        self.label_2.setFont(font7)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_19)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_3)


        self.verticalLayout_19.addWidget(self.frame_19)

        self.frame_4 = QFrame(self.frame_14)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 10))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(550, 16777215))
        self.line.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line)


        self.verticalLayout_19.addWidget(self.frame_4)

        self.InformationFrame_6 = QFrame(self.frame_14)
        self.InformationFrame_6.setObjectName(u"InformationFrame_6")
        self.InformationFrame_6.setFrameShape(QFrame.StyledPanel)
        self.InformationFrame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.InformationFrame_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.fDY = QFrame(self.InformationFrame_6)
        self.fDY.setObjectName(u"fDY")
        self.fDY.setFrameShape(QFrame.StyledPanel)
        self.fDY.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.fDY)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(30, 0, -1, 0)
        self.label_24 = QLabel(self.fDY)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(185, 0))
        self.label_24.setMaximumSize(QSize(185, 150))
        self.label_24.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_24)

        self.frame_24 = QFrame(self.fDY)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(35, 0, 50, 0)
        self.min_DY = QLineEdit(self.frame_24)
        self.min_DY.setObjectName(u"min_DY")
        self.min_DY.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_13.addWidget(self.min_DY)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.max_DY = QLineEdit(self.frame_24)
        self.max_DY.setObjectName(u"max_DY")
        self.max_DY.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_13.addWidget(self.max_DY)


        self.horizontalLayout_12.addWidget(self.frame_24)


        self.verticalLayout_20.addWidget(self.fDY)

        self.fPL = QFrame(self.InformationFrame_6)
        self.fPL.setObjectName(u"fPL")
        self.fPL.setFrameShape(QFrame.StyledPanel)
        self.fPL.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.fPL)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(30, 0, -1, 0)
        self.label_42 = QLabel(self.fPL)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(185, 0))
        self.label_42.setMaximumSize(QSize(185, 150))
        self.label_42.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_60.addWidget(self.label_42)

        self.frame_28 = QFrame(self.fPL)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(35, 0, 50, 0)
        self.min_PL = QLineEdit(self.frame_28)
        self.min_PL.setObjectName(u"min_PL")
        self.min_PL.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_61.addWidget(self.min_PL)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_29)

        self.max_PL = QLineEdit(self.frame_28)
        self.max_PL.setObjectName(u"max_PL")
        self.max_PL.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_61.addWidget(self.max_PL)


        self.horizontalLayout_60.addWidget(self.frame_28)


        self.verticalLayout_20.addWidget(self.fPL)

        self.fPVP = QFrame(self.InformationFrame_6)
        self.fPVP.setObjectName(u"fPVP")
        self.fPVP.setFrameShape(QFrame.StyledPanel)
        self.fPVP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.fPVP)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(30, 0, -1, 0)
        self.label_43 = QLabel(self.fPVP)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(185, 0))
        self.label_43.setMaximumSize(QSize(185, 150))
        self.label_43.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_62.addWidget(self.label_43)

        self.frame_32 = QFrame(self.fPVP)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(35, 0, 50, 0)
        self.min_PVP = QLineEdit(self.frame_32)
        self.min_PVP.setObjectName(u"min_PVP")
        self.min_PVP.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_63.addWidget(self.min_PVP)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_30)

        self.max_PVP = QLineEdit(self.frame_32)
        self.max_PVP.setObjectName(u"max_PVP")
        self.max_PVP.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_63.addWidget(self.max_PVP)


        self.horizontalLayout_62.addWidget(self.frame_32)


        self.verticalLayout_20.addWidget(self.fPVP)

        self.fMargemEbit = QFrame(self.InformationFrame_6)
        self.fMargemEbit.setObjectName(u"fMargemEbit")
        self.fMargemEbit.setFrameShape(QFrame.StyledPanel)
        self.fMargemEbit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.fMargemEbit)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(30, 0, -1, 0)
        self.label_45 = QLabel(self.fMargemEbit)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(185, 0))
        self.label_45.setMaximumSize(QSize(185, 150))
        self.label_45.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_45.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_66.addWidget(self.label_45)

        self.frame_40 = QFrame(self.fMargemEbit)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(35, 0, 50, 0)
        self.min_MargemEbit = QLineEdit(self.frame_40)
        self.min_MargemEbit.setObjectName(u"min_MargemEbit")
        self.min_MargemEbit.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_67.addWidget(self.min_MargemEbit)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_32)

        self.max_MargemEbit = QLineEdit(self.frame_40)
        self.max_MargemEbit.setObjectName(u"max_MargemEbit")
        self.max_MargemEbit.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_67.addWidget(self.max_MargemEbit)


        self.horizontalLayout_66.addWidget(self.frame_40)


        self.verticalLayout_20.addWidget(self.fMargemEbit)

        self.fMargem = QFrame(self.InformationFrame_6)
        self.fMargem.setObjectName(u"fMargem")
        self.fMargem.setFrameShape(QFrame.StyledPanel)
        self.fMargem.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.fMargem)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(30, 0, -1, 0)
        self.label_58 = QLabel(self.fMargem)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(185, 0))
        self.label_58.setMaximumSize(QSize(185, 150))
        self.label_58.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_58.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_92.addWidget(self.label_58)

        self.frame_74 = QFrame(self.fMargem)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(35, 0, 50, 0)
        self.min_Margem = QLineEdit(self.frame_74)
        self.min_Margem.setObjectName(u"min_Margem")
        self.min_Margem.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_93.addWidget(self.min_Margem)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_45)

        self.max_Margem = QLineEdit(self.frame_74)
        self.max_Margem.setObjectName(u"max_Margem")
        self.max_Margem.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_93.addWidget(self.max_Margem)


        self.horizontalLayout_92.addWidget(self.frame_74)


        self.verticalLayout_20.addWidget(self.fMargem)

        self.fP_EBIT = QFrame(self.InformationFrame_6)
        self.fP_EBIT.setObjectName(u"fP_EBIT")
        self.fP_EBIT.setFrameShape(QFrame.StyledPanel)
        self.fP_EBIT.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.fP_EBIT)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(30, 0, -1, 0)
        self.label_44 = QLabel(self.fP_EBIT)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(185, 0))
        self.label_44.setMaximumSize(QSize(185, 150))
        self.label_44.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_64.addWidget(self.label_44)

        self.frame_36 = QFrame(self.fP_EBIT)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(35, 0, 50, 0)
        self.min_P_EBIT = QLineEdit(self.frame_36)
        self.min_P_EBIT.setObjectName(u"min_P_EBIT")
        self.min_P_EBIT.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_65.addWidget(self.min_P_EBIT)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_31)

        self.max_P_EBIT = QLineEdit(self.frame_36)
        self.max_P_EBIT.setObjectName(u"max_P_EBIT")
        self.max_P_EBIT.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_65.addWidget(self.max_P_EBIT)


        self.horizontalLayout_64.addWidget(self.frame_36)


        self.verticalLayout_20.addWidget(self.fP_EBIT)

        self.fDivida_Pat = QFrame(self.InformationFrame_6)
        self.fDivida_Pat.setObjectName(u"fDivida_Pat")
        self.fDivida_Pat.setFrameShape(QFrame.StyledPanel)
        self.fDivida_Pat.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.fDivida_Pat)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(30, 0, -1, 0)
        self.label_46 = QLabel(self.fDivida_Pat)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(185, 0))
        self.label_46.setMaximumSize(QSize(185, 150))
        self.label_46.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_68.addWidget(self.label_46)

        self.frame_44 = QFrame(self.fDivida_Pat)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(35, 0, 50, 0)
        self.min_Divida_Pat = QLineEdit(self.frame_44)
        self.min_Divida_Pat.setObjectName(u"min_Divida_Pat")
        self.min_Divida_Pat.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_69.addWidget(self.min_Divida_Pat)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_33)

        self.max_Divida_Pat = QLineEdit(self.frame_44)
        self.max_Divida_Pat.setObjectName(u"max_Divida_Pat")
        self.max_Divida_Pat.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_69.addWidget(self.max_Divida_Pat)


        self.horizontalLayout_68.addWidget(self.frame_44)


        self.verticalLayout_20.addWidget(self.fDivida_Pat)

        self.fP_Cap = QFrame(self.InformationFrame_6)
        self.fP_Cap.setObjectName(u"fP_Cap")
        self.fP_Cap.setFrameShape(QFrame.StyledPanel)
        self.fP_Cap.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.fP_Cap)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(30, 0, -1, 0)
        self.label_49 = QLabel(self.fP_Cap)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(185, 0))
        self.label_49.setMaximumSize(QSize(185, 150))
        self.label_49.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_74.addWidget(self.label_49)

        self.frame_56 = QFrame(self.fP_Cap)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(35, 0, 50, 0)
        self.min_P_Cap = QLineEdit(self.frame_56)
        self.min_P_Cap.setObjectName(u"min_P_Cap")
        self.min_P_Cap.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_75.addWidget(self.min_P_Cap)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_36)

        self.max_P_Cap = QLineEdit(self.frame_56)
        self.max_P_Cap.setObjectName(u"max_P_Cap")
        self.max_P_Cap.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_75.addWidget(self.max_P_Cap)


        self.horizontalLayout_74.addWidget(self.frame_56)


        self.verticalLayout_20.addWidget(self.fP_Cap)

        self.fROE = QFrame(self.InformationFrame_6)
        self.fROE.setObjectName(u"fROE")
        self.fROE.setFrameShape(QFrame.StyledPanel)
        self.fROE.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.fROE)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(30, 0, -1, 0)
        self.label_48 = QLabel(self.fROE)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(185, 0))
        self.label_48.setMaximumSize(QSize(185, 150))
        self.label_48.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_72.addWidget(self.label_48)

        self.frame_52 = QFrame(self.fROE)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(35, 0, 50, 0)
        self.min_ROE = QLineEdit(self.frame_52)
        self.min_ROE.setObjectName(u"min_ROE")
        self.min_ROE.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_73.addWidget(self.min_ROE)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_35)

        self.max_ROE = QLineEdit(self.frame_52)
        self.max_ROE.setObjectName(u"max_ROE")
        self.max_ROE.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_73.addWidget(self.max_ROE)


        self.horizontalLayout_72.addWidget(self.frame_52)


        self.verticalLayout_20.addWidget(self.fROE)

        self.fROA = QFrame(self.InformationFrame_6)
        self.fROA.setObjectName(u"fROA")
        self.fROA.setFrameShape(QFrame.StyledPanel)
        self.fROA.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.fROA)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(30, 0, -1, 0)
        self.label_47 = QLabel(self.fROA)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(185, 0))
        self.label_47.setMaximumSize(QSize(185, 150))
        self.label_47.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_70.addWidget(self.label_47)

        self.frame_48 = QFrame(self.fROA)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(35, 0, 50, 0)
        self.min_ROA = QLineEdit(self.frame_48)
        self.min_ROA.setObjectName(u"min_ROA")
        self.min_ROA.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_71.addWidget(self.min_ROA)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_34)

        self.max_ROA = QLineEdit(self.frame_48)
        self.max_ROA.setObjectName(u"max_ROA")
        self.max_ROA.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_71.addWidget(self.max_ROA)


        self.horizontalLayout_70.addWidget(self.frame_48)


        self.verticalLayout_20.addWidget(self.fROA)

        self.fROIC = QFrame(self.InformationFrame_6)
        self.fROIC.setObjectName(u"fROIC")
        self.fROIC.setFrameShape(QFrame.StyledPanel)
        self.fROIC.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.fROIC)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(30, 0, -1, 0)
        self.label_51 = QLabel(self.fROIC)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(185, 0))
        self.label_51.setMaximumSize(QSize(185, 150))
        self.label_51.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_78.addWidget(self.label_51)

        self.frame_61 = QFrame(self.fROIC)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(35, 0, 50, 0)
        self.min_ROIC = QLineEdit(self.frame_61)
        self.min_ROIC.setObjectName(u"min_ROIC")
        self.min_ROIC.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_79.addWidget(self.min_ROIC)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_38)

        self.max_ROIC = QLineEdit(self.frame_61)
        self.max_ROIC.setObjectName(u"max_ROIC")
        self.max_ROIC.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_79.addWidget(self.max_ROIC)


        self.horizontalLayout_78.addWidget(self.frame_61)


        self.verticalLayout_20.addWidget(self.fROIC)

        self.fPatAti = QFrame(self.InformationFrame_6)
        self.fPatAti.setObjectName(u"fPatAti")
        self.fPatAti.setFrameShape(QFrame.StyledPanel)
        self.fPatAti.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.fPatAti)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(30, 0, -1, 0)
        self.label_50 = QLabel(self.fPatAti)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(185, 0))
        self.label_50.setMaximumSize(QSize(185, 150))
        self.label_50.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_76.addWidget(self.label_50)

        self.frame_59 = QFrame(self.fPatAti)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(35, 0, 50, 0)
        self.min_PatAti = QLineEdit(self.frame_59)
        self.min_PatAti.setObjectName(u"min_PatAti")
        self.min_PatAti.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_77.addWidget(self.min_PatAti)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_37)

        self.max_PatAti = QLineEdit(self.frame_59)
        self.max_PatAti.setObjectName(u"max_PatAti")
        self.max_PatAti.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_77.addWidget(self.max_PatAti)


        self.horizontalLayout_76.addWidget(self.frame_59)


        self.verticalLayout_20.addWidget(self.fPatAti)

        self.fPasAti = QFrame(self.InformationFrame_6)
        self.fPasAti.setObjectName(u"fPasAti")
        self.fPasAti.setFrameShape(QFrame.StyledPanel)
        self.fPasAti.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.fPasAti)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(30, 0, -1, 0)
        self.label_52 = QLabel(self.fPasAti)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(185, 0))
        self.label_52.setMaximumSize(QSize(185, 150))
        self.label_52.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_80.addWidget(self.label_52)

        self.frame_63 = QFrame(self.fPasAti)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(35, 0, 50, 0)
        self.min_PasAti = QLineEdit(self.frame_63)
        self.min_PasAti.setObjectName(u"min_PasAti")
        self.min_PasAti.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_81.addWidget(self.min_PasAti)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_39)

        self.max_PasAti = QLineEdit(self.frame_63)
        self.max_PasAti.setObjectName(u"max_PasAti")
        self.max_PasAti.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_81.addWidget(self.max_PasAti)


        self.horizontalLayout_80.addWidget(self.frame_63)


        self.verticalLayout_20.addWidget(self.fPasAti)

        self.fCAGRR = QFrame(self.InformationFrame_6)
        self.fCAGRR.setObjectName(u"fCAGRR")
        self.fCAGRR.setFrameShape(QFrame.StyledPanel)
        self.fCAGRR.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.fCAGRR)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(30, 0, -1, 0)
        self.label_54 = QLabel(self.fCAGRR)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(185, 0))
        self.label_54.setMaximumSize(QSize(185, 150))
        self.label_54.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_84.addWidget(self.label_54)

        self.frame_67 = QFrame(self.fCAGRR)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(35, 0, 50, 0)
        self.min_CAGRR = QLineEdit(self.frame_67)
        self.min_CAGRR.setObjectName(u"min_CAGRR")
        self.min_CAGRR.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_85.addWidget(self.min_CAGRR)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_41)

        self.max_CAGRR = QLineEdit(self.frame_67)
        self.max_CAGRR.setObjectName(u"max_CAGRR")
        self.max_CAGRR.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_85.addWidget(self.max_CAGRR)


        self.horizontalLayout_84.addWidget(self.frame_67)


        self.verticalLayout_20.addWidget(self.fCAGRR)

        self.fCAGRL = QFrame(self.InformationFrame_6)
        self.fCAGRL.setObjectName(u"fCAGRL")
        self.fCAGRL.setFrameShape(QFrame.StyledPanel)
        self.fCAGRL.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.fCAGRL)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(30, 0, -1, 0)
        self.label_53 = QLabel(self.fCAGRL)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(185, 0))
        self.label_53.setMaximumSize(QSize(185, 150))
        self.label_53.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_82.addWidget(self.label_53)

        self.frame_65 = QFrame(self.fCAGRL)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(35, 0, 50, 0)
        self.min_CAGRL = QLineEdit(self.frame_65)
        self.min_CAGRL.setObjectName(u"min_CAGRL")
        self.min_CAGRL.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_83.addWidget(self.min_CAGRL)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_40)

        self.max_CAGRL = QLineEdit(self.frame_65)
        self.max_CAGRL.setObjectName(u"max_CAGRL")
        self.max_CAGRL.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_83.addWidget(self.max_CAGRL)


        self.horizontalLayout_82.addWidget(self.frame_65)


        self.verticalLayout_20.addWidget(self.fCAGRL)

        self.fLiquidez = QFrame(self.InformationFrame_6)
        self.fLiquidez.setObjectName(u"fLiquidez")
        self.fLiquidez.setFrameShape(QFrame.StyledPanel)
        self.fLiquidez.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.fLiquidez)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(30, 0, -1, 0)
        self.label_57 = QLabel(self.fLiquidez)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(185, 0))
        self.label_57.setMaximumSize(QSize(185, 150))
        self.label_57.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_57.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_90.addWidget(self.label_57)

        self.frame_72 = QFrame(self.fLiquidez)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(35, 0, 50, 0)
        self.min_Liquidez = QLineEdit(self.frame_72)
        self.min_Liquidez.setObjectName(u"min_Liquidez")
        self.min_Liquidez.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_91.addWidget(self.min_Liquidez)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_91.addItem(self.horizontalSpacer_44)

        self.max_Liquidez = QLineEdit(self.frame_72)
        self.max_Liquidez.setObjectName(u"max_Liquidez")
        self.max_Liquidez.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_91.addWidget(self.max_Liquidez)


        self.horizontalLayout_90.addWidget(self.frame_72)


        self.verticalLayout_20.addWidget(self.fLiquidez)

        self.fPEG = QFrame(self.InformationFrame_6)
        self.fPEG.setObjectName(u"fPEG")
        self.fPEG.setFrameShape(QFrame.StyledPanel)
        self.fPEG.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.fPEG)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(30, 0, -1, 0)
        self.label_56 = QLabel(self.fPEG)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(185, 0))
        self.label_56.setMaximumSize(QSize(185, 150))
        self.label_56.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_56.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_88.addWidget(self.label_56)

        self.frame_71 = QFrame(self.fPEG)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(35, 0, 50, 0)
        self.min_PEG = QLineEdit(self.frame_71)
        self.min_PEG.setObjectName(u"min_PEG")
        self.min_PEG.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_89.addWidget(self.min_PEG)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_89.addItem(self.horizontalSpacer_43)

        self.max_PEG = QLineEdit(self.frame_71)
        self.max_PEG.setObjectName(u"max_PEG")
        self.max_PEG.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_89.addWidget(self.max_PEG)


        self.horizontalLayout_88.addWidget(self.frame_71)


        self.verticalLayout_20.addWidget(self.fPEG)

        self.fValor = QFrame(self.InformationFrame_6)
        self.fValor.setObjectName(u"fValor")
        self.fValor.setFrameShape(QFrame.StyledPanel)
        self.fValor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.fValor)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(30, 0, -1, 0)
        self.label_55 = QLabel(self.fValor)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(185, 0))
        self.label_55.setMaximumSize(QSize(185, 150))
        self.label_55.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_55.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_86.addWidget(self.label_55)

        self.frame_69 = QFrame(self.fValor)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(35, 0, 50, 0)
        self.min_Valor = QLineEdit(self.frame_69)
        self.min_Valor.setObjectName(u"min_Valor")
        self.min_Valor.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_87.addWidget(self.min_Valor)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer_42)

        self.max_Valor = QLineEdit(self.frame_69)
        self.max_Valor.setObjectName(u"max_Valor")
        self.max_Valor.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_87.addWidget(self.max_Valor)


        self.horizontalLayout_86.addWidget(self.frame_69)


        self.verticalLayout_20.addWidget(self.fValor)

        self.verticalSpacer_11 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_20.addItem(self.verticalSpacer_11)


        self.verticalLayout_19.addWidget(self.InformationFrame_6)

        self.ButtonFrame_6 = QFrame(self.frame_14)
        self.ButtonFrame_6.setObjectName(u"ButtonFrame_6")
        self.ButtonFrame_6.setMaximumSize(QSize(16777215, 80))
        self.ButtonFrame_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:1, stop:0.2746 rgba(217, 217, 217, 255), stop:0.287185 rgba(175, 175, 175, 255));\n"
"padding-top:8px;\n"
"\n"
"")
        self.ButtonFrame_6.setFrameShape(QFrame.NoFrame)
        self.ButtonFrame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.ButtonFrame_6)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_14)

        self.stocksFilters = QPushButton(self.ButtonFrame_6)
        self.stocksFilters.setObjectName(u"stocksFilters")
        self.stocksFilters.setMinimumSize(QSize(185, 50))
        self.stocksFilters.setMaximumSize(QSize(185, 50))
        self.stocksFilters.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(69, 118, 178);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 22pt \"Arial\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"    background-color:rgb(98, 168, 254);\n"
"}")

        self.horizontalLayout_25.addWidget(self.stocksFilters)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_15)


        self.verticalLayout_19.addWidget(self.ButtonFrame_6)


        self.horizontalLayout_9.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.stocksFiltersPage)
        self.fiisOptionsPage = QWidget()
        self.fiisOptionsPage.setObjectName(u"fiisOptionsPage")
        self.horizontalLayout_8 = QHBoxLayout(self.fiisOptionsPage)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_11 = QFrame(self.fiisOptionsPage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(600, 550))
        self.frame_11.setMaximumSize(QSize(600, 600))
        self.frame_11.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)

        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 90))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_66 = QLabel(self.frame_17)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font5)
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_66)


        self.verticalLayout_13.addWidget(self.frame_17)

        self.InformationFrame_4 = QFrame(self.frame_11)
        self.InformationFrame_4.setObjectName(u"InformationFrame_4")
        self.InformationFrame_4.setFrameShape(QFrame.StyledPanel)
        self.InformationFrame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.InformationFrame_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.GenderBox_4 = QFrame(self.InformationFrame_4)
        self.GenderBox_4.setObjectName(u"GenderBox_4")
        self.GenderBox_4.setStyleSheet(u"QCheckBox::indicator{\n"
"	background: #5E5E5E;\n"
"	border: 1px solid rgba(0, 170, 255, 0.71);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	background: rgba(50, 170, 255, 0.58);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"}\n"
"\n"
"")
        self.GenderBox_4.setFrameShape(QFrame.NoFrame)
        self.GenderBox_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.GenderBox_4)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, 0, 40, 0)
        self.frame_7 = QFrame(self.GenderBox_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(250, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Fiis_DY = QCheckBox(self.frame_7)
        self.Fiis_DY.setObjectName(u"Fiis_DY")
        self.Fiis_DY.setMinimumSize(QSize(0, 0))
        self.Fiis_DY.setFont(font2)
        self.Fiis_DY.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Fiis_DY.setIconSize(QSize(31, 30))
        self.Fiis_DY.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.Fiis_DY)

        self.Fiis_DY_CAGR = QCheckBox(self.frame_7)
        self.Fiis_DY_CAGR.setObjectName(u"Fiis_DY_CAGR")
        self.Fiis_DY_CAGR.setFont(font2)
        self.Fiis_DY_CAGR.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Fiis_DY_CAGR.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.Fiis_DY_CAGR)

        self.Fiis_PVP = QCheckBox(self.frame_7)
        self.Fiis_PVP.setObjectName(u"Fiis_PVP")
        self.Fiis_PVP.setFont(font2)
        self.Fiis_PVP.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Fiis_PVP.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.Fiis_PVP)

        self.Fiis_Liquidez = QCheckBox(self.frame_7)
        self.Fiis_Liquidez.setObjectName(u"Fiis_Liquidez")
        self.Fiis_Liquidez.setFont(font2)
        self.Fiis_Liquidez.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Fiis_Liquidez.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.Fiis_Liquidez)

        self.Fiis_Cotas = QCheckBox(self.frame_7)
        self.Fiis_Cotas.setObjectName(u"Fiis_Cotas")
        self.Fiis_Cotas.setFont(font2)
        self.Fiis_Cotas.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Fiis_Cotas.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.Fiis_Cotas)

        self.Fiis_Dividendo = QCheckBox(self.frame_7)
        self.Fiis_Dividendo.setObjectName(u"Fiis_Dividendo")
        self.Fiis_Dividendo.setFont(font2)
        self.Fiis_Dividendo.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Fiis_Dividendo.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.Fiis_Dividendo)

        self.Fiis_CAGR = QCheckBox(self.frame_7)
        self.Fiis_CAGR.setObjectName(u"Fiis_CAGR")
        self.Fiis_CAGR.setFont(font2)
        self.Fiis_CAGR.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Fiis_CAGR.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.Fiis_CAGR)

        self.Fiis_Valor = QCheckBox(self.frame_7)
        self.Fiis_Valor.setObjectName(u"Fiis_Valor")
        self.Fiis_Valor.setFont(font2)
        self.Fiis_Valor.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.Fiis_Valor.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.Fiis_Valor)


        self.horizontalLayout_7.addWidget(self.frame_7)


        self.verticalLayout_16.addWidget(self.GenderBox_4)

        self.verticalSpacer_7 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)


        self.verticalLayout_13.addWidget(self.InformationFrame_4)

        self.ButtonFrame_4 = QFrame(self.frame_11)
        self.ButtonFrame_4.setObjectName(u"ButtonFrame_4")
        self.ButtonFrame_4.setMaximumSize(QSize(16777215, 80))
        self.ButtonFrame_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:1, stop:0.2746 rgba(217, 217, 217, 255), stop:0.287185 rgba(175, 175, 175, 255));\n"
"padding-top:8px;\n"
"\n"
"")
        self.ButtonFrame_4.setFrameShape(QFrame.NoFrame)
        self.ButtonFrame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.ButtonFrame_4)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_10)

        self.fiisOptions = QPushButton(self.ButtonFrame_4)
        self.fiisOptions.setObjectName(u"fiisOptions")
        self.fiisOptions.setMinimumSize(QSize(185, 50))
        self.fiisOptions.setMaximumSize(QSize(185, 50))
        self.fiisOptions.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(69, 118, 178);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 22pt \"Arial\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"    background-color:rgb(98, 168, 254);\n"
"}")

        self.horizontalLayout_22.addWidget(self.fiisOptions)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_11)


        self.verticalLayout_13.addWidget(self.ButtonFrame_4)


        self.horizontalLayout_8.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.fiisOptionsPage)
        self.fiisFiltersPage = QWidget()
        self.fiisFiltersPage.setObjectName(u"fiisFiltersPage")
        self.horizontalLayout_10 = QHBoxLayout(self.fiisFiltersPage)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_18 = QFrame(self.fiisFiltersPage)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(600, 550))
        self.frame_18.setMaximumSize(QSize(600, 600))
        self.frame_18.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_12 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_21.addItem(self.verticalSpacer_12)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 50))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(34, 0, 25, 0)
        self.label_69 = QLabel(self.frame_20)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font6)
        self.label_69.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_94.addWidget(self.label_69)

        self.label_4 = QLabel(self.frame_20)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_20)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.label_5)


        self.verticalLayout_21.addWidget(self.frame_20)

        self.frame_8 = QFrame(self.frame_18)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 10))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.frame_8)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(550, 16777215))
        self.line_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.line_2)


        self.verticalLayout_21.addWidget(self.frame_8)

        self.InformationFrame_7 = QFrame(self.frame_18)
        self.InformationFrame_7.setObjectName(u"InformationFrame_7")
        self.InformationFrame_7.setFrameShape(QFrame.StyledPanel)
        self.InformationFrame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.InformationFrame_7)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.fFiis_DY = QFrame(self.InformationFrame_7)
        self.fFiis_DY.setObjectName(u"fFiis_DY")
        self.fFiis_DY.setFrameShape(QFrame.StyledPanel)
        self.fFiis_DY.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.fFiis_DY)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(30, 0, -1, 0)
        self.fDY_2 = QLabel(self.fFiis_DY)
        self.fDY_2.setObjectName(u"fDY_2")
        self.fDY_2.setMinimumSize(QSize(185, 0))
        self.fDY_2.setMaximumSize(QSize(185, 150))
        self.fDY_2.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.fDY_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.fDY_2)

        self.frame_76 = QFrame(self.fFiis_DY)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(35, 0, 50, 0)
        self.min_Fiis_DY = QLineEdit(self.frame_76)
        self.min_Fiis_DY.setObjectName(u"min_Fiis_DY")
        self.min_Fiis_DY.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_95.addWidget(self.min_Fiis_DY)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_12)

        self.max_Fiis_DY = QLineEdit(self.frame_76)
        self.max_Fiis_DY.setObjectName(u"max_Fiis_DY")
        self.max_Fiis_DY.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_95.addWidget(self.max_Fiis_DY)


        self.horizontalLayout_23.addWidget(self.frame_76)


        self.verticalLayout_22.addWidget(self.fFiis_DY)

        self.fFiis_PVP = QFrame(self.InformationFrame_7)
        self.fFiis_PVP.setObjectName(u"fFiis_PVP")
        self.fFiis_PVP.setFrameShape(QFrame.StyledPanel)
        self.fFiis_PVP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.fFiis_PVP)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(30, 0, -1, 0)
        self.label_61 = QLabel(self.fFiis_PVP)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(185, 0))
        self.label_61.setMaximumSize(QSize(185, 150))
        self.label_61.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_61.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_98.addWidget(self.label_61)

        self.frame_80 = QFrame(self.fFiis_PVP)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(35, 0, 50, 0)
        self.min_Fiis_PVP = QLineEdit(self.frame_80)
        self.min_Fiis_PVP.setObjectName(u"min_Fiis_PVP")
        self.min_Fiis_PVP.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_99.addWidget(self.min_Fiis_PVP)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_47)

        self.max_Fiis_PVP = QLineEdit(self.frame_80)
        self.max_Fiis_PVP.setObjectName(u"max_Fiis_PVP")
        self.max_Fiis_PVP.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_99.addWidget(self.max_Fiis_PVP)


        self.horizontalLayout_98.addWidget(self.frame_80)


        self.verticalLayout_22.addWidget(self.fFiis_PVP)

        self.fFiis_DY_CAGR = QFrame(self.InformationFrame_7)
        self.fFiis_DY_CAGR.setObjectName(u"fFiis_DY_CAGR")
        self.fFiis_DY_CAGR.setFrameShape(QFrame.StyledPanel)
        self.fFiis_DY_CAGR.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.fFiis_DY_CAGR)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(30, 0, -1, 0)
        self.label_62 = QLabel(self.fFiis_DY_CAGR)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(185, 0))
        self.label_62.setMaximumSize(QSize(185, 150))
        self.label_62.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_62.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_100.addWidget(self.label_62)

        self.frame_82 = QFrame(self.fFiis_DY_CAGR)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(35, 0, 50, 0)
        self.min_Fiis_DY_CAGR = QLineEdit(self.frame_82)
        self.min_Fiis_DY_CAGR.setObjectName(u"min_Fiis_DY_CAGR")
        self.min_Fiis_DY_CAGR.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_101.addWidget(self.min_Fiis_DY_CAGR)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_48)

        self.max_Fiis_DY_CAGR = QLineEdit(self.frame_82)
        self.max_Fiis_DY_CAGR.setObjectName(u"max_Fiis_DY_CAGR")
        self.max_Fiis_DY_CAGR.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_101.addWidget(self.max_Fiis_DY_CAGR)


        self.horizontalLayout_100.addWidget(self.frame_82)


        self.verticalLayout_22.addWidget(self.fFiis_DY_CAGR)

        self.fFiis_Dividendo = QFrame(self.InformationFrame_7)
        self.fFiis_Dividendo.setObjectName(u"fFiis_Dividendo")
        self.fFiis_Dividendo.setFrameShape(QFrame.StyledPanel)
        self.fFiis_Dividendo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.fFiis_Dividendo)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(30, 0, -1, 0)
        self.label_67 = QLabel(self.fFiis_Dividendo)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(185, 0))
        self.label_67.setMaximumSize(QSize(185, 150))
        self.label_67.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_67.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_104.addWidget(self.label_67)

        self.frame_86 = QFrame(self.fFiis_Dividendo)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(35, 0, 50, 0)
        self.min_Fiis_Dividendo = QLineEdit(self.frame_86)
        self.min_Fiis_Dividendo.setObjectName(u"min_Fiis_Dividendo")
        self.min_Fiis_Dividendo.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_105.addWidget(self.min_Fiis_Dividendo)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_50)

        self.max_Fiis_Dividendo = QLineEdit(self.frame_86)
        self.max_Fiis_Dividendo.setObjectName(u"max_Fiis_Dividendo")
        self.max_Fiis_Dividendo.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_105.addWidget(self.max_Fiis_Dividendo)


        self.horizontalLayout_104.addWidget(self.frame_86)


        self.verticalLayout_22.addWidget(self.fFiis_Dividendo)

        self.fFiis_CAGR = QFrame(self.InformationFrame_7)
        self.fFiis_CAGR.setObjectName(u"fFiis_CAGR")
        self.fFiis_CAGR.setFrameShape(QFrame.StyledPanel)
        self.fFiis_CAGR.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.fFiis_CAGR)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(30, 0, -1, 0)
        self.label_70 = QLabel(self.fFiis_CAGR)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(185, 0))
        self.label_70.setMaximumSize(QSize(185, 150))
        self.label_70.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_70.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_106.addWidget(self.label_70)

        self.frame_88 = QFrame(self.fFiis_CAGR)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_107.setSpacing(0)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(35, 0, 50, 0)
        self.min_Fiis_CAGR = QLineEdit(self.frame_88)
        self.min_Fiis_CAGR.setObjectName(u"min_Fiis_CAGR")
        self.min_Fiis_CAGR.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_107.addWidget(self.min_Fiis_CAGR)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_51)

        self.max_Fiis_CAGR = QLineEdit(self.frame_88)
        self.max_Fiis_CAGR.setObjectName(u"max_Fiis_CAGR")
        self.max_Fiis_CAGR.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_107.addWidget(self.max_Fiis_CAGR)


        self.horizontalLayout_106.addWidget(self.frame_88)


        self.verticalLayout_22.addWidget(self.fFiis_CAGR)

        self.fFiis_Liquidez = QFrame(self.InformationFrame_7)
        self.fFiis_Liquidez.setObjectName(u"fFiis_Liquidez")
        self.fFiis_Liquidez.setFrameShape(QFrame.StyledPanel)
        self.fFiis_Liquidez.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.fFiis_Liquidez)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(30, 0, -1, 0)
        self.label_79 = QLabel(self.fFiis_Liquidez)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(185, 0))
        self.label_79.setMaximumSize(QSize(185, 150))
        self.label_79.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_79.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_124.addWidget(self.label_79)

        self.frame_106 = QFrame(self.fFiis_Liquidez)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(35, 0, 50, 0)
        self.min_Fiis_Liquidez = QLineEdit(self.frame_106)
        self.min_Fiis_Liquidez.setObjectName(u"min_Fiis_Liquidez")
        self.min_Fiis_Liquidez.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_125.addWidget(self.min_Fiis_Liquidez)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_125.addItem(self.horizontalSpacer_60)

        self.max_Fiis_Liquidez = QLineEdit(self.frame_106)
        self.max_Fiis_Liquidez.setObjectName(u"max_Fiis_Liquidez")
        self.max_Fiis_Liquidez.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_125.addWidget(self.max_Fiis_Liquidez)


        self.horizontalLayout_124.addWidget(self.frame_106)


        self.verticalLayout_22.addWidget(self.fFiis_Liquidez)

        self.fFiis_Cotas = QFrame(self.InformationFrame_7)
        self.fFiis_Cotas.setObjectName(u"fFiis_Cotas")
        self.fFiis_Cotas.setFrameShape(QFrame.StyledPanel)
        self.fFiis_Cotas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.fFiis_Cotas)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(30, 0, -1, 0)
        self.label_60 = QLabel(self.fFiis_Cotas)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(185, 0))
        self.label_60.setMaximumSize(QSize(185, 150))
        self.label_60.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_60.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_96.addWidget(self.label_60)

        self.frame_78 = QFrame(self.fFiis_Cotas)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(35, 0, 50, 0)
        self.min_Fiis_Cotas = QLineEdit(self.frame_78)
        self.min_Fiis_Cotas.setObjectName(u"min_Fiis_Cotas")
        self.min_Fiis_Cotas.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_97.addWidget(self.min_Fiis_Cotas)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_46)

        self.max_Fiis_Cotas = QLineEdit(self.frame_78)
        self.max_Fiis_Cotas.setObjectName(u"max_Fiis_Cotas")
        self.max_Fiis_Cotas.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_97.addWidget(self.max_Fiis_Cotas)


        self.horizontalLayout_96.addWidget(self.frame_78)


        self.verticalLayout_22.addWidget(self.fFiis_Cotas)

        self.fFiis_Valor = QFrame(self.InformationFrame_7)
        self.fFiis_Valor.setObjectName(u"fFiis_Valor")
        self.fFiis_Valor.setFrameShape(QFrame.StyledPanel)
        self.fFiis_Valor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.fFiis_Valor)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(30, 0, -1, 0)
        self.label_81 = QLabel(self.fFiis_Valor)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(185, 0))
        self.label_81.setMaximumSize(QSize(185, 150))
        self.label_81.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_81.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_128.addWidget(self.label_81)

        self.frame_110 = QFrame(self.fFiis_Valor)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_129.setSpacing(0)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(35, 0, 50, 0)
        self.min_Fiis_Valor = QLineEdit(self.frame_110)
        self.min_Fiis_Valor.setObjectName(u"min_Fiis_Valor")
        self.min_Fiis_Valor.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_129.addWidget(self.min_Fiis_Valor)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_129.addItem(self.horizontalSpacer_62)

        self.max_Fiis_Valor = QLineEdit(self.frame_110)
        self.max_Fiis_Valor.setObjectName(u"max_Fiis_Valor")
        self.max_Fiis_Valor.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_129.addWidget(self.max_Fiis_Valor)


        self.horizontalLayout_128.addWidget(self.frame_110)


        self.verticalLayout_22.addWidget(self.fFiis_Valor)

        self.verticalSpacer_13 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacer_13)


        self.verticalLayout_21.addWidget(self.InformationFrame_7)

        self.ButtonFrame_7 = QFrame(self.frame_18)
        self.ButtonFrame_7.setObjectName(u"ButtonFrame_7")
        self.ButtonFrame_7.setMaximumSize(QSize(16777215, 80))
        self.ButtonFrame_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:1, stop:0.2746 rgba(217, 217, 217, 255), stop:0.287185 rgba(175, 175, 175, 255));\n"
"padding-top:8px;\n"
"\n"
"")
        self.ButtonFrame_7.setFrameShape(QFrame.NoFrame)
        self.ButtonFrame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.ButtonFrame_7)
        self.horizontalLayout_130.setSpacing(0)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_130.addItem(self.horizontalSpacer_63)

        self.fiisFilters = QPushButton(self.ButtonFrame_7)
        self.fiisFilters.setObjectName(u"fiisFilters")
        self.fiisFilters.setMinimumSize(QSize(185, 50))
        self.fiisFilters.setMaximumSize(QSize(185, 50))
        self.fiisFilters.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(69, 118, 178);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 22pt \"Arial\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"    background-color:rgb(98, 168, 254);\n"
"}")

        self.horizontalLayout_130.addWidget(self.fiisFilters)

        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_130.addItem(self.horizontalSpacer_64)


        self.verticalLayout_21.addWidget(self.ButtonFrame_7)


        self.horizontalLayout_10.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.fiisFiltersPage)
        self.endPage = QWidget()
        self.endPage.setObjectName(u"endPage")
        self.horizontalLayout_110 = QHBoxLayout(self.endPage)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.frame_12 = QFrame(self.endPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(600, 300))
        self.frame_12.setMaximumSize(QSize(600, 300))
        self.frame_12.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, 0)
        self.frame_21 = QFrame(self.frame_12)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 90))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_71 = QLabel(self.frame_21)
        self.label_71.setObjectName(u"label_71")
        font8 = QFont()
        font8.setPointSize(25)
        font8.setBold(True)
        self.label_71.setFont(font8)
        self.label_71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.label_71)


        self.verticalLayout_17.addWidget(self.frame_21)

        self.verticalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_16)

        self.InformationFrame_5 = QFrame(self.frame_12)
        self.InformationFrame_5.setObjectName(u"InformationFrame_5")
        self.InformationFrame_5.setFrameShape(QFrame.StyledPanel)
        self.InformationFrame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.InformationFrame_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_17 = QLabel(self.InformationFrame_5)
        self.label_17.setObjectName(u"label_17")
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(11)
        font9.setBold(False)
        font9.setItalic(False)
        self.label_17.setFont(font9)
        self.label_17.setStyleSheet(u"")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_17)


        self.verticalLayout_17.addWidget(self.InformationFrame_5)

        self.verticalSpacer_14 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_14)

        self.ButtonFrame_5 = QFrame(self.frame_12)
        self.ButtonFrame_5.setObjectName(u"ButtonFrame_5")
        self.ButtonFrame_5.setMaximumSize(QSize(16777215, 80))
        self.ButtonFrame_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:1, stop:0.2746 rgba(217, 217, 217, 255), stop:0.287185 rgba(175, 175, 175, 255));\n"
"padding-top:8px;\n"
"\n"
"")
        self.ButtonFrame_5.setFrameShape(QFrame.NoFrame)
        self.ButtonFrame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.ButtonFrame_5)
        self.horizontalLayout_109.setSpacing(0)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_109.addItem(self.horizontalSpacer_13)

        self.end = QPushButton(self.ButtonFrame_5)
        self.end.setObjectName(u"end")
        self.end.setMinimumSize(QSize(185, 50))
        self.end.setMaximumSize(QSize(185, 50))
        self.end.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(69, 118, 178);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 22pt \"Arial\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 3px solid rgba(0, 170, 255, 0.71);\n"
"    background-color:rgb(98, 168, 254);\n"
"}")

        self.horizontalLayout_109.addWidget(self.end)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_109.addItem(self.horizontalSpacer_49)


        self.verticalLayout_17.addWidget(self.ButtonFrame_5)


        self.horizontalLayout_110.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.endPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame_3 = QFrame(Widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgba(50, 50, 50, 150);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Market Analysis and Filtering", None))
        self.label_error.setText(QCoreApplication.translate("Widget", u"Preencha todos os campos!", None))
        self.pushButton_close.setText(QCoreApplication.translate("Widget", u"X", None))
        self.label_64.setText(QCoreApplication.translate("Widget", u"Bem Vindo!", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"Qual investimento voc\u00ea deseja analisar?", None))
        self.acoes.setText(QCoreApplication.translate("Widget", u"A\u00e7\u00f5es", None))
        self.fiis.setText(QCoreApplication.translate("Widget", u"FII's", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt;\">Voc\u00ea deseja usar filtros autom\u00e1ticos?</span></p></body></html>", None))
        self.yes.setText(QCoreApplication.translate("Widget", u"Sim", None))
        self.no.setText(QCoreApplication.translate("Widget", u"N\u00e3o", None))
        self.label_72.setText(QCoreApplication.translate("Widget", u"Qual o caminho da pasta de downloads?", None))
        self.path.setPlaceholderText(QCoreApplication.translate("Widget", u"D:\\User", None))
        self.NextWelcome.setText(QCoreApplication.translate("Widget", u"Seguinte", None))
        self.label_65.setText(QCoreApplication.translate("Widget", u"Quais indicadores voc\u00ea deseja analisar?", None))
        self.DY.setText(QCoreApplication.translate("Widget", u"DY", None))
        self.PL.setText(QCoreApplication.translate("Widget", u"P/L", None))
        self.PVP.setText(QCoreApplication.translate("Widget", u"P/VP", None))
        self.MargemEbit.setText(QCoreApplication.translate("Widget", u"Margem EBIT", None))
        self.Margem.setText(QCoreApplication.translate("Widget", u"Margem L\u00edquida", None))
        self.P_EBIT.setText(QCoreApplication.translate("Widget", u"P/EBIT", None))
        self.Divida_Pat.setText(QCoreApplication.translate("Widget", u"D\u00edvida/Patrim\u00f4nio", None))
        self.P_Cap.setText(QCoreApplication.translate("Widget", u"P/Cap. Giro", None))
        self.ROE.setText(QCoreApplication.translate("Widget", u"ROE", None))
        self.ROA.setText(QCoreApplication.translate("Widget", u"ROA", None))
        self.ROIC.setText(QCoreApplication.translate("Widget", u"ROIC", None))
        self.PatAti.setText(QCoreApplication.translate("Widget", u"Patrim\u00f4nio/Ativos", None))
        self.PasAti.setText(QCoreApplication.translate("Widget", u"Passivos/Ativos", None))
        self.CAGRR.setText(QCoreApplication.translate("Widget", u"CAGR Receita (5 anos)", None))
        self.CAGRL.setText(QCoreApplication.translate("Widget", u"CAGR Lucro (5 anos)", None))
        self.Liquidez.setText(QCoreApplication.translate("Widget", u"Liquidez Di\u00e1ria", None))
        self.PEG.setText(QCoreApplication.translate("Widget", u"PEG Ratio", None))
        self.Valor.setText(QCoreApplication.translate("Widget", u"Valor de Mercado", None))
        self.stocksOptions.setText(QCoreApplication.translate("Widget", u"Seguinte", None))
        self.label_68.setText(QCoreApplication.translate("Widget", u"Filtros", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"M\u00ednimo", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"M\u00e1ximo", None))
        self.label_24.setText(QCoreApplication.translate("Widget", u"DY", None))
        self.label_42.setText(QCoreApplication.translate("Widget", u"P/L", None))
        self.label_43.setText(QCoreApplication.translate("Widget", u"P/VP", None))
        self.label_45.setText(QCoreApplication.translate("Widget", u"Margem EBIT", None))
        self.label_58.setText(QCoreApplication.translate("Widget", u"Margem L\u00edquida", None))
        self.label_44.setText(QCoreApplication.translate("Widget", u"P/EBIT", None))
        self.label_46.setText(QCoreApplication.translate("Widget", u"D\u00edvida/Patrim\u00f4nio", None))
        self.label_49.setText(QCoreApplication.translate("Widget", u"P/Cap. Giro", None))
        self.label_48.setText(QCoreApplication.translate("Widget", u"ROE", None))
        self.label_47.setText(QCoreApplication.translate("Widget", u"ROA", None))
        self.label_51.setText(QCoreApplication.translate("Widget", u"ROIC", None))
        self.label_50.setText(QCoreApplication.translate("Widget", u"Patrim\u00f4nio/Ativos", None))
        self.label_52.setText(QCoreApplication.translate("Widget", u"Passivos/Ativos", None))
        self.label_54.setText(QCoreApplication.translate("Widget", u"CAGR Receita (5 anos)", None))
        self.label_53.setText(QCoreApplication.translate("Widget", u"CAGR Lucro (5 anos)", None))
        self.label_57.setText(QCoreApplication.translate("Widget", u"Liquidez Di\u00e1ria", None))
        self.label_56.setText(QCoreApplication.translate("Widget", u"PEG Ratio", None))
        self.label_55.setText(QCoreApplication.translate("Widget", u"Valor de Mercado", None))
        self.stocksFilters.setText(QCoreApplication.translate("Widget", u"Seguinte", None))
        self.label_66.setText(QCoreApplication.translate("Widget", u"Quais indicadores voc\u00ea deseja analisar?", None))
        self.Fiis_DY.setText(QCoreApplication.translate("Widget", u"DY", None))
        self.Fiis_DY_CAGR.setText(QCoreApplication.translate("Widget", u"DY CAGR 3 Anos", None))
        self.Fiis_PVP.setText(QCoreApplication.translate("Widget", u"P/VP", None))
        self.Fiis_Liquidez.setText(QCoreApplication.translate("Widget", u"Liquidez Di\u00e1ria", None))
        self.Fiis_Cotas.setText(QCoreApplication.translate("Widget", u"Cotas", None))
        self.Fiis_Dividendo.setText(QCoreApplication.translate("Widget", u"Dividendo", None))
        self.Fiis_CAGR.setText(QCoreApplication.translate("Widget", u"CAGR (3 Anos)", None))
        self.Fiis_Valor.setText(QCoreApplication.translate("Widget", u"Valor Patrimonial", None))
        self.fiisOptions.setText(QCoreApplication.translate("Widget", u"Seguinte", None))
        self.label_69.setText(QCoreApplication.translate("Widget", u"Filtros", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"M\u00ednimo", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"M\u00e1ximo", None))
        self.fDY_2.setText(QCoreApplication.translate("Widget", u"DY", None))
        self.label_61.setText(QCoreApplication.translate("Widget", u"P/VP", None))
        self.label_62.setText(QCoreApplication.translate("Widget", u"DY CAGR 3 Anos", None))
        self.label_67.setText(QCoreApplication.translate("Widget", u"\u00daltimo Dividendo", None))
        self.label_70.setText(QCoreApplication.translate("Widget", u"CAGR (3 Anos)", None))
        self.label_79.setText(QCoreApplication.translate("Widget", u"Liquidez Di\u00e1ria", None))
        self.label_60.setText(QCoreApplication.translate("Widget", u"N\u00famero de Cotas", None))
        self.label_81.setText(QCoreApplication.translate("Widget", u"Valor Patrimonial", None))
        self.fiisFilters.setText(QCoreApplication.translate("Widget", u"Seguinte", None))
        self.label_71.setText(QCoreApplication.translate("Widget", u"Planilha Atualizada com Sucesso!!", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"Uma planilha atualizada e filtrada estar\u00e1 salva na mesma pasta que o c\u00f3digo!", None))
        self.end.setText(QCoreApplication.translate("Widget", u"In\u00edcio", None))
        self.label.setText(QCoreApplication.translate("Widget", u"developed by Jucelio Tavares Junior", None))
    # retranslateUi

