import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_main import Ui_Carrera
from logic import CocheHilo

class GranPremioApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Carrera()
        self.ui.setupUi(self)
        self.hilos_coches = []
        self.ganador_detectado = False
        self.ui.btn_inicio.clicked.connect(self.comenzar_carrera)

    def comenzar_carrera(self):
        self.ganador_detectado = False
        self.ui.lbl_resultado.setText("🟢 ¡EN MARCHA! 🟢")
        self.ui.btn_inicio.setEnabled(False)
        
        for i in range(5):
            self.ui.barras[i].setValue(0)
            self.ui.labels_coches[i].setContentsMargins(0, 0, 0, 0) # Resetear posición

        self.hilos_coches = []
        for i in range(5):
            hilo = CocheHilo(i)
            hilo.progreso_actualizado.connect(self.actualizar_carrera)
            hilo.ganador_anunciado.connect(self.declarar_ganador)
            self.hilos_coches.append(hilo)
            hilo.start()

    def actualizar_carrera(self, id_coche, valor):
        # Actualizamos la barra
        self.ui.barras[id_coche].setValue(valor)
        
        # Efecto visual: Movemos el emoji usando márgenes
        # Multiplicamos el valor por 4 para simular el desplazamiento en píxeles
        desplazamiento = int(valor * 4.5) 
        self.ui.labels_coches[id_coche].setContentsMargins(desplazamiento, 0, 0, 0)

    def declarar_ganador(self, id_coche):
        if not self.ganador_detectado:
            self.ganador_detectado = True
            emoji_ganador = self.ui.emojis[id_coche]
            self.ui.lbl_resultado.setText(f"🏆 ¡GANADOR: Coche {id_coche + 1} {emoji_ganador}!")
            self.ui.btn_inicio.setEnabled(True)
            self.ui.btn_inicio.setText("¿OTRA CARRERA? 🏁")
            
            for h in self.hilos_coches:
                h.corriendo = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GranPremioApp()
    ventana.show()
    sys.exit(app.exec())