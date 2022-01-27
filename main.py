import threading

from PyQt5 import QtCore, QtWidgets
from main_dialog import Ui_Dialog
from app import App


class MainWindow(Ui_Dialog):
    def setupUi(self, dialog):
        super(MainWindow, self).setupUi(dialog)

        # 버튼 이벤트 연결
        self.pushButton.clicked.connect(self.startServer)

    def startServer(self):
        if not hasattr(self, 'thread'):
            self.thread = threading.Thread(target=self.startFlaskThread, daemon=True)
            self.thread.start()


    def startFlaskThread(self):
        name = self.lineEdit.text()
        stdNumber = self.lineEdit_2.text()
        stdDept = self.lineEdit_3.text()
        stdGrade = self.lineEdit_4.text()
        maxCredits = self.lineEdit_5.text()

        self.flask = App(import_name=__name__, name=name, stdNumber=stdNumber, stdDept=stdDept, grade=stdGrade, maxCredits=maxCredits)
        self.flask.run()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
