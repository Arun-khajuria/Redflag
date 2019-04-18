from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit
from PyQt5.QtWidgets import QMessageBox
import sys


class myapp(QtWidgets.QMainWindow):
    def __init__(self):  # connecting to buttons
        super(myapp, self).__init__()
        uic.loadUi('redflag.ui', self)
        self.button_ok_2.clicked.connect(self.ddos_)
        self.button_cancel_2.clicked.connect(self.ddos_cancel)
        self.button_ok.clicked.connect(self.sql)
        self.button_cancel.clicked.connect(self.sql_cancel)
        self.button_graph.clicked.connect(self.graph)

    def ddos_(self):  # calling the ddos funtion

        text = self.input_url_ddos.text()

        if text != "":
            import ddos
            exe = ddos.log(text, level=1)
            ddos.ip = text
            exe.exec_()

        else:
            QMessageBox.about(self, "Error", "Enter Url")

    def ddos_cancel(self):
        quit()

    def sql(self):  #
        text = self.input_url_sql.text()
        if text != "":
            import requests as req
            import sys
            file = open('data.txt', 'r')  # reading the data from file
            payload = file.read().splitlines()
            l = len(payload)

            for x in range(l):  # attcking the address
                y = payload[x]
                resp = req.request(method='get', url=text, params=y)
                if resp.status_code == 200:
                    print("found it Url: %s" % resp.url)
                    #import pylab as plb
                    #plb.figure(1)
                    #gaus_dist = plb.normal(-2,2, size=z)

                    #plb.hist(gaus_dist, normed=True, bins=24, color="red")

                    #plb.title("Gaussian distribution/Histogram")
                    #plb.xlabel("value")
                    #plb.ylabel("frequency")
                    #plb.grid(True)
                    #plb.pause(10)
                    #plb.show()
                    exit()
                else:
                    print("trying man")
        else:
            QMessageBox.about(self, "Error", "Enter Url")

    def sql_cancel(self):
        quit()

    def graph(self):
        import pylab as plb
        plb.figure(1)
        file = open('C:\\project\\UI\\data.txt', 'r')  # reading the data from file
        payload = file.read()
        l = len(payload)
        gaus_dist = plb.normal(-2, 2, size=l)

        plb.hist(gaus_dist, normed=True, bins=24, color="red")

        plb.title("Gaussian distribution/Histogram")
        plb.xlabel("value")
        plb.ylabel("frequency")
        plb.grid(True)
        plb.show()


if __name__ == '__main__':  # calling the application to show
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = myapp()
    window.show()
    sys.exit(app.exec_())
