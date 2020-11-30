# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "BlackJack.ui"
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "BlackJack.ui"
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from copy import deepcopy
from random import shuffle

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = {"Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = int(value)


class ListWidgetItem(QtWidgets.QListWidgetItem):
    def __lt__(self, other):
        if int(self.text().split(" ")[2]) == int(other.text().split(" ")[2]):
            return self.text().lower() < other.text().lower()
        else:
            return int(self.text().split(" ")[2]) > int(other.text().split(" ")[2])


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 800)
        MainWindow.setStyleSheet("background-color: green;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.player_hand_label = QtWidgets.QLabel(self.centralwidget)
        self.player_hand_label.setGeometry(QtCore.QRect(280, 689, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.player_hand_label.setFont(font)
        self.player_hand_label.setStyleSheet("color: white")
        self.player_hand_label.setObjectName("player_hand_label")
        self.dealer_hand_label = QtWidgets.QLabel(self.centralwidget)
        self.dealer_hand_label.setGeometry(QtCore.QRect(280, 10, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dealer_hand_label.setFont(font)
        self.dealer_hand_label.setStyleSheet("color: white")
        self.dealer_hand_label.setObjectName("dealer_hand_label")
        self.hit_button = QtWidgets.QPushButton(self.centralwidget)
        self.hit_button.setGeometry(QtCore.QRect(60, 660, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hit_button.setFont(font)
        self.hit_button.setStyleSheet("background-color: white")
        self.hit_button.setObjectName("hit_button")
        self.stand_button = QtWidgets.QPushButton(self.centralwidget)
        self.stand_button.setGeometry(QtCore.QRect(60, 700, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stand_button.setFont(font)
        self.stand_button.setStyleSheet("background-color: white")
        self.stand_button.setObjectName("stand_button")
        self.player_value = QtWidgets.QLabel(self.centralwidget)
        self.player_value.setGeometry(QtCore.QRect(400, 689, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.player_value.setFont(font)
        self.player_value.setStyleSheet("color: white")
        self.player_value.setText("")
        self.player_value.setObjectName("player_value")
        self.dealer_value = QtWidgets.QLabel(self.centralwidget)
        self.dealer_value.setGeometry(QtCore.QRect(390, 10, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dealer_value.setFont(font)
        self.dealer_value.setStyleSheet("color: white")
        self.dealer_value.setText("")
        self.dealer_value.setObjectName("dealer_value")
        self.top_list = QtWidgets.QListWidget(self.centralwidget)
        self.top_list.setGeometry(QtCore.QRect(10, 160, 181, 451))
        self.top_list.setStyleSheet("background-color: white")
        self.top_list.setObjectName("top_list")
        self.top_list_label = QtWidgets.QLabel(self.centralwidget)
        self.top_list_label.setGeometry(QtCore.QRect(10, 125, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.top_list_label.setFont(font)
        self.top_list_label.setStyleSheet("color: white")
        self.top_list_label.setObjectName("top_list_label")
        self.name_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(10, 40, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_edit.setFont(font)
        self.name_edit.setStyleSheet("background-color: white")
        self.name_edit.setObjectName("name_edit")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(10, 10, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: white")
        self.name_label.setObjectName("name_label")
        self.name_save_button = QtWidgets.QPushButton(self.centralwidget)
        self.name_save_button.setGeometry(QtCore.QRect(40, 80, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_save_button.setFont(font)
        self.name_save_button.setStyleSheet("background-color: white")
        self.name_save_button.setObjectName("name_save_button")
        self.winning_streak_label = QtWidgets.QLabel(self.centralwidget)
        self.winning_streak_label.setGeometry(QtCore.QRect(679, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.winning_streak_label.setFont(font)
        self.winning_streak_label.setStyleSheet("color: white")
        self.winning_streak_label.setObjectName("winning_streak_label")
        self.winning_streak = QtWidgets.QLabel(self.centralwidget)
        self.winning_streak.setGeometry(QtCore.QRect(830, 10, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.winning_streak.setFont(font)
        self.winning_streak.setStyleSheet("color: white")
        self.winning_streak.setObjectName("winning_streak")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.loaded_deck = self.load_deck()
        self.top_winners = self.load_top_list()
        self.name_save_button.clicked.connect(self.save_name)
        self.winning_streak.setText("0")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BlackJack"))
        self.player_hand_label.setText(_translate("MainWindow", "Játékos lapjai:"))
        self.dealer_hand_label.setText(_translate("MainWindow", "Osztó lapjai:"))
        self.hit_button.setText(_translate("MainWindow", "Hit"))
        self.stand_button.setText(_translate("MainWindow", "Stand"))
        self.top_list_label.setText(_translate("MainWindow", "Ranglista"))
        self.name_label.setText(_translate("MainWindow", "Adja meg a nevét:"))
        self.name_save_button.setText(_translate("MainWindow", "Mentés"))
        self.winning_streak_label.setText(_translate("MainWindow", "Győzelmi széria:"))

    def save_name(self):
        name_input = self.name_edit.toPlainText()
        self.name_label.setText("Játékos: " + name_input)
        self.name_label.move(10, 50)
        self.name_save_button.hide()
        self.name_edit.hide()
        self.hit_button.clicked.connect(self.player_hit)
        self.stand_button.clicked.connect(self.player_stand)
        self.start_game()

    def start_game(self):
        self.winner = None
        self.player_hand = []
        self.player_value.setText("0")
        self.dealer_hand = []
        self.dealer_value.setText("0")
        self.deck = deepcopy(self.loaded_deck)
        shuffle(self.deck)
        self.deal_cards()

    def restart_game(self):
        for i in range(len(self.player_hand)):
            card = self.centralwidget.findChild(QtWidgets.QLabel, "player_card_" + str(i))
            card.setParent(None)

        for i in range(len(self.dealer_hand)):
            card = self.centralwidget.findChild(QtWidgets.QLabel, "dealer_card_" + str(i))
            card.setParent(None)

        self.start_game()

    def player_hit(self):
        if not self.winner:
            if int(self.player_value.text()) > 21:
                self.check_winner()
                return

            new_card = self.deck.pop()
            self.player_hand.append(new_card)
            new_player_card = QtWidgets.QLabel(self.centralwidget)
            new_player_card.setGeometry(QtCore.QRect(250 + len(self.player_hand) * 50, 420, 170, 250))
            new_player_card.setObjectName("player_card_" + str(len(self.player_hand) - 1))
            new_player_card.setPixmap(QtGui.QPixmap("./cards/{}.png".format(new_card.name)))
            new_player_card.show()
            self.player_value.setText(str(int(self.player_value.text()) + new_card.value))

            if int(self.player_value.text()) > 21:
                if self.has_ace("player"):
                    self.player_value.setText(str(int(self.player_value.text()) - 10))
                else:
                    self.check_winner()
        else:
            self.check_winner()

    def player_stand(self):
        if not self.winner:
            show_card = self.dealer_hand[1]
            show_dealer_card = QtWidgets.QLabel(self.centralwidget)
            show_dealer_card.setGeometry(QtCore.QRect(250 + 2 * 50, 60, 170, 250))
            show_dealer_card.setObjectName("dealer_card_" + str(len(self.dealer_hand) - 1))
            show_dealer_card.setPixmap(QtGui.QPixmap("./cards/{}.png".format(show_card.name)))
            show_dealer_card.show()
            self.dealer_value.setText(str(int(self.dealer_value.text()) + show_card.value))

            if int(self.dealer_value.text()) > 21:
                if self.has_ace("dealer"):
                    self.dealer_value.setText(str(int(self.dealer_value.text()) - 10))

            if int(self.dealer_value.text()) >= 17:
                self.dealer_stand()
            else:
                self.dealer_hit(False)
        else:
            self.check_winner()

    def dealer_hit(self, auto):
        new_card = self.deck.pop()
        self.dealer_hand.append(new_card)
        new_dealer_card = QtWidgets.QLabel(self.centralwidget)
        new_dealer_card.setGeometry(QtCore.QRect(250 + len(self.dealer_hand) * 50, 60, 170, 250))
        new_dealer_card.setObjectName("dealer_card_" + str(len(self.dealer_hand) - 1))

        if len(self.dealer_hand) == 2:
            new_dealer_card.setPixmap(QtGui.QPixmap("./cards/Back.png"))
        else:
            new_dealer_card.setPixmap(QtGui.QPixmap("./cards/{}.png".format(new_card.name)))
            self.dealer_value.setText(str(int(self.dealer_value.text()) + new_card.value))

        new_dealer_card.show()

        if not auto:
            if int(self.dealer_value.text()) >= 17:
                self.dealer_stand()
            else:
                self.dealer_hit(False)

    def dealer_stand(self):
        self.check_winner()

    def deal_cards(self):
        self.player_hit()
        self.player_hit()

        self.dealer_hit(True)
        self.dealer_hit(True)

    def create_dialog(self, winner):
        new_dialog = QtWidgets.QDialog(self.centralwidget)
        new_dialog.setGeometry(QtCore.QRect(800, 500, 150, 100))
        new_dialog.setWindowTitle("Vége")
        result = QtWidgets.QLabel(new_dialog)
        if winner != "draw":
            result.setText("A(z) {} nyert!".format(winner))
        else:
            result.setText("Döntetlen!")

        result.move(30, 20)
        new_dialog.setModal(True)
        new_dialog.setStyleSheet("background-color: white")

        restart_button = QtWidgets.QPushButton(new_dialog)
        restart_button.move(30, 50)
        restart_button.setText("Új játszma")
        restart_button.clicked.connect(self.restart_game)
        restart_button.clicked.connect(lambda x: new_dialog.hide())
        new_dialog.show()

    def check_winner(self):
        player_value = int(self.player_value.text())
        dealer_value = int(self.dealer_value.text())

        if (dealer_value > 21 and player_value <= 21) or (dealer_value < player_value <= 21):
            self.winning_streak.setText(str(int(self.winning_streak.text()) + 1))
            player_name = self.name_label.text().split(" ")[1]
            self.check_top_list((player_name, self.winning_streak.text()))
            self.winner = "játékos"
            self.create_dialog("játékos")
        elif player_value > 21 or (player_value < dealer_value <= 21):
            self.winning_streak.setText("0")
            self.winner = "osztó"
            self.create_dialog("osztó")
        elif player_value == dealer_value:
            self.winner = "döntetlen"
            self.create_dialog("draw")

    def has_ace(self, player):
        if player == "player":
            for card in self.player_hand:
                if card.value == 11:
                    card.value = 1
                    return True

            return False
        else:
            for card in self.dealer_hand:
                if card.value == 11:
                    card.value = 1
                    return True

            return False

    def load_deck(self):
        deck = []
        for rank in ranks:
            for suit in suits:
                if rank in values.keys():
                    value = values[rank]
                else:
                    value = rank

                card = Card("{} of {}".format(rank, suit), value)
                deck.append(card)

        return deck

    def load_top_list(self):
        f = open("toplist.txt", "r", encoding="utf-8")

        for row in f:
            row = row.strip()
            top_list_item = ListWidgetItem(row)
            self.top_list.addItem(top_list_item)

        f.close()
        self.top_list.sortItems()

    def check_top_list(self, player):
        found = False
        for i in range(len(self.top_list)):
            item = self.top_list.item(i)
            item_data = item.text().split(" ")
            if item_data[0] == player[0]:
                found = True
                if item_data[2] < player[1]:
                    item.setText("{} győzelmei: {}".format(player[0], player[1]))

        if not found:
            top_list_item = ListWidgetItem("{} győzelmei: {}".format(player[0], player[1]))
            self.top_list.addItem(top_list_item)

        self.top_list.sortItems()
        self.top_list.reset()


def save_top_list():
    f = open("toplist.txt", "w", encoding='utf-8')
    for i in range(len(ui.top_list)):
        item = ui.top_list.item(i)
        f.write(item.text() + '\n')

    f.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(save_top_list)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
