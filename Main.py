import base64
import os
import pickle
import secrets
import sys

from PIL import Image
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from tinyec import registry
import SafeEC
from GUI import Ui_MainWindow
from mailer import mail
KEY_FILE = 'secret.key'
DEC_FILE = 'dec.jpg'


class MainApp:
    def __init__(self):
        self.img_path = None
        self.privKey = None
        self.pubKey = None
        self.curve = None

        self.init_ui()

    def init_ui(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

    def init_listeners(self):
        self.ui.pushButtonUploadPlain.clicked.connect(self.upload_plain_image)
        self.ui.pushButtonUploadEnc.clicked.connect(self.upload_enc_image)
        self.ui.pushButtonEncrypt.clicked.connect(self.encrypt_file)
        self.ui.pushButtonDecrypt.clicked.connect(self.decrypt_file)

    def upload_plain_image(self):
        dlg = QFileDialog()
        if dlg.exec_():
            path = dlg.selectedFiles()[0]
            self.img_path = path
            self.ui.lineEditPlainImgPath.setText(path)

            image = Image.open(path)
            image.show()

    def upload_enc_image(self):
        dlg = QFileDialog()
        if dlg.exec_():
            path = dlg.selectedFiles()[0]
            self.img_path = path
            self.ui.lineEditEncImgPath.setText(path)

    def init_curve(self):
        self.curve = registry.get_curve('brainpoolP256r1')

        if os.path.exists(KEY_FILE):
            key_file = open(KEY_FILE, 'rb')
            keys = pickle.load(key_file)
            self.pubKey = keys[0]
            self.privKey = keys[1]
        else:

            self.privKey = secrets.randbelow(self.curve.field.n)
            self.pubKey = self.privKey * self.curve.g

            keys = [self.pubKey, self.privKey]
            key_file = open(KEY_FILE, 'wb')
            pickle.dump(keys, key_file)

    def encrypt_file(self):
        if self.img_path:
            with open(self.img_path, "rb") as image_file:

                encoded_string = base64.b64encode(image_file.read())

                self.init_curve()

                encryptedMsg = SafeEC.encrypt_ECC(self.curve, encoded_string, self.pubKey)

                enc_file = open('encrypted.dat', 'wb')
                pickle.dump(encryptedMsg, enc_file)
                self.show_message("Encrypted")

                file_name=os.path.basename(self.img_path)
                s_mail=self.ui.lineEditUsername.text()
                s_pwd=self.ui.lineEditPassword.text()
                r_mail = self.ui.lineEditMail.text()
                mail(r_mail,file_name,s_mail,s_pwd)


        else:
            self.show_error("No file selected!")

    def decrypt_file(self):
        if self.img_path:
            with open(self.img_path, "rb") as image_file:
                # unpickler = pickle.Unpickler(image_file)
                # encryptedMsg = unpickler.load()
                encryptedMsg = pickle.load(image_file)
                self.init_curve()

                decryptedMsg = SafeEC.decrypt_ECC(encryptedMsg, self.privKey)

                dec_file = open(DEC_FILE, 'wb')
                dec_file.write(base64.b64decode(decryptedMsg))
                dec_file.flush()
                dec_file.close()

                image = Image.open(DEC_FILE)
                image.show()

                self.show_error("Decrypted")

        else:
            self.show_error("No file selected!")

    def show_error(self, msg):
        print(msg)
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(msg)

    def show_message(self, msg):
        print(msg)
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(msg)

    def start(self):
        self.ui.setupUi(self.MainWindow)
        self.init_listeners()
        self.MainWindow.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    main_app = MainApp()
    main_app.start()
