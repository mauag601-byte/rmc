from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Producto, Carrito

def home(request):
    return render(request, 'templates/web/home.html') 

def base(request):
    return render(request, 'templates/web/base.html')

@login_required
def products(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'templates/web/products.html', {'productos': productos}) 

def armar_pc(request):
    # Obtener el parámetro 'categoria' de la URL
    categoria = request.GET.get('categoria')
    if categoria:
        # Filtrar productos por categoría
        productos = Producto.objects.filter(category=categoria)  # Asegúrate de que 'category' coincida con el campo en el modelo
    else:
        # Si no hay filtro, mostrar todos los productos
        productos = Producto.objects.all()

    # Cargar o inicializar el ensamblado en la sesión
    ensamblado = request.session.get('ensamblado', [])
    total = sum(item['precio'] for item in ensamblado)  # Sumar los precios de los componentes en el ensamblado

    # Pasar los productos, ensamblado y el total al template
    return render(request, 'templates/web/armar_pc.html', {
        'productos': productos,
        'ensamblado': ensamblado,
        'total': total
    })

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Producto

def agregar_al_ensamblado(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    # Lógica para agregar al ensamblado
    ensamblado = request.session.get('ensamblado', [])
    
    # Agregar el producto al ensamblado
    ensamblado.append({
        'id': producto.id,
        'nombre': producto.title,
        'precio': float(producto.price),
    })
    
    # Guardar el ensamblado en la sesión
    request.session['ensamblado'] = ensamblado
    
    # Redirigir o renderizar un template
    return redirect('armar_pc')  # Redirigir a la página de armar pc 


def exit(request):
    logout(request)  
    return redirect('home')    

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'templates/web/detalle_producto.html', {'producto': producto})

def detalle_producto_pc(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'templates/web/detalle_producto_pc.html')

def product_list(request):
    # Obtener todos los productos de la base de datos
    products = Producto.objects.all()

    # Inicializar el carrito si no existe
    if 'cart' not in request.session:
        request.session['cart'] = []

    # Si se hace una petición POST (cuando el usuario selecciona un producto)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            product = Producto.objects.get(id=product_id)
            # Agregar el producto al carrito (almacenado en la sesión)
            request.session['cart'].append(product.id)
            request.session.modified = True
            return redirect('product_list')

    # Obtener los productos seleccionados por el usuario
    cart_items = Producto.objects.filter(id__in=request.session['cart'])

    return render(request, 'templates/web/product_list.html', {'products': products, 'cart_items': cart_items})


@login_required
def ver_carrito(request):
    carrito_items = Carrito.objects.filter(user=request.user)
    total = sum(item.total for item in carrito_items)  # Suma los totales de cada producto
    return render(request, 'templates/web/carrito/carrito.html', {'carrito_items': carrito_items, 'total': total})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, created = Carrito.objects.get_or_create(user=request.user, producto=producto)
    if not created:
        carrito_item.cantidad += 1  # Si el producto ya está en el carrito, aumenta la cantidad
        carrito_item.save()
    return redirect('ver_carrito')  # Redirige al carrito después de agregar el producto

@login_required
def eliminar_del_carrito(request, carrito_id):
    carrito_item = get_object_or_404(Carrito, id=carrito_id, user=request.user)
    carrito_item.delete()
    return redirect('ver_carrito')

@login_required
def actualizar_cantidad(request, carrito_id):
    carrito_item = get_object_or_404(Carrito, id=carrito_id, user=request.user)
    nueva_cantidad = request.POST.get('cantidad', 1)
    carrito_item.cantidad = nueva_cantidad
    carrito_item.save()
    return redirect('ver_carrito')

@login_required
def finalizar_compra(request):
    # Este es el bloque de código que debe estar correctamente indentado
    carrito_items = Carrito.objects.filter(user=request.user, comprado=False)
    total = sum(item.total for item in carrito_items)
    return render(request, 'templates/web/carrito/finalizar_compra.html', {'carrito_items': carrito_items, 'total': total})
@login_required
def finalizar_compra_pc(request):
    # Obtener el ensamblado de la sesión
    ensamblado = request.session.get('ensamblado', [])

    if request.method == 'POST':
        # Manejo de la eliminación de productos
        product_id_to_remove = request.POST.get('remove_product_id')
        if product_id_to_remove:
            # Eliminar el producto de la lista del ensamblado
            ensamblado = [item for item in ensamblado if str(item['id']) != product_id_to_remove]
            request.session['ensamblado'] = ensamblado
            return redirect('finalizar_compra_pc')  # Redirigir para actualizar la lista

    # Calcular el total
    total = sum(item['precio'] for item in ensamblado)

    # Pasar los productos y el total al template
    return render(request, 'templates/web/carrito/finalizar_compra_pc.html', {
        'carrito_items': ensamblado,
        'total': total
    })
def verificar_compatibilidad(producto):
    # Aquí se puede agregar la lógica específica de compatibilidad según los componentes seleccionados.
    # Por ejemplo, si ya hay una placa madre en el ensamblado, comprobar que el procesador sea compatible.
    return True