import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton, QLabel,QLineEdit
from MinecraftFunctions import Teleport, SetBlock, BlockOptions, SpawnMob, EntityOptions, PlaceMessage

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Panel Minecraft')
        
        self.tpInputX = QLineEdit(self)
        self.tpInputX.setPlaceholderText('Koordynat X')
        self.tpInputX.setMaximumWidth(100)
        self.tpInputY = QLineEdit(self)
        self.tpInputY.setPlaceholderText('Koordynat Y')
        self.tpInputY.setMaximumWidth(100)
        self.tpInputZ = QLineEdit(self)
        self.tpInputZ.setPlaceholderText('Koordynat Z')
        self.tpInputZ.setMaximumWidth(100)
        self.tpButton = QPushButton('Teleportuj', self)
        self.tpButton.clicked.connect(lambda: Teleport(self.tpInputX.text(),self.tpInputY.text(),self.tpInputZ.text()))
        
        self.mobSelect = QComboBox(self)
        self.mobSelect.addItems(EntityOptions)
        self.mobButton = QPushButton('Przywołaj moba/byt', self)
        self.mobButton.clicked.connect(lambda: SpawnMob(self.mobSelect.currentText()))
        
        self.blockSelect = QComboBox(self)
        self.blockSelect.addItems(BlockOptions)
        self.blockButton = QPushButton('Postaw blok', self)
        self.blockButton.clicked.connect(lambda: SetBlock(self.blockSelect.currentText()))
        
        self.signInput1 = QLineEdit(self)
        self.signInput1.setPlaceholderText('Linia 1')
        self.signInput1.setMaximumWidth(200)
        self.signInput2 = QLineEdit(self)
        self.signInput2.setPlaceholderText('Linia 2')
        self.signInput2.setMaximumWidth(200)
        self.signInput3 = QLineEdit(self)
        self.signInput3.setPlaceholderText('Linia 3')
        self.signInput3.setMaximumWidth(200)
        self.signInput4 = QLineEdit(self)
        self.signInput4.setPlaceholderText('Linia 4')
        self.signInput4.setMaximumWidth(200)
        self.signButton = QPushButton('Pozostaw wiadomość', self)
        self.signButton.clicked.connect(lambda: PlaceMessage([self.signInput1.text(),self.signInput2.text(),self.signInput3.text(),self.signInput4.text()]))


        input_layout = QHBoxLayout()
        input_layout.addWidget(self.tpInputX)
        input_layout.addWidget(self.tpInputY)
        input_layout.addWidget(self.tpInputZ)
        input_layout.addWidget(self.tpButton)
        
        select_layout1 = QHBoxLayout()
        select_layout1.addWidget(QLabel('Mob/byt:'))
        select_layout1.addWidget(self.mobSelect)
        select_layout1.addWidget(self.mobButton)
        
        select_layout2 = QHBoxLayout()
        select_layout2.addWidget(QLabel('Blok:'))
        select_layout2.addWidget(self.blockSelect)
        select_layout2.addWidget(self.blockButton)
        
        input_layout2 = QHBoxLayout()
        input_layout2.addWidget(self.signInput1)
        input_layout2.addWidget(self.signInput2)
        input_layout2.addWidget(self.signInput3)
        input_layout2.addWidget(self.signInput4)
        input_layout2.addWidget(self.signButton)

        layout = QVBoxLayout()
        layout.addLayout(input_layout)
        layout.addLayout(select_layout1)
        layout.addLayout(select_layout2)
        layout.addLayout(input_layout2)              
                     
        self.setLayout(layout)

    def on_submit(self):
        input1_val = self.input1.text()
        input2_val = self.input2.text()
        input3_val = self.input3.text()
        select1_val = self.select1.currentText()
        print(f'Input 1: {input1_val}')
        print(f'Input 2: {input2_val}')
        print(f'Input 3: {input3_val}')
        print(f'Select 1: {select1_val}')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
