import db
import metodos

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    metodos.listar()
    #metodos.filtro_por_precio(3)
    #metodos.contar()
    #metodos.agregar('Queso', 3.4)
    #metodos.consultar(5)
    #metodos.actualizar(2, 'Jabon', 2.3)
    #metodos.borrar(5)
