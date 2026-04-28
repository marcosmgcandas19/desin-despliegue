import time
import random
from PySide6.QtCore import QThread, Signal

class CocheHilo(QThread):
    progreso_actualizado = Signal(int, int)
    ganador_anunciado = Signal(int)

    def __init__(self, id_coche):
        super().__init__()
        self.id_coche = id_coche
        self.progreso = 0
        self.corriendo = True

    def run(self):
        while self.progreso < 100 and self.corriendo:
            time.sleep(random.uniform(0.05, 0.15)) 
            self.progreso += random.randint(1, 4)
            
            if self.progreso > 100: self.progreso = 100
            
            self.progreso_actualizado.emit(self.id_coche, self.progreso)
            
        if self.progreso >= 100 and self.corriendo:
            self.ganador_anunciado.emit(self.id_coche)