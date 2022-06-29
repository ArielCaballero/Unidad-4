from Aplicacion import NewPacient, PacientsView, PacientIMC
from ManejadorPacientes import ManejadorPacientes

class ControladorPacientes():
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.pacientes = list(repo.obtenerListaPacientes())
    def crearPaciente(self):
        nuevoPaciente = NewPacient(self.vista).show()
        if nuevoPaciente:
            paciente = self.repo.agregarPaciente(nuevoPaciente)
            self.pacientes.append(paciente)
            self.vista.agregarPaciente(paciente)
    def MostrarIMCPaciente(self):
        if self.seleccion==-1:
            return
        paciente = self.pacientes[self.seleccion]
        IMC = PacientIMC(self.vista, paciente).show()

    def seleccionarPaciente(self, index):
        self.seleccion = index
        paciente = self.pacientes[index]
        self.vista.verPacienteEnForm(paciente)
    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        rowid = self.pacientes[self.seleccion].rowid
        detallespaciente = self.vista.obtenerDetalles()
        detallespaciente.rowid = rowid
        paciente = self.repo.modificarPaciente(detallespaciente)
        self.pacientes[self.seleccion] = paciente
        self.vista.modificarPaciente(paciente, self.seleccion)
    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repo.borrarPaciente(paciente)
        self.pacientes.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion=-1
    def start(self):
        for p in self.pacientes:
            self.vista.agregarPaciente(p)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.grabarDatos()