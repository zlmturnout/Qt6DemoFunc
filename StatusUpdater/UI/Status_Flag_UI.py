# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Status_Flag_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(895, 607)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Time_step_input = QLineEdit(Form)
        self.Time_step_input.setObjectName(u"Time_step_input")
        self.Time_step_input.setMinimumSize(QSize(80, 50))
        self.Time_step_input.setMaximumSize(QSize(80, 50))
        font = QFont()
        font.setFamilies([u"Cambria Math"])
        font.setPointSize(18)
        self.Time_step_input.setFont(font)
        self.Time_step_input.setInputMethodHints(Qt.ImhPreferNumbers)
        self.Time_step_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Time_step_input)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/icons/icons/Status_green50px.png"))

        self.horizontalLayout.addWidget(self.label)

        self.Start_plot_btn = QPushButton(Form)
        self.Start_plot_btn.setObjectName(u"Start_plot_btn")
        self.Start_plot_btn.setMinimumSize(QSize(120, 50))
        self.Start_plot_btn.setMaximumSize(QSize(120, 50))
        palette = QPalette()
        brush = QBrush(QColor(41, 152, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.Start_plot_btn.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.Start_plot_btn.setFont(font2)
        icon = QIcon()
        icon.addFile(u"Status_green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start_plot_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.Start_plot_btn)

        self.Stop_plot_btn = QPushButton(Form)
        self.Stop_plot_btn.setObjectName(u"Stop_plot_btn")
        self.Stop_plot_btn.setMinimumSize(QSize(120, 50))
        self.Stop_plot_btn.setMaximumSize(QSize(120, 50))
        palette1 = QPalette()
        brush3 = QBrush(QColor(255, 84, 5, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.Stop_plot_btn.setPalette(palette1)
        self.Stop_plot_btn.setFont(font2)
        self.Stop_plot_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.Stop_plot_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        Form.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Time_step_input.setToolTip(QCoreApplication.translate("Form", u"10~1000ms", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Time_step_input.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.Time_step_input.setInputMask("")
        self.Time_step_input.setText(QCoreApplication.translate("Form", u"1000", None))
        self.Time_step_input.setPlaceholderText(QCoreApplication.translate("Form", u"ms", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ms", None))
        self.label.setText("")
        self.Start_plot_btn.setText(QCoreApplication.translate("Form", u"Start", None))
        self.Stop_plot_btn.setText(QCoreApplication.translate("Form", u"Stop", None))
    # retranslateUi

