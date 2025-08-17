from django.urls import path
from .views import home, products, armar_pc, exit, detalle_producto, product_list, ver_carrito, agregar_al_carrito, eliminar_del_carrito, actualizar_cantidad, finalizar_compra, agregar_al_ensamblado, finalizar_compra_pc, detalle_producto_pc

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name="products"),
    path('armar_pc/', armar_pc, name='armar_pc'),  
    path('logout/', exit, name='exit'),
    path('producto/<int:id>/', detalle_producto, name='detalle_producto'),
    path('productos/', product_list, name='product_list'),
    path('carrito/', ver_carrito, name='ver_carrito'),  # Ver el carrito
    path('agregar-al-carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),  # Agregar producto
    path('eliminar-del-carrito/<int:carrito_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),  # Eliminar producto
    path('actualizar-cantidad/<int:carrito_id>/', actualizar_cantidad, name='actualizar_cantidad'),  # Actualizar cantidad
    path('finalizar-compra/', finalizar_compra, name='finalizar_compra'),
    path('agregar_al_ensamblado/<int:id>/', agregar_al_ensamblado, name='agregar_al_ensamblado'),
    path('finalizar_compra-pc/', finalizar_compra_pc, name='finalizar_compra_pc'),
    path('detalle_producto_pc/<int:id>/', detalle_producto, name='detalle_producto_pc'),
]
