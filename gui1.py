# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 766)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mplwindow = QtWidgets.QWidget(self.centralwidget)
        self.mplwindow.setObjectName("mplwindow")
        self.processLabel = QtWidgets.QLabel(self.mplwindow)
        self.processLabel.setGeometry(QtCore.QRect(160, 20, 421, 50))
        self.processLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.processLabel.setAutoFillBackground(True)
        self.processLabel.setText("")
        self.processLabel.setObjectName("processLabel")
        self.plotWidget = QtWidgets.QWidget(self.mplwindow)
        self.plotWidget.setGeometry(QtCore.QRect(50, 70, 500, 550))
        self.plotWidget.setMinimumSize(QtCore.QSize(500, 550))
        self.plotWidget.setMaximumSize(QtCore.QSize(600, 500))
        self.plotWidget.setObjectName("plotWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.plotWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imageDisplay = QtWidgets.QLabel(self.plotWidget)
        self.imageDisplay.setMaximumSize(QtCore.QSize(350, 400))
        self.imageDisplay.setText("")
        self.imageDisplay.setObjectName("imageDisplay")
        self.horizontalLayout_2.addWidget(self.imageDisplay)
        self.groupBox_2 = QtWidgets.QGroupBox(self.mplwindow)
        self.groupBox_2.setGeometry(QtCore.QRect(570, 100, 100, 526))
        self.groupBox_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.imageSizeVerticalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.imageSizeVerticalSlider.setMinimumSize(QtCore.QSize(0, 350))
        self.imageSizeVerticalSlider.setMaximumSize(QtCore.QSize(16777215, 300))
        self.imageSizeVerticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.imageSizeVerticalSlider.setObjectName("imageSizeVerticalSlider")
        self.verticalLayout_2.addWidget(self.imageSizeVerticalSlider)
        self.resizingLabel = QtWidgets.QLabel(self.groupBox_2)
        self.resizingLabel.setMinimumSize(QtCore.QSize(0, 100))
        self.resizingLabel.setText("")
        self.resizingLabel.setObjectName("resizingLabel")
        self.verticalLayout_2.addWidget(self.resizingLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.mplwindow)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.operationComboBox = QtWidgets.QComboBox(self.groupBox)
        self.operationComboBox.setObjectName("operationComboBox")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.verticalLayout_4.addWidget(self.operationComboBox)
        self.audioBrowseButton = QtWidgets.QPushButton(self.groupBox)
        self.audioBrowseButton.setObjectName("audioBrowseButton")
        self.verticalLayout_4.addWidget(self.audioBrowseButton)
        self.imageBrowseButton = QtWidgets.QPushButton(self.groupBox)
        self.imageBrowseButton.setObjectName("imageBrowseButton")
        self.verticalLayout_4.addWidget(self.imageBrowseButton)
        self.audioAnalysisComboBox = QtWidgets.QComboBox(self.groupBox)
        self.audioAnalysisComboBox.setObjectName("audioAnalysisComboBox")
        self.audioAnalysisComboBox.addItem("")
        self.audioAnalysisComboBox.addItem("")
        self.audioAnalysisComboBox.addItem("")
        self.audioAnalysisComboBox.addItem("")
        self.audioAnalysisComboBox.addItem("")
        self.verticalLayout_4.addWidget(self.audioAnalysisComboBox)
        self.grayScaleButton = QtWidgets.QPushButton(self.groupBox)
        self.grayScaleButton.setObjectName("grayScaleButton")
        self.verticalLayout_4.addWidget(self.grayScaleButton)
        self.imageProcessingComboBox = QtWidgets.QComboBox(self.groupBox)
        self.imageProcessingComboBox.setObjectName("imageProcessingComboBox")
        self.imageProcessingComboBox.addItem("")
        self.imageProcessingComboBox.addItem("")
        self.imageProcessingComboBox.addItem("")
        self.imageProcessingComboBox.addItem("")
        self.verticalLayout_4.addWidget(self.imageProcessingComboBox)
        self.basicGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.basicGroupBox.setObjectName("basicGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.basicGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.brightnessHorizontalSlider = QtWidgets.QSlider(self.basicGroupBox)
        self.brightnessHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessHorizontalSlider.setObjectName("brightnessHorizontalSlider")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.brightnessHorizontalSlider)
        self.brightnessLabel = QtWidgets.QLabel(self.basicGroupBox)
        self.brightnessLabel.setObjectName("brightnessLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.brightnessLabel)
        self.filteringLabel = QtWidgets.QLabel(self.basicGroupBox)
        self.filteringLabel.setObjectName("filteringLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.filteringLabel)
        self.filteringHorizontalSlider = QtWidgets.QSlider(self.basicGroupBox)
        self.filteringHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.filteringHorizontalSlider.setObjectName("filteringHorizontalSlider")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.filteringHorizontalSlider)
        self.inversionHorizontalSlider = QtWidgets.QSlider(self.basicGroupBox)
        self.inversionHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.inversionHorizontalSlider.setObjectName("inversionHorizontalSlider")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inversionHorizontalSlider)
        self.inversionLabel = QtWidgets.QLabel(self.basicGroupBox)
        self.inversionLabel.setObjectName("inversionLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.inversionLabel)
        self.verticalLayout_4.addWidget(self.basicGroupBox)
        self.interGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.interGroupBox.setObjectName("interGroupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.interGroupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.equalizationLabel = QtWidgets.QLabel(self.interGroupBox)
        self.equalizationLabel.setObjectName("equalizationLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.equalizationLabel)
        self.equalizationHorizontalSlider = QtWidgets.QSlider(self.interGroupBox)
        self.equalizationHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.equalizationHorizontalSlider.setObjectName("equalizationHorizontalSlider")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.equalizationHorizontalSlider)
        self.noiseReductionLabel = QtWidgets.QLabel(self.interGroupBox)
        self.noiseReductionLabel.setObjectName("noiseReductionLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.noiseReductionLabel)
        self.noiseReductionhorizontalSlider = QtWidgets.QSlider(self.interGroupBox)
        self.noiseReductionhorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.noiseReductionhorizontalSlider.setObjectName("noiseReductionhorizontalSlider")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.noiseReductionhorizontalSlider)
        self.enhancementLabel = QtWidgets.QLabel(self.interGroupBox)
        self.enhancementLabel.setObjectName("enhancementLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.enhancementLabel)
        self.enhancementHorizontalSlider = QtWidgets.QSlider(self.interGroupBox)
        self.enhancementHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.enhancementHorizontalSlider.setObjectName("enhancementHorizontalSlider")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.enhancementHorizontalSlider)
        self.verticalLayout_4.addWidget(self.interGroupBox)
        self.advancedGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.advancedGroupBox.setObjectName("advancedGroupBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.advancedGroupBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.thresholdingLabel = QtWidgets.QLabel(self.advancedGroupBox)
        self.thresholdingLabel.setObjectName("thresholdingLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.thresholdingLabel)
        self.thresholdingHorizontalSlider = QtWidgets.QSlider(self.advancedGroupBox)
        self.thresholdingHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.thresholdingHorizontalSlider.setObjectName("thresholdingHorizontalSlider")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.thresholdingHorizontalSlider)
        self.segmentationLabel = QtWidgets.QLabel(self.advancedGroupBox)
        self.segmentationLabel.setObjectName("segmentationLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.segmentationLabel)
        self.segmentationHorizontalSlider = QtWidgets.QSlider(self.advancedGroupBox)
        self.segmentationHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.segmentationHorizontalSlider.setObjectName("segmentationHorizontalSlider")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.segmentationHorizontalSlider)
        self.featureDetectionLabel = QtWidgets.QLabel(self.advancedGroupBox)
        self.featureDetectionLabel.setObjectName("featureDetectionLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.featureDetectionLabel)
        self.horizontalSlider_7 = QtWidgets.QSlider(self.advancedGroupBox)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_7)
        self.verticalLayout_4.addWidget(self.advancedGroupBox)
        self.resetImageButton = QtWidgets.QPushButton(self.groupBox)
        self.resetImageButton.setObjectName("resetImageButton")
        self.verticalLayout_4.addWidget(self.resetImageButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1002, 27))
        self.menubar.setObjectName("menubar")
        self.menuMyDawApp = QtWidgets.QMenu(self.menubar)
        self.menuMyDawApp.setObjectName("menuMyDawApp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMyDawApp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Parameters"))
        self.operationComboBox.setItemText(0, _translate("MainWindow", "--Operation--"))
        self.operationComboBox.setItemText(1, _translate("MainWindow", "Audio Processing"))
        self.operationComboBox.setItemText(2, _translate("MainWindow", "Image Processing"))
        self.audioBrowseButton.setText(_translate("MainWindow", "Upload Audio"))
        self.imageBrowseButton.setText(_translate("MainWindow", "Upload Image"))
        self.audioAnalysisComboBox.setItemText(0, _translate("MainWindow", "--Analysis--"))
        self.audioAnalysisComboBox.setItemText(1, _translate("MainWindow", "Waveform"))
        self.audioAnalysisComboBox.setItemText(2, _translate("MainWindow", "Time Domain - FFT"))
        self.audioAnalysisComboBox.setItemText(3, _translate("MainWindow", "Freq - Magnitude"))
        self.audioAnalysisComboBox.setItemText(4, _translate("MainWindow", "Freq - Phase"))
        self.grayScaleButton.setText(_translate("MainWindow", "GrayScale"))
        self.imageProcessingComboBox.setItemText(0, _translate("MainWindow", "--Image Processing--"))
        self.imageProcessingComboBox.setItemText(1, _translate("MainWindow", "Basic"))
        self.imageProcessingComboBox.setItemText(2, _translate("MainWindow", "Intermediate"))
        self.imageProcessingComboBox.setItemText(3, _translate("MainWindow", "Advanced"))
        self.basicGroupBox.setTitle(_translate("MainWindow", "Basic Operations"))
        self.brightnessLabel.setText(_translate("MainWindow", "brightness"))
        self.filteringLabel.setText(_translate("MainWindow", "Filtering"))
        self.inversionLabel.setText(_translate("MainWindow", "Inversion"))
        self.interGroupBox.setTitle(_translate("MainWindow", "Intermediate Operations"))
        self.equalizationLabel.setText(_translate("MainWindow", "Equalization"))
        self.noiseReductionLabel.setText(_translate("MainWindow", "N.Reduction"))
        self.enhancementLabel.setText(_translate("MainWindow", "Enhancement"))
        self.advancedGroupBox.setTitle(_translate("MainWindow", "Advanced Operations"))
        self.thresholdingLabel.setText(_translate("MainWindow", "Thresholding"))
        self.segmentationLabel.setText(_translate("MainWindow", "Segmentation"))
        self.featureDetectionLabel.setText(_translate("MainWindow", "Detection"))
        self.resetImageButton.setText(_translate("MainWindow", "reset"))
        self.menuMyDawApp.setTitle(_translate("MainWindow", "MyDawApp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
