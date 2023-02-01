# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtGui, QtWidgets
import os
from PySide6.QtGui import QFont, QIcon,QColor,QKeySequence,QSyntaxHighlighter,QTextCharFormat,QTextCursor
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


QRegularExpression = QtCore.QRegularExpression
Qt = QtCore.Qt

class MyHighlighter(QSyntaxHighlighter):
    def highlightBlock(self, text):
        myClassFormat = QTextCharFormat()
        myClassFormat.setFontWeight(QFont.Bold)
        myClassFormat.setForeground(Qt.darkMagenta)
        expression = QRegularExpression("\\b(signed|union|struct|int|float|double|char|short|long|unsigned|void|bool)\\b")
        i = expression.globalMatch(text)
        while i.hasNext():
            match = i.next()
            self.setFormat(match.capturedStart(), match.capturedLength(), myClassFormat)
        myClassFormat = QTextCharFormat()
        myClassFormat.setFontWeight(QFont.Bold)
        myClassFormat.setForeground(Qt.blue)
        expression = QRegularExpression("\\b(class|for|while|do|return|static|volatile)\\b")
        i = expression.globalMatch(text)
        while i.hasNext():
            match = i.next()
            self.setFormat(match.capturedStart(), match.capturedLength(), myClassFormat)

        myClassFormat = QTextCharFormat()
        myClassFormat.setFontItalic(True)
        myClassFormat.setForeground(Qt.blue)
        expression = QRegularExpression("\\$\\(.+\\)")
        i = expression.globalMatch(text)
        while i.hasNext():
            match = i.next()
            self.setFormat(match.capturedStart(), match.capturedLength(), myClassFormat)


        multiLineCommentFormat = QTextCharFormat()
        multiLineCommentFormat.setForeground(Qt.red)
        startExpression = QRegularExpression("/\\*")
        s = startExpression.match(text)
        endExpression = QRegularExpression("\\*/")
        self.setCurrentBlockState(0)
        startIndex = -1
        if self.previousBlockState() != 1 and s.hasMatch():
            startIndex = s.capturedStart()
            print(startIndex)
        while startIndex >= 0:
            t = endExpression.match(text, startIndex)
            endIndex = t.capturedStart()
            print(startIndex - endIndex)
            commentLength = int()
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + t.capturedLength()
            self.setFormat(startIndex, commentLength, multiLineCommentFormat)
            if endIndex == -1:
                break
            else:
                s = startExpression.match(text, endIndex)
                startIndex = -1
                if s.hasMatch():
                    startIndex = s.capturedStart()



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print(type(self.ui.textEdit.document()))
        self.syntax_highlighter = MyHighlighter(self.ui.textEdit.document())
        self.mias_path="mias.exe"
        self.mico_path="mico.exe"
        self.mua_path="mua.exe"
        self.working_dir = os.getcwd()
        self.doLog(f"Working Dir = {self.working_dir}")


    def doLog(self, text):
        self.ui.textEdit_4.append(text)


    def resizeEvent(self, e):
        self.on_resize(int(e.size().width()), int(e.size().height() - 50))

    def on_resize(self, width, height):
        print(f"Resize central widget to ({width}, {height})")
        self.ui.verticalWidget_4.setFixedSize(width, height)

    def on_actionOpen_File(self):
        print("Open File.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
