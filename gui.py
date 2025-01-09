# gui.py

import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QFileDialog, QComboBox, QProgressBar,
    QVBoxLayout, QHBoxLayout, QMessageBox, QGroupBox,
    QGridLayout, QMenuBar, QAction, QTextEdit, QStyle, QSpacerItem,
    QSizePolicy
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QFont
from converter import batch_convert_heic, setup_logging
import logging
import multiprocessing


class ConverterThread(QThread):
    progress_update = pyqtSignal(int, int)

    def __init__(self, input_dir, output_dir, quality_value, output_fmt):
        super().__init__()
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.quality_value = quality_value
        self.output_fmt = output_fmt

    def run(self):
        def progress_callback(processed, total):
            self.progress_update.emit(processed, total)

        try:
            setup_logging()
            batch_convert_heic(
                self.input_dir,
                self.output_dir,
                self.quality_value,
                self.output_fmt,
                progress_callback
            )
        except Exception as e:
            logging.error(f"Exception: {e}", exc_info=True)
            self.progress_update.emit(-1, -1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("HEIC to Image Converter")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogListView))

        # Initialize UI components
        self.init_ui()

    def init_ui(self):
        # Central widget
        widget = QWidget()
        self.setCentralWidget(widget)

        # Main layout
        main_layout = QVBoxLayout()
        widget.setLayout(main_layout)

        # Menu Bar
        self.init_menu_bar()

        # Input Group
        input_group = QGroupBox("Select Directories")
        input_layout = QGridLayout()
        input_group.setLayout(input_layout)

        # Input Directory
        self.input_directory = QLineEdit()
        self.input_button = QPushButton("Browse")
        self.input_button.clicked.connect(self.browse_input)
        self.input_button.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        input_layout.addWidget(QLabel("Input Directory:"), 0, 0)
        input_layout.addWidget(self.input_directory, 0, 1)
        input_layout.addWidget(self.input_button, 0, 2)

        # Output Directory
        self.output_directory = QLineEdit()
        self.output_button = QPushButton("Browse")
        self.output_button.clicked.connect(self.browse_output)
        self.output_button.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        input_layout.addWidget(QLabel("Output Directory:"), 1, 0)
        input_layout.addWidget(self.output_directory, 1, 1)
        input_layout.addWidget(self.output_button, 1, 2)

        # Settings Group
        settings_group = QGroupBox("Settings")
        settings_layout = QGridLayout()
        settings_group.setLayout(settings_layout)

        # Quality
        self.quality_input = QLineEdit()
        self.quality_input.setFixedWidth(50)
        self.quality_input.setText("90")
        settings_layout.addWidget(QLabel("Quality (1-100):"), 0, 0)
        settings_layout.addWidget(self.quality_input, 0, 1)

        # Output Format
        self.format_combobox = QComboBox()
        self.format_combobox.addItems(["PNG", "JPG", "WEBP"])
        self.format_combobox.setCurrentIndex(0)
        self.format_combobox.setFixedWidth(100)
        settings_layout.addWidget(QLabel("Output Format:"), 1, 0)
        settings_layout.addWidget(self.format_combobox, 1, 1)

        # Spacer to align items to the left
        settings_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 2)

        # Convert Button
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_images)
        self.convert_button.setIcon(self.style().standardIcon(QStyle.SP_CommandLink))
        self.convert_button.setFixedHeight(40)
        convert_layout = QHBoxLayout()
        convert_layout.addStretch()
        convert_layout.addWidget(self.convert_button)
        convert_layout.addStretch()

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setFixedHeight(25)

        # Add widgets to main layout
        main_layout.addWidget(input_group)
        main_layout.addWidget(settings_group)
        main_layout.addLayout(convert_layout)
        main_layout.addWidget(self.progress_bar)

        # Apply Stylesheet
        self.apply_stylesheet()

    def init_menu_bar(self):
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu('File')

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Help Menu
        help_menu = menu_bar.addMenu('Help')

        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

        view_logs_action = QAction('View Logs', self)
        view_logs_action.triggered.connect(self.view_logs)
        help_menu.addAction(view_logs_action)

    def apply_stylesheet(self):
        # Apply a modern dark theme stylesheet
        style = """
        QWidget {
            background-color: #232629;
            color: #F0F0F0;
            font-family: Arial;
            font-size: 12px;
        }
        QGroupBox {
            font-weight: bold;
            border: 1px solid #4D4D4D;
            border-radius: 5px;
            margin-top: 10px;
        }
        QGroupBox:title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 3px;
        }
        QLabel {
            font-size: 12px;
        }
        QLineEdit, QComboBox {
            background-color: #2A2D32;
            border: 1px solid #4D4D4D;
            border-radius: 3px;
            padding: 2px;
        }
        QPushButton {
            background-color: #3A3F44;
            border: none;
            padding: 5px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #50565C;
        }
        QProgressBar {
            text-align: center;
            border: 1px solid #4D4D4D;
            border-radius: 5px;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            width: 20px;
        }
        QMenuBar {
            background-color: #2A2D32;
        }
        QMenuBar::item {
            spacing: 3px;
            padding: 1px 4px;
            background: transparent;
        }
        QMenuBar::item:selected {
            background: #3A3F44;
        }
        QMenu {
            background-color: #2A2D32;
            color: #F0F0F0;
        }
        QMenu::item:selected {
            background-color: #05B8CC;
        }
        """
        self.setStyleSheet(style)

    def browse_input(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Input Directory")
        if directory:
            self.input_directory.setText(directory)

    def browse_output(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if directory:
            self.output_directory.setText(directory)

    def convert_images(self):
        input_dir = self.input_directory.text()
        output_dir = self.output_directory.text()
        output_fmt = self.format_combobox.currentText().lower()

        try:
            quality_value = int(self.quality_input.text())
            if not 1 <= quality_value <= 100:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Quality must be an integer between 1 and 100.")
            return

        if not input_dir or not output_dir:
            QMessageBox.warning(self, "Input Error", "Please select both input and output directories.")
            return

        self.convert_button.setEnabled(False)
        self.progress_bar.setValue(0)

        # Start conversion in a separate thread
        self.thread = ConverterThread(input_dir, output_dir, quality_value, output_fmt)
        self.thread.progress_update.connect(self.update_progress)
        self.thread.finished.connect(self.conversion_finished)
        self.thread.start()

    def update_progress(self, processed, total):
        if processed == -1:
            QMessageBox.critical(self, "Error", "An error occurred during conversion. Check logs for details.")
            self.progress_bar.setValue(0)
            self.convert_button.setEnabled(True)
            return

        progress_value = int((processed / total) * 100)
        self.progress_bar.setValue(progress_value)
        QApplication.processEvents()

    def conversion_finished(self):
        self.progress_bar.setValue(100)
        QMessageBox.information(self, "Conversion Complete", "All files have been processed.")
        self.convert_button.setEnabled(True)

    def show_about(self):
        QMessageBox.information(self, "About", "HEIC to Image Converter by Verso Industries\nwww.versoindustries.com\nVersion 1.0")

    def view_logs(self):
        log_file = 'heic_converter.log'
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                logs = f.read()
            log_dialog = QDialog(self)
            log_dialog.setWindowTitle("Application Logs")
            log_dialog.setGeometry(150, 150, 600, 400)
            layout = QVBoxLayout()
            log_text = QTextEdit()
            log_text.setPlainText(logs)
            log_text.setReadOnly(True)
            layout.addWidget(log_text)
            log_dialog.setLayout(layout)
            log_dialog.exec_()
        else:
            QMessageBox.information(self, "Logs Not Found", "No logs have been generated yet.")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    setup_logging()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())