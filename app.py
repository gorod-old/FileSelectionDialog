import os

from PyQt5.QtWidgets import QMainWindow, QFileDialog

import design
from MessagePack import print_info_msg


class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self, marker: str = ''):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setupUi(self)

        # ToolTips stylesheet
        self.setStyleSheet("""QToolTip {
                            border: 1px solid black;
                            padding: 3px;
                            border-radius: 3px;
                            opacity: 200;
                        }""")

        self.startButton.clicked.connect(self._start_click)
        self.selectDirButton.clicked.connect(self._select_dir_path)
        self.selectFileButton.clicked.connect(self._select_file_path)

    def _select_dir_path(self):
        path = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.lineEditDir.setText(path)
        print_info_msg(f'path: {path}')

    def _select_file_path(self):
        print(os.getcwd())
        path = QFileDialog.getOpenFileName(self, 'Выберите файл', os.getcwd())[0]
        self.lineEditFile.setText(path)
        print_info_msg(f'path: {path}')

    def _start_click(self):
        pass
