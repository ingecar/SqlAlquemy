import db
from models import Producto

def agregar(elemento: str , valor: float) -> None:
    """
    Este metodo permite agregar productos a la base de datos
    :param elemento: representa el nombre
    :param valor: representa el valor
    :return: No tiene retorno
    """
    p = Producto(elemento, valor)
    db.session.add(p)
    db.session.commit()
    print('Producto creado!')

def actualizar(id: str, nuevo_nombre: str, nuevo_precio:int) -> None:
    """
    Este metodo modifica uun producto de la base de datos
    :param id: Representa el identificador
    :param nuevo_nombre: Representa el nuevo nombre del producto
    :param nuevo_precio: Representa el nuevo valor del producto
    :return: No tiene retorno
    """
    pd = db.session.query(Producto).filter_by(id=id).first()
    pd.nombre = nuevo_nombre
    pd.precio = nuevo_precio
    db.session.add(pd)
    db.session.commit()
    print('Producto actualizado!')

def consultar(id: str) -> None:
    """
    Este metodo permite consultar un registro en la tabla e imprimir sus datos
    :param id: Representa el identificador
    :return: No tiene retorno
    """
    pd = db.session.query(Producto).filter_by(id=id).first()
    if pd:
        print(pd.id,pd.nombre, pd.precio)
    else:
        print('El producto no existe')

def borrar(id: int) -> None:
    """
    Este metodo elimina os elementos de una tabla
    :param id: Representa el identificador
    :return: No tiene retorno
    """
    pd = db.session.query(Producto).get(id)
    db.session.delete(pd)
    db.session.commit()
    print('Producto eliminado!')

def listar() -> None:
    """
    Este metodo permite imprimit todos los elementos de una tabla
    :return: No tiene retorno
    """
    ob = db.session.query(Producto).all()
    for ca in ob:
        print( ca.id, ca.nombre, ca.precio)

def filtro_por_precio(valor:int) -> None:
   """
   Este metodo muestra los productos menores al precio indicado
   :param valor: Representa el valor del filtro
   :return:
   """
   ob = db.session.query(Producto).filter(Producto.precio < valor).all()
   print('Los productos con precio menor a', valor, 'son:')
   for ca in ob:
        print(ca.id,ca.nombre, ca.precio)


def contar() -> None:
    """
    Este metodo cuenta la cantidad de productos en el sistema
    :return: Retorna un mensaje con el numero total
    """
    pd = db.session.query(Producto).count()
    print('El sistema tiene', '(', pd ,')', 'productos')

