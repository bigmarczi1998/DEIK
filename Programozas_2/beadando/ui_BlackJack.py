# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BlackJackZnmCJp.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 800)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: green;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.player_hand_label = QLabel(self.centralwidget)
        self.player_hand_label.setObjectName(u"player_hand_label")
        self.player_hand_label.setGeometry(QRect(280, 689, 131, 31))
        self.player_hand_label.setFont(font)
        self.player_hand_label.setStyleSheet(u"color: white")
        self.dealer_hand_label = QLabel(self.centralwidget)
        self.dealer_hand_label.setObjectName(u"dealer_hand_label")
        self.dealer_hand_label.setGeometry(QRect(280, 10, 120, 31))
        self.dealer_hand_label.setFont(font)
        self.dealer_hand_label.setStyleSheet(u"color: white")
        self.hit_button = QPushButton(self.centralwidget)
        self.hit_button.setObjectName(u"hit_button")
        self.hit_button.setGeometry(QRect(60, 660, 75, 25))
        self.hit_button.setFont(font)
        self.hit_button.setStyleSheet(u"background-color: white")
        self.stand_button = QPushButton(self.centralwidget)
        self.stand_button.setObjectName(u"stand_button")
        self.stand_button.setGeometry(QRect(60, 700, 75, 25))
        self.stand_button.setFont(font)
        self.stand_button.setStyleSheet(u"background-color: white")
        self.player_value = QLabel(self.centralwidget)
        self.player_value.setObjectName(u"player_value")
        self.player_value.setGeometry(QRect(430, 689, 47, 31))
        self.player_value.setFont(font)
        self.player_value.setStyleSheet(u"color: white")
        self.dealer_value = QLabel(self.centralwidget)
        self.dealer_value.setObjectName(u"dealer_value")
        self.dealer_value.setGeometry(QRect(410, 10, 47, 31))
        self.dealer_value.setFont(font)
        self.dealer_value.setStyleSheet(u"color: white")
        self.top_list = QListWidget(self.centralwidget)
        self.top_list.setObjectName(u"top_list")
        self.top_list.setGeometry(QRect(10, 160, 181, 451))
        self.top_list.setStyleSheet(u"background-color: white")
        self.top_list_label = QLabel(self.centralwidget)
        self.top_list_label.setObjectName(u"top_list_label")
        self.top_list_label.setGeometry(QRect(10, 125, 81, 31))
        self.top_list_label.setFont(font)
        self.top_list_label.setStyleSheet(u"color: white")
        self.name_edit = QTextEdit(self.centralwidget)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setGeometry(QRect(10, 40, 151, 30))
        self.name_edit.setFont(font)
        self.name_edit.setStyleSheet(u"background-color: white")
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(10, 10, 171, 20))
        self.name_label.setFont(font)
        self.name_label.setStyleSheet(u"color: white")
        self.name_save_button = QPushButton(self.centralwidget)
        self.name_save_button.setObjectName(u"name_save_button")
        self.name_save_button.setGeometry(QRect(40, 80, 75, 25))
        self.name_save_button.setFont(font)
        self.name_save_button.setStyleSheet(u"background-color: white")
        self.winning_streak_label = QLabel(self.centralwidget)
        self.winning_streak_label.setObjectName(u"winning_streak_label")
        self.winning_streak_label.setGeometry(QRect(669, 10, 151, 31))
        self.winning_streak_label.setFont(font)
        self.winning_streak_label.setStyleSheet(u"color: white")
        self.winning_streak = QLabel(self.centralwidget)
        self.winning_streak.setObjectName(u"winning_streak")
        self.winning_streak.setGeometry(QRect(830, 10, 47, 31))
        self.winning_streak.setFont(font)
        self.winning_streak.setStyleSheet(u"color: white")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BlackJack", None))
        self.player_hand_label.setText(QCoreApplication.translate("MainWindow", u"J\u00e1t\u00e9kos lapjai:", None))
        self.dealer_hand_label.setText(QCoreApplication.translate("MainWindow", u"Oszt\u00f3 lapjai:", None))
        self.hit_button.setText(QCoreApplication.translate("MainWindow", u"Hit", None))
        self.stand_button.setText(QCoreApplication.translate("MainWindow", u"Stand", None))
        self.player_value.setText("")
        self.dealer_value.setText("")
        self.top_list_label.setText(QCoreApplication.translate("MainWindow", u"Ranglista", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Adja meg a nev\u00e9t:", None))
        self.name_save_button.setText(QCoreApplication.translate("MainWindow", u"Ment\u00e9s", None))
        self.winning_streak_label.setText(QCoreApplication.translate("MainWindow", u"Gy\u0151zelmi sz\u00e9ria:", None))
    # retranslateUi

