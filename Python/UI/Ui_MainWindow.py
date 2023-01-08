# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from pyqtgraph import GraphicsLayoutWidget
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 916)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(
            7, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MesaurementSettingsBox = QGroupBox(self.centralwidget)
        self.MesaurementSettingsBox.setObjectName("MesaurementSettingsBox")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MesaurementSettingsBox.sizePolicy().hasHeightForWidth()
        )
        self.MesaurementSettingsBox.setSizePolicy(sizePolicy)
        self.MesaurementSettingsBox.setMinimumSize(QSize(242, 150))
        self.MesaurementSettingsBox.setFlat(False)
        self.MesaurementSettingsBox.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.MesaurementSettingsBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 6, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.label = QLabel(self.MesaurementSettingsBox)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(
            5, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.InputSerialPort = QLabel(self.MesaurementSettingsBox)
        self.InputSerialPort.setObjectName("InputSerialPort")

        self.horizontalLayout.addWidget(self.InputSerialPort)

        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setLabelAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.formLayout.setFormAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, -1, -1, -1)
        self.InputChgSerialPort = QPushButton(self.MesaurementSettingsBox)
        self.InputChgSerialPort.setObjectName("InputChgSerialPort")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.InputChgSerialPort)

        self.label_2 = QLabel(self.MesaurementSettingsBox)
        self.label_2.setObjectName("label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.InputNumChannels = QSpinBox(self.MesaurementSettingsBox)
        self.InputNumChannels.setObjectName("InputNumChannels")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.InputNumChannels)

        self.label_3 = QLabel(self.MesaurementSettingsBox)
        self.label_3.setObjectName("label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.InputSamplingRate = QSpinBox(self.MesaurementSettingsBox)
        self.InputSamplingRate.setObjectName("InputSamplingRate")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.InputSamplingRate)

        self.label_5 = QLabel(self.MesaurementSettingsBox)
        self.label_5.setObjectName("label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.InputDisplayDuration = QSpinBox(self.MesaurementSettingsBox)
        self.InputDisplayDuration.setObjectName("InputDisplayDuration")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.InputDisplayDuration)

        self.gridLayout_3.addLayout(self.formLayout, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.MesaurementSettingsBox)

        self.Measurement = QGroupBox(self.centralwidget)
        self.Measurement.setObjectName("Measurement")
        sizePolicy.setHeightForWidth(self.Measurement.sizePolicy().hasHeightForWidth())
        self.Measurement.setSizePolicy(sizePolicy)
        self.Measurement.setMinimumSize(QSize(271, 60))
        self.horizontalLayout_4 = QHBoxLayout(self.Measurement)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 0, 6, 0)
        self.InputMeasureStop = QPushButton(self.Measurement)
        self.InputMeasureStop.setObjectName("InputMeasureStop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.InputMeasureStop.sizePolicy().hasHeightForWidth()
        )
        self.InputMeasureStop.setSizePolicy(sizePolicy1)
        self.InputMeasureStop.setMinimumSize(QSize(30, 10))

        self.horizontalLayout_4.addWidget(self.InputMeasureStop)

        self.InputMeasureStart = QPushButton(self.Measurement)
        self.InputMeasureStart.setObjectName("InputMeasureStart")
        sizePolicy1.setHeightForWidth(
            self.InputMeasureStart.sizePolicy().hasHeightForWidth()
        )
        self.InputMeasureStart.setSizePolicy(sizePolicy1)
        self.InputMeasureStart.setMinimumSize(QSize(30, 10))
        self.InputMeasureStart.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.InputMeasureStart)

        self.verticalLayout.addWidget(self.Measurement)

        self.RecordSettings = QGroupBox(self.centralwidget)
        self.RecordSettings.setObjectName("RecordSettings")
        sizePolicy.setHeightForWidth(
            self.RecordSettings.sizePolicy().hasHeightForWidth()
        )
        self.RecordSettings.setSizePolicy(sizePolicy)
        self.RecordSettings.setMinimumSize(QSize(0, 90))
        self.RecordSettings.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_2 = QGridLayout(self.RecordSettings)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(6, 0, 6, 0)
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.formLayout_7.setLabelAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.formLayout_7.setFormAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.formLayout_7.setVerticalSpacing(0)
        self.formLayout_7.setContentsMargins(0, -1, 0, -1)
        self.label_4 = QLabel(self.RecordSettings)
        self.label_4.setObjectName("label_4")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.InputRecordInterval = QSpinBox(self.RecordSettings)
        self.InputRecordInterval.setObjectName("InputRecordInterval")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.InputRecordInterval)

        self.label_16 = QLabel(self.RecordSettings)
        self.label_16.setObjectName("label_16")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.InputSaveDirPath = QLabel(self.RecordSettings)
        self.InputSaveDirPath.setObjectName("InputSaveDirPath")
        self.InputSaveDirPath.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.InputSaveDirPath)

        self.InputChgSaveFolder = QPushButton(self.RecordSettings)
        self.InputChgSaveFolder.setObjectName("InputChgSaveFolder")
        sizePolicy1.setHeightForWidth(
            self.InputChgSaveFolder.sizePolicy().hasHeightForWidth()
        )
        self.InputChgSaveFolder.setSizePolicy(sizePolicy1)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.InputChgSaveFolder)

        self.gridLayout_2.addLayout(self.formLayout_7, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.RecordSettings)

        self.Record = QGroupBox(self.centralwidget)
        self.Record.setObjectName("Record")
        sizePolicy.setHeightForWidth(self.Record.sizePolicy().hasHeightForWidth())
        self.Record.setSizePolicy(sizePolicy)
        self.Record.setMinimumSize(QSize(271, 150))
        self.verticalLayout_4 = QVBoxLayout(self.Record)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.InputRecordStart = QPushButton(self.Record)
        self.InputRecordStart.setObjectName("InputRecordStart")
        sizePolicy1.setHeightForWidth(
            self.InputRecordStart.sizePolicy().hasHeightForWidth()
        )
        self.InputRecordStart.setSizePolicy(sizePolicy1)
        self.InputRecordStart.setMinimumSize(QSize(30, 10))
        self.InputRecordStart.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.InputRecordStart)

        self.InputRecordStop = QPushButton(self.Record)
        self.InputRecordStop.setObjectName("InputRecordStop")
        sizePolicy1.setHeightForWidth(
            self.InputRecordStop.sizePolicy().hasHeightForWidth()
        )
        self.InputRecordStop.setSizePolicy(sizePolicy1)
        self.InputRecordStop.setMinimumSize(QSize(30, 10))
        self.InputRecordStop.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.InputRecordStop)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_3.setLabelAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.formLayout_3.setFormAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(0)
        self.formLayout_3.setContentsMargins(0, -1, 0, 0)
        self.InputSaveDir = QLabel(self.Record)
        self.InputSaveDir.setObjectName("InputSaveDir")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.InputSaveDir.sizePolicy().hasHeightForWidth()
        )
        self.InputSaveDir.setSizePolicy(sizePolicy2)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.InputSaveDir)

        self.label_6 = QLabel(self.Record)
        self.label_6.setObjectName("label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.InputElapsedTime = QLabel(self.Record)
        self.InputElapsedTime.setObjectName("InputElapsedTime")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.InputElapsedTime)

        self.label_7 = QLabel(self.Record)
        self.label_7.setObjectName("label_7")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.InputNumSamples = QLabel(self.Record)
        self.InputNumSamples.setObjectName("InputNumSamples")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.InputNumSamples)

        self.label_8 = QLabel(self.Record)
        self.label_8.setObjectName("label_8")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.InputFolderSize = QLabel(self.Record)
        self.InputFolderSize.setObjectName("InputFolderSize")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.InputFolderSize)

        self.label_9 = QLabel(self.Record)
        self.label_9.setObjectName("label_9")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.InputOpenFolder = QPushButton(self.Record)
        self.InputOpenFolder.setObjectName("InputOpenFolder")
        sizePolicy1.setHeightForWidth(
            self.InputOpenFolder.sizePolicy().hasHeightForWidth()
        )
        self.InputOpenFolder.setSizePolicy(sizePolicy1)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.InputOpenFolder)

        self.verticalLayout_4.addLayout(self.formLayout_3)

        self.verticalLayout.addWidget(self.Record)

        self.NoteBox = QGroupBox(self.centralwidget)
        self.NoteBox.setObjectName("NoteBox")
        sizePolicy.setHeightForWidth(self.NoteBox.sizePolicy().hasHeightForWidth())
        self.NoteBox.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.NoteBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(6, 0, 6, 0)
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.formLayout_4.setLabelAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.formLayout_4.setFormAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.formLayout_4.setVerticalSpacing(0)
        self.label_11 = QLabel(self.NoteBox)
        self.label_11.setObjectName("label_11")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.InputPlace = QLineEdit(self.NoteBox)
        self.InputPlace.setObjectName("InputPlace")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.InputPlace)

        self.label_12 = QLabel(self.NoteBox)
        self.label_12.setObjectName("label_12")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.InputTemperature = QDoubleSpinBox(self.NoteBox)
        self.InputTemperature.setObjectName("InputTemperature")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.InputTemperature)

        self.label_13 = QLabel(self.NoteBox)
        self.label_13.setObjectName("label_13")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.InputHumidity = QSpinBox(self.NoteBox)
        self.InputHumidity.setObjectName("InputHumidity")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.InputHumidity)

        self.gridLayout_4.addLayout(self.formLayout_4, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QLabel(self.NoteBox)
        self.label_15.setObjectName("label_15")

        self.verticalLayout_3.addWidget(self.label_15)

        self.InputNote = QPlainTextEdit(self.NoteBox)
        self.InputNote.setObjectName("InputNote")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(50)
        sizePolicy4.setHeightForWidth(self.InputNote.sizePolicy().hasHeightForWidth())
        self.InputNote.setSizePolicy(sizePolicy4)
        self.InputNote.setMinimumSize(QSize(0, 25))

        self.verticalLayout_3.addWidget(self.InputNote)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.gridLayout_4.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_14 = QLabel(self.NoteBox)
        self.label_14.setObjectName("label_14")

        self.verticalLayout_2.addWidget(self.label_14)

        self.InputPurpose = QPlainTextEdit(self.NoteBox)
        self.InputPurpose.setObjectName("InputPurpose")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.InputPurpose.sizePolicy().hasHeightForWidth()
        )
        self.InputPurpose.setSizePolicy(sizePolicy5)
        self.InputPurpose.setMinimumSize(QSize(0, 25))
        self.InputPurpose.setMaximumSize(QSize(16777215, 50))
        self.InputPurpose.setTabStopWidth(80)

        self.verticalLayout_2.addWidget(self.InputPurpose)

        self.gridLayout_4.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QLabel(self.NoteBox)
        self.label_10.setObjectName("label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.InputPlant = QLineEdit(self.NoteBox)
        self.InputPlant.setObjectName("InputPlant")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.InputPlant.sizePolicy().hasHeightForWidth())
        self.InputPlant.setSizePolicy(sizePolicy6)

        self.horizontalLayout_2.addWidget(self.InputPlant)

        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.NoteBox)

        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.GraphicsLayoutWidget = GraphicsLayoutWidget(self.centralwidget)
        self.GraphicsLayoutWidget.setObjectName("GraphicsLayoutWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.GraphicsLayoutWidget.sizePolicy().hasHeightForWidth()
        )
        self.GraphicsLayoutWidget.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.GraphicsLayoutWidget, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            7, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1086, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.MesaurementSettingsBox.setTitle(
            QCoreApplication.translate("MainWindow", "Measurement Settings", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "serial port", None)
        )
        self.InputSerialPort.setText("")
        self.InputChgSerialPort.setText(
            QCoreApplication.translate("MainWindow", "show ports", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "number of channels", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "sampting rate [Hz]", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "display duration [s]", None)
        )
        self.Measurement.setTitle(
            QCoreApplication.translate("MainWindow", "Measurement", None)
        )
        self.InputMeasureStop.setText(
            QCoreApplication.translate("MainWindow", "stop", None)
        )
        self.InputMeasureStart.setText(
            QCoreApplication.translate("MainWindow", "start", None)
        )
        self.RecordSettings.setTitle(
            QCoreApplication.translate("MainWindow", "Record Settings", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", "record interval [s]    ", None)
        )
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "save path", None)
        )
        self.InputSaveDirPath.setText("")
        self.InputChgSaveFolder.setText(
            QCoreApplication.translate("MainWindow", "change folder", None)
        )
        self.Record.setTitle(QCoreApplication.translate("MainWindow", "Record", None))
        self.InputRecordStart.setText(
            QCoreApplication.translate("MainWindow", "start", None)
        )
        self.InputRecordStop.setText(
            QCoreApplication.translate("MainWindow", "stop", None)
        )
        self.InputSaveDir.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", "start", None))
        self.InputElapsedTime.setText("")
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", "elapsed time", None)
        )
        self.InputNumSamples.setText("")
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", "nubmer of samples", None)
        )
        self.InputFolderSize.setText("")
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", "folder size", None)
        )
        self.InputOpenFolder.setText(
            QCoreApplication.translate("MainWindow", "open folder", None)
        )
        self.NoteBox.setTitle(QCoreApplication.translate("MainWindow", "Note", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", "place", None))
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", "temperature [\u2103]", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", "humidity", None)
        )
        self.label_15.setText(QCoreApplication.translate("MainWindow", "note", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", "purpose", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", "plant", None))

    # retranslateUi
