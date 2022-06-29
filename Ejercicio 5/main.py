from Repositorio import RespositorioPacientes
from Aplicacion import PacientsView
from Controlador import ControladorPacientes
from ObjectEncoder import ObjectEncoder

def main():
    json=ObjectEncoder('pacientes.json')
    repo=RespositorioPacientes(json)
    vista=PacientsView()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
    
if __name__=='__main__':
    main()