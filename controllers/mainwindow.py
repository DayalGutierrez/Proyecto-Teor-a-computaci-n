from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget
from views.main_window import Ui_Maquinaexpendedora_form 
from controllers.salidas import salida

class MaquinaExpendedoraWindow(QWidget, Ui_Maquinaexpendedora_form):
    def __init__(self):
        super().__init__()
        
        self.dinero = "10"

        self.setupUi(self)
        self.Moneda5_pushButton.clicked.connect(self.mas5)
        self.Moneda10_pushButton.clicked.connect(self.mas10)
        self.billete20_pushButton.clicked.connect(self.mas20)

        

    @Slot()
    def mas5(self):
        s = 'menos5'
        salida(self.dinero,s)
        self.dinero,alerta,producto,cambio = salida(self.dinero,s)
        self.dineroDisponible_label.setText(self.dinero)
        self.alertas_label.setText(alerta)
        self.productoEntregadoNombre_label.setText(producto)
        self.cambioCantidad_label.setText(cambio)
