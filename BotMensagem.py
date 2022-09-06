import pyautogui as auto
import time
import pyperclip
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDesktopWidget

class Teste(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        QMessageBox.about(self, "Aviso", '''
        Atenção, Logue no seu WhatsApp Web antes de usar o app.
        Lembre-se de definir sua mensagem e seus contatos para usar o app.
        ''')
        self.contato=[]
        self.texto=[]
        self.botao= QtWidgets.QPushButton(self)
        self.label= QtWidgets.QLabel(self)
        self.botaoA= QtWidgets.QPushButton(self)
        self.botaoE = QtWidgets.QPushButton(self)
        self.labelEdit = QtWidgets.QLabel(self)
        self.line = QtWidgets.QLineEdit(self)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.botao.setText('Confirmar')
        self.botaoA.setText('Enviar')
        self.botaoE.setText('Edit')
        self.label.setText('Contatos:')
        self.labelEdit.setText('Editar Msg:')
        self.botao.clicked.connect(self.clickCallback)
        self.botaoA.clicked.connect(self.mandarMensagem)
        self.botaoE.clicked.connect(self.editarMensagem)
        self.botao.move(160,0)
        self.label.move(5,0)
        self.line.move(60,0)
        self.botaoA.move(160,30)
        self.lineEdit.move(60,60)
        self.labelEdit.move(5,60)
        self.botaoE.move(160,60)
        self.setWindowTitle('Mandar mensagens')
        self.setGeometry(0,250,250,250)



    def localizacao(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())



    def clickCallback(self):
        self.contato.append(self.line.text())
        self.line.clear()
        QMessageBox.about(self, "Aviso",'Contato Adicionado com sucesso')

    def editarMensagem(self):
        self.texto.append(self.lineEdit.text())
        self.lineEdit.clear()
        print(self.texto)
        QMessageBox.about(self, "Aviso", 'Mensagem salva com sucesso.')


    def mandarMensagem(self):
        if self.texto and self.contato:
            auto.PAUSE=1
            auto.hotkey("win")
            auto.write("opera")
            auto.press("enter")
            time.sleep(2)
            auto.hotkey("ctrl", "t")
            pyperclip.copy("https://web.whatsapp.com")
            auto.hotkey("ctrl", "v")
            auto.press("enter")
            time.sleep(7)
            for nome in self.contato:
                auto.click(x=361, y=96)
                pyperclip.copy(nome)
                auto.hotkey("ctrl", "v")
                auto.click(x=181, y=325)
                auto.click(x=1258, y=693)
                for mensagem in self.texto:
                    pyperclip.copy(mensagem)
                auto.hotkey("ctrl", "v")
                auto.press("enter")
            # print(auto.position())

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    test = Teste()
    test.localizacao()
    test.show()
    sys.exit(app.exec_())

