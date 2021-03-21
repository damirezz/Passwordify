import sys,string,random,pyperclip as pc
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui 
from welcome_page import welcome





weak=string.ascii_letters
mediuum=string.ascii_letters+string.digits
strong=string.ascii_letters+ string.digits + string.punctuation


        

#initialise the QDialog
class window(QWidget):
    def __init__(self,parent=None):
        #initialise the windows(compulsory all time)
        super().__init__(parent)
        #title of window
        self.title="Passwordify"
        #set position of widget(geometry)
        self.left=500
        self.top=200
        #set size of widget
        self.minimumWidth=350
        self.minimumHeight=500
        self.maxiheight=500
        self.maximumWid=600
        self.setWindowIcon(QtGui.QIcon('padlock.svg'))
        self.setStyleSheet('background-color:#01579b')
        
        
    
        #add icon
        #self.iconed=''
        #initialise windows,items are to be placed within the initwindows
        
        self.initwindow()
        self.layout_widget()
       
        
      
        
        
        
        
    
    
        
        
    
    
        
   
        
    def initwindow(self):
        self.setWindowTitle(self.title,)
        
        self.setMaximumHeight(self.maxiheight)
        self.setMaximumWidth(self.maximumWid)
        self.setGeometry(self.left,self.top,self.minimumHeight,self.minimumWidth)
        self.show()
    
   
    def command(self): 
        #aadd functionality to widgets
         spinval=self.spinbox.value()
         global new
        #if password is set to weak do this 
         if self.radio3.isChecked()==True:
             ans=random.choices(weak,k=(spinval))
             new=''.join(ans)
             self.linedisplay.setText(str(new))
             
        
        #if password is set to mediuum do this
         elif self.radio2.isChecked()==True:
             ans=random.choices(mediuum,k=(spinval))
             new= ''.join(ans)
             self.linedisplay.setText(str(new))
             
        
        #if password is set to strong do this
         elif self.radio1.isChecked()==True:
            ans=random.choices(strong,k=(spinval)) 
            new=''.join(ans)
            self.linedisplay.setText(str(new))

         
          
        

       
    #copy password to paste to clipboard     
    def copy(self):
        try:
            pc.copy(new)
            self.message.exec_()

        except NameError:
             self.linedisplay.setText('NULL')
            
          
     
       
        
    def layout_widget(self):
        #create layout 
        grid=QGridLayout()
        self.setLayout(grid)
          
        #create widgets 'QSpinbox,QPushButton,QRadioButton,Qlinedisplay and QLabel'
        self.spinbox=QSpinBox()
        
        self.radio3=QRadioButton('Weak')
        self.radio2=QRadioButton('Medium')
        self.radio1=QRadioButton('Strong')
        
        self.button1=QPushButton('Copy')
        self.button2=QPushButton('Shuffle password')
        
       
        self.linedisplay=QLineEdit()
        
        self.label=QLabel('Password Length:')
        
        self.message=QMessageBox()
        
        
        
        
        
        
        #add widgets to grid layout
        grid.addWidget(self.label,0,0,1,3) 
        grid.addWidget(self.spinbox,0,2,1,3) 
        grid.addWidget(self.radio3, 1,0)  
        grid.addWidget(self.radio2, 1,3,1,4)  
        grid.addWidget(self.radio1, 1,6) 
        grid.addWidget(self.linedisplay,2,1,1,5)
        grid.addWidget(self.button1,3,0,1,2)   
        grid.addWidget(self.button2,3,5,1,2) 
      
        
        
        #setstyle sheet  and functionality for widgett and window
        self.radio1.setStyleSheet('color:white;font-size:20px;font-family:cambria')
        self.radio2.setStyleSheet('color:yellow;font-size:20px;font-family:cambria')
        self.radio2.setChecked(True)
        self.radio3.setStyleSheet('color:red;font-size:20px;font-family:cambria')
        
       
        self.button1.setStyleSheet('padding:10px;color:black;font-family:cambria;font-size:15px;')
        self.button1.setToolTip('Copy to clipboard and paste where needed')
        self.button1.clicked.connect(self.copy)
        
        
        
        
        self.button2.setStyleSheet('padding:10px;color:white;font-family:cambria;font-size:15px;')
        self.button2.clicked.connect(self.command)
        
        
        
        

        self.linedisplay.setStyleSheet('background-color:none;padding:10px;font-size:30px')
        self.linedisplay.setPlaceholderText('Generated Password')
        self.linedisplay.setReadOnly(True)
        
        self.spinbox.setStyleSheet('background-color:white;font-size:50px')
        self.spinbox.setRange(6,14)
        self.spinbox.valueChanged.connect(self.command)
        
     
        
        self.label.setStyleSheet('color:white;font-family:cambria;font-size:15px')
        
        self.message.setText('Copied to clipboard')
        self.message.setIcon(QMessageBox.Information)
        self.message.buttonClicked.connect(self.copy)
        

       
        
        
        
      
        
        
    
    
   
    
    
    
        

        

    


if __name__ == '__main__':

    app=QApplication(sys.argv)
    
    
    
    win=window()
    win.show()
    
    sys.exit(app.exec_())






