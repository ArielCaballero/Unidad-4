from Repositorio import RespositorioProvincias
from Aplicacion import ProvinceView
from Controlador import ControladorProvincias
from ObjectEncoder import ObjectEncoder

def main():
    json=ObjectEncoder('provincias.json')
    repo=RespositorioProvincias(json)
    vista=ProvinceView()
    ctrl=ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
    
if __name__=='__main__':
    main()