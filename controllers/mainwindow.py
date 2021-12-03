from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget
from views.main_window import Ui_Maquinaexpendedora_form 
from controllers.salidas import salida

class MaquinaExpendedoraWindow(QWidget, Ui_Maquinaexpendedora_form):
    def __init__(self):
        super().__init__()
        
        self.dinero = "0"
        g = {
            "q0":{
                "5":"mas5",
                "10":"mas10",
                "20":"mas20",
                "50":"mas50",
                "r":"mdi",
                "c355":"mdi",
                "c235":"mdi",
                "sd":"n"
            },
            "q5":{
                "5":"mas5",
                "10":"mas10",
                "20":"mas20",
                "50":"mdm",
                "r":"mdi",
                "c355":"mdi",
                "c235":"mdi",
                "sd":"menos5"
            },
            "q10":{
                "5":"mas5",
                "10":"mas10",
                "20":"mas20",
                "50":"mdm",
                "r":"mdi",
                "c355":"mdi",
                "c235":"mdi",
                "sd":"menos10"
            },
            "q15":{
                "5":"mas5",
                "10":"mas10",
                "20":"mas20",
                "50":"mdm",
                "r":"mdi",
                "c355":"mdi",
                "c235":"c235menos15",
                "sd":"menos15"
            },
            "q20":{
                "5":"mas5",
                "10":"mas10",
                "20":"mas20",
                "50":"mdm",
                "r":"mdi",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos20"
            },
            "q25":{
                "5":"mas5",
                "10":"mas10",
                "20":"mas20",
                "50":"mdm",
                "r":"mdi",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos25"
            },
            "q30":{
                "5":"mas5",
                "10":"mas10",
                "20":"mas20",
                "50":"mdm",
                "r":"mdi",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos30"
            },
            "q35":{
                "5":"mas5",
                "10":"mas10",
                "20":"mdm",
                "50":"mdm",
                "r":"mdi",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos35"
            },
            "q40":{
                "5":"mrl",
                "10":"mrl",
                "20":"mrl",
                "50":"mrl",
                "r":"rmenos40",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos40"
            },
            "q45":{
                "5":"mrl",
                "10":"mrl",
                "20":"mrl",
                "50":"mrl",
                "r":"rmenos40",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos45"
            },
            "q50":{
                "5":"mrl",
                "10":"mrl",
                "20":"mrl",
                "50":"mrl",
                "r":"rmenos40",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos50"
            }
        }

        g = {
            "q0":{
                "5":"q5",
                "10":"q10",
                "20":"q20",
                "50":"q50",
                "r":"q0",
                "c355":"q0",
                "c235":"q0",
                "sd":"q0"
            },
            "q5":{
                "5":"q10",
                "10":"q15",
                "20":"q25",
                "50":"q5",
                "r":"q5",
                "c355":"q5",
                "c235":"q5",
                "sd":"q0"
            },
            "q10":{
                "5":"q15",
                "10":"q20",
                "20":"q30",
                "50":"q10",
                "r":"q10",
                "c355":"q10",
                "c235":"q10",
                "sd":"q0"
            },
            "q15":{
                "5":"q20",
                "10":"q25",
                "20":"q35",
                "50":"q15",
                "r":"q15",
                "c355":"q15",
                "c235":"q0",
                "sd":"q0"
            },
            "q20":{
                "5":"mas5",
                "10":"mas10",
                "20":"mas20",
                "50":"mdm",
                "r":"mdi",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos20"
            },
            "q25":{
                "5":"mas5",
                "10":"mas10",
                "20":"mas20",
                "50":"mdm",
                "r":"mdi",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos25"
            },
            "q30":{
                "5":"mas5",
                "10":"mas10",
                "20":"mas20",
                "50":"mdm",
                "r":"mdi",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos30"
            },
            "q35":{
                "5":"mas5",
                "10":"mas10",
                "20":"mdm",
                "50":"mdm",
                "r":"mdi",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos35"
            },
            "q40":{
                "5":"mrl",
                "10":"mrl",
                "20":"mrl",
                "50":"mrl",
                "r":"rmenos40",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos40"
            },
            "q45":{
                "5":"mrl",
                "10":"mrl",
                "20":"mrl",
                "50":"mrl",
                "r":"rmenos40",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos45"
            },
            "q50":{
                "5":"mrl",
                "10":"mrl",
                "20":"mrl",
                "50":"mrl",
                "r":"rmenos40",
                "c355":"c355menos20",
                "c235":"c235menos15",
                "sd":"menos50"
            }
        }

        self.setupUi(self)
        self.Moneda5_pushButton.clicked.connect(self.mas5)
        self.Moneda10_pushButton.clicked.connect(self.mas10)
        self.billete20_pushButton.clicked.connect(self.mas20)
        self.billete50_pushButton.clicked.connect(self.mas50)
        

        

    @Slot()
    def mas5(self):
        s = 'mas5'
        salida(self.dinero,s)
        self.dinero,alerta,producto,cambio = salida(self.dinero,s)
        self.dineroDisponible_label.setText(self.dinero)
        self.alertas_label.setText(alerta)
        self.productoEntregadoNombre_label.setText(producto)
        self.cambioCantidad_label.setText(cambio)

    @Slot()
    def mas10(self):
        s = 'mas10'
        salida(self.dinero,s)
        self.dinero,alerta,producto,cambio = salida(self.dinero,s)
        self.dineroDisponible_label.setText(self.dinero)
        self.alertas_label.setText(alerta)
        self.productoEntregadoNombre_label.setText(producto)
        self.cambioCantidad_label.setText(cambio)

    @Slot()
    def mas20(self):
        s = 'mas20'
        salida(self.dinero,s)
        self.dinero,alerta,producto,cambio = salida(self.dinero,s)
        self.dineroDisponible_label.setText(self.dinero)
        self.alertas_label.setText(alerta)
        self.productoEntregadoNombre_label.setText(producto)
        self.cambioCantidad_label.setText(cambio)

    @Slot()
    def mas50(self):
        s = 'mas50'
        salida(self.dinero,s)
        self.dinero,alerta,producto,cambio = salida(self.dinero,s)
        self.dineroDisponible_label.setText(self.dinero)
        self.alertas_label.setText(alerta)
        self.productoEntregadoNombre_label.setText(producto)
        self.cambioCantidad_label.setText(cambio)
