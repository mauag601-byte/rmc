from django.db import models
from django.contrib.auth.models import User


# Definir opciones para socket_type
SOCKET_CHOICES = [
    ('AM5', 'AM5'),
    ('AM4', 'AM4'),
    ('LGA1200', 'LGA1200'),
    ('LGA1700', 'LGA1700'),
    ('TR4', 'TR4'),
    ('LGA1151', 'LGA1151'),
    ('BGA', 'BGA'),
]

# Definir opciones para memory_type
MEMORY_CHOICES = [
    ('DDR3', 'DDR3'),
    ('DDR4', 'DDR4'),
    ('DDR5', 'DDR5'),
    ('LPDDR3', 'LPDDR3'),
    ('LPDDR4', 'LPDDR4'),
    ('LPDDR5', 'LPDDR5'),
]

# Definir opciones para watts (para fuentes de alimentación u otros productos)
WATTS_CHOICES = [
    (10, '10W'),
    (20, '20W'),
    (30, '30W'),
    (40, '40W'),
    (50, '50W'),
    (60, '60W'),
    (70, '70W'),
    (80, '80W'),
    (90, '90W'),
    (100, '100W'),
    (110, '110W'),
    (120, '120W'),
    (130, '130W'),
    (140, '140W'),
    (150, '150W'),
    (160, '160W'),
    (170, '170W'),
    (180, '180W'),
    (190, '190W'),
    (200, '200W'),
    (210, '210W'),
    (220, '220W'),
    (230, '230W'),
    (240, '240W'),
    (250, '250W'),
    (260, '260W'),
    (270, '270W'),
    (280, '280W'),
    (290, '290W'),
    (300, '300W'),
    (310, '310W'),
    (320, '320W'),
    (330, '330W'),
    (340, '340W'),
    (350, '350W'),
    (360, '360W'),
    (370, '370W'),
    (380, '380W'),
    (390, '390W'),
    (400, '400W'),
    (410, '410W'),
    (420, '420W'),
    (430, '430W'),
    (440, '440W'),
    (450, '450W'),
    (460, '460W'),
    (470, '470W'),
    (480, '480W'),
    (490, '490W'),
    (500, '500W'),
    (510, '510W'),
    (520, '520W'),
    (530, '530W'),
    (540, '540W'),
    (550, '550W'),
    (560, '560W'),
    (570, '570W'),
    (580, '580W'),
    (590, '590W'),
    (600, '600W'),
    (610, '610W'),
    (620, '620W'),
    (630, '630W'),
    (640, '640W'),
    (650, '650W'),
    (660, '660W'),
    (670, '670W'),
    (680, '680W'),
    (690, '690W'),
    (700, '700W'),
    (710, '710W'),
    (720, '720W'),
    (730, '730W'),
    (740, '740W'),
    (750, '750W'),
    (760, '760W'),
    (770, '770W'),
    (780, '780W'),
    (790, '790W'),
    (800, '800W'),
    (810, '810W'),
    (820, '820W'),
    (830, '830W'),
    (840, '840W'),
    (850, '850W'),
    (860, '860W'),
    (870, '870W'),
    (880, '880W'),
    (890, '890W'),
    (900, '900W'),
    (910, '910W'),
    (920, '920W'),
    (930, '930W'),
    (940, '940W'),
    (950, '950W'),
    (960, '960W'),
    (970, '970W'),
    (980, '980W'),
    (990, '990W'),
    (1000, '1000W'),
    (1010, '1010W'),
    (1020, '1020W'),
    (1030, '1030W'),
    (1040, '1040W'),
    (1050, '1050W'),
    (1060, '1060W'),
    (1070, '1070W'),
    (1080, '1080W'),
    (1090, '1090W'),
    (1100, '1100W'),
    (1110, '1110W'),
    (1120, '1120W'),
    (1130, '1130W'),
    (1140, '1140W'),
    (1150, '1150W'),
    (1160, '1160W'),
    (1170, '1170W'),
    (1180, '1180W'),
    (1190, '1190W'),
    (1200, '1200W'),
    (1210, '1210W'),
    (1220, '1220W'),
    (1230, '1230W'),
    (1240, '1240W'),
    (1250, '1250W'),
    (1260, '1260W'),
    (1270, '1270W'),
    (1280, '1280W'),
    (1290, '1290W'),
    (1300, '1300W'),
    (1310, '1310W'),
    (1320, '1320W'),
    (1330, '1330W'),
    (1340, '1340W'),
    (1350, '1350W'),
    (1360, '1360W'),
    (1370, '1370W'),
    (1380, '1380W'),
    (1390, '1390W'),
    (1400, '1400W'),
    (1410, '1410W'),
    (1420, '1420W'),
    (1430, '1430W'),
    (1440, '1440W'),
    (1450, '1450W'),
    (1460, '1460W'),
    (1470, '1470W'),
    (1480, '1480W'),
    (1490, '1490W'),
    (1500, '1500W'),
    (1510, '1510W'),
    (1520, '1520W'),
    (1530, '1530W'),
    (1540, '1540W'),
    (1550, '1550W'),
    (1560, '1560W'),
    (1570, '1570W'),
    (1580, '1580W'),
    (1590, '1590W'),
    (1600, '1600W'),
    (1610, '1610W'),
    (1620, '1620W'),
    (1630, '1630W'),
    (1640, '1640W'),
    (1650, '1650W'),
    (1660, '1660W'),
    (1670, '1670W'),
    (1680, '1680W'),
    (1690, '1690W'),
    (1700, '1700W'),
    (1710, '1710W'),
    (1720, '1720W'),
    (1730, '1730W'),
    (1740, '1740W'),
    (1750, '1750W'),
    (1760, '1760W'),
    (1770, '1770W'),
    (1780, '1780W'),
    (1790, '1790W'),
    (1800, '1800W'),
    (1810, '1810W'),
    (1820, '1820W'),
    (1830, '1830W'),
    (1840, '1840W'),
    (1850, '1850W'),
    (1860, '1860W'),
    (1870, '1870W'),
    (1880, '1880W'),
    (1890, '1890W'),
    (1900, '1900W'),
    (1910, '1910W'),
    (1920, '1920W'),
    (1930, '1930W'),
    (1940, '1940W'),
    (1950, '1950W'),
    (1960, '1960W'),
    (1970, '1970W'),
    (1980, '1980W'),
    (1990, '1990W'),
    (2000, '2000W'),
]

# Modelo de Categoría para clasificar los productos (CPU, GPU, RAM, etc.)
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=100, decimal_places=2)

    class Meta:
        verbose_name_plural = 'categorías'
    
    def __str__(self):
        return self.name

# Definir las categorías de productos
CATEGORIA_CHOICES = [
    ('procesadores', 'Procesadores'),
    ('placas_madre', 'Placas Madre'),
    ('memoria_ram', 'Memoria RAM'),
    ('tarjeta_grafica', 'Tarjeta Gráfica'),
    ('almacenamiento', 'Almacenamiento'),
    ('fuente_poder', 'Fuente de Poder'),
    ('gabinete', 'Gabinete'),
    ('monitor', 'Monitor'),
    ('cooler', 'Cooler'),
    ('auriculares', 'Auriculares')
]

# Modelo de Producto con compatibilidad entre componentes
class Producto(models.Model):
    category = models.ForeignKey('Category', related_name='productos', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='media/productos', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)  # Control de stock
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    # Campos para especificaciones técnicas
    socket_type = models.CharField(max_length=50, choices=SOCKET_CHOICES, blank=True, null=True)  
    memory_type = models.CharField(max_length=50, choices=MEMORY_CHOICES, blank=True, null=True)  
    watts = models.PositiveIntegerField(choices=WATTS_CHOICES, blank=True, null=True)  

    category = models.CharField(
        max_length=50,
        choices=CATEGORIA_CHOICES  
    )

    class Meta:
        verbose_name_plural = 'productos'
        ordering = ('-created',)

    def __str__(self):
        return self.title

# Modelo para manejar las relaciones entre productos compatibles
class Compatibility(models.Model):
    producto = models.ForeignKey(Producto, related_name='compatibilidades', on_delete=models.CASCADE)
    compatible_with = models.ManyToManyField(Producto, related_name='productos_compatibles')

    def __str__(self):
        return f'{self.producto.title} compatible con {", ".join([p.title for p in self.compatible_with.all()])}'

# Modelo de Carrito para gestionar los productos añadidos por los usuarios
class Carrito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con el producto
    cantidad = models.PositiveIntegerField(default=1)  # Cantidad de productos
    created = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    comprado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.producto.title} - {self.cantidad}'

    @property
    def total(self):
        return self.cantidad * self.producto.price  # Calcula el total para este producto

    def __str__(self):
        return f"{self.user.username} - {self.producto.title}"

    
    # Validación de stock (opcional, si lo deseas)
    def save(self, *args, **kwargs):
     try:
        # Asegúrate de que 'self.cantidad' sea un entero
        cantidad = int(self.cantidad)  # Convertir a entero
     except ValueError:
        raise ValueError("La cantidad debe ser un número entero válido.")
    
    # Validación de stock
     if cantidad > self.producto.stock:
        raise ValueError("No hay suficiente stock disponible para este producto.")
    
    # Llamar al método save original
     super().save(*args, **kwargs)