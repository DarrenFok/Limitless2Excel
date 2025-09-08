from dataclasses import dataclass

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QLineEdit, QLabel, \
    QMessageBox, QFileDialog
from PySide6.QtCore import Qt, QUrl, Signal
from app_ui import Ui_mainWindow
from limitless2excel import convert
from pathlib import Path

import sys, html

@dataclass
class AppState:
    link_text: str = ""
    save_path: str = ""

class StartPage:
    def __init__(self,  root: QWidget):
        self.root = root
        self.confirmButton: QPushButton = root.findChild(QPushButton, "confirmButton")
        self.linkField: QLineEdit = root.findChild(QLineEdit, "linkField")

    def get_link(self) -> str:
        if self.linkField:
            return self.linkField.text().strip()  # remove any trailing whitespace
        else:
            return "".strip()

    # signal connection helpers
    def on_next(self, slot):
        if self.confirmButton:
            self.confirmButton.clicked.connect(slot)

class DirectorySelectPage:
    def __init__(self, root: QWidget):
        self.root = root
        self.browseButton: QPushButton = root.findChild(QPushButton, "browseButton")
        self.cancelButton: QPushButton = root.findChild(QPushButton, "cancelButton")
        self.linkHyperEdit: QLabel = root.findChild(QLabel, "confirmLabel")

    def set_link_preview(self, text: str):
        if not self.linkHyperEdit:  # check for label
            return

        url = QUrl.fromLocalFile(text.strip())
        if url.isValid and not url.isEmpty():
            self.linkHyperEdit.setTextFormat(Qt.TextFormat.RichText)
            self.linkHyperEdit.setOpenExternalLinks(True)
            display = html.escape(url.toDisplayString())

            # remove formatting
            if display.startswith("file:"):
                display = display.replace("file:", "")

            href = url.toString(QUrl.ComponentFormattingOption.FullyEncoded)
            self.linkHyperEdit.setText(f'<a href="{href}" style="color:white;" >{html.escape(display)}</a>')
        else:
            self.linkHyperEdit.setText(f'<i>(No valid link provided)<i>')

    def set_save_path(self, path: str):
        if self.directoryEdit:
            self.directoryEdit.setText(path)

    # signal connection helpers
    def on_next(self, slot):
        if self.browseButton:
            self.browseButton.clicked.connect(slot)

    def on_back(self, slot):
        if self.cancelButton:
            self.cancelButton.clicked.connect(slot)

class ConfirmationPage:
    def __init__(self, root: QWidget):
        self.root = root
        self.closeProgramButton: QPushButton = root.findChild(QPushButton, "closeProgramButton")
        self.createAnotherButton: QPushButton = root.findChild(QPushButton, "createAnotherButton")
        self.directoryEdit: QLabel = root.findChild(QLabel, "directoryEdit")

    def set_directory_preview(self, text: str):
        if self.directoryEdit:
            self.directoryEdit.setText(text)

    # signal confirmation helpers
    def on_next(self, slot):
        if self.createAnotherButton:
            self.createAnotherButton.clicked.connect(slot)

    def on_close(self, slot):
        if self.closeProgramButton:
            self.closeProgramButton.clicked.connect(slot)

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.state = AppState()

        self.setMinimumSize(750, 400)
        self.setMaximumSize(750, 400)

        self.page0 = StartPage(self.startPage)
        self.page1 = DirectorySelectPage(self.directorySelectPage)
        self.page2 = ConfirmationPage(self.confirmationPage)

        # connect buttons
        self.page0.on_next(self._start_to_directory)
        self.page1.on_next(self._directory_to_confirmation)
        self.page1.on_back(lambda: self.stackedWidget.setCurrentWidget(self.startPage))
        self.page2.on_next(lambda: self.stackedWidget.setCurrentWidget(self.startPage))
        self.page2.on_close(self.close)

        self.stackedWidget.setCurrentWidget(self.startPage)

        # assign custom title bar button actions
        self.titleBar.findChild(QPushButton, "closeButton").clicked.connect(self.close)
        self.titleBar.findChild(QPushButton, "minimizeButton").clicked.connect(self.showMinimized)

        # assign drag and drop capabilities for custom title bar
        self.titleBar.mousePressEvent = self.title_bar_mouse_press
        self.titleBar.mouseMoveEvent = self.title_bar_mouse_move
        self.titleBar.mouseReleaseEvent = self.title_bar_mouse_release

        self._old_pos = None

    def title_bar_mouse_press(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._old_pos = event.globalPosition().toPoint()

    def title_bar_mouse_move(self, event):
        if self._old_pos is not None:
            delta = event.globalPosition().toPoint() - self._old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self._old_pos = event.globalPosition().toPoint()

    def title_bar_mouse_release(self, event):
        self._old_pos = None

    # transition handling functions
    def _start_to_directory(self):
        txt = self.page0.get_link()
        # check for empty link box
        if not txt:
            QMessageBox.warning(self, "Warning", "No link provided")
            return

        # check for link validity
        if not txt.startswith("https://limitlesstcg.com/decks/list/"):
            QMessageBox.warning(self, "Warning", "Link provided is not supported")
            return

        self.state.link_text = txt
        self.page1.set_link_preview(txt)
        self.stackedWidget.setCurrentWidget(self.directorySelectPage)

    def _directory_to_confirmation(self):
        # pop up dialog window
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save as", "output.xlsx", "Excel Workbook (*.xlsx);;All Files (*)"
        )
        if filename:
            if not filename.lower().endswith(".xlsx"):
                filename += ".xlsx"
            self.state.save_path = filename
        else:
            return
        deck_name = Path(filename).stem
        convert(self.state.link_text, deck_name)  # call conversion function from limitless2excel.py

        self.state.save_path = filename
        self.page2.set_directory_preview(self.state.save_path)
        self.stackedWidget.setCurrentWidget(self.confirmationPage)

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(771, 341)
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()