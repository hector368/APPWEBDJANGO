from django.db import models

# Create your models here.
class generos(models.Model):
    genero_id = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=255)
    
    class Meta:
        db_table = "generos"

class usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    fk_generos = models.ForeignKey(generos, on_delete=models.CASCADE,default=0)
    
    class Meta:
        db_table = "usuarios"


class categorias(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    class Meta:
        db_table = "categorias"

# Model for Products
class Productos(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    fk_categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    class Meta:
        db_table = "productos"

# Model for Orders
class Pedidos(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    fk_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, choices=[
        ('PENDIENTE', 'Pendiente'),
        ('PROCESADO', 'Procesado'),
        ('ENVIADO', 'Enviado'),
        ('COMPLETADO', 'Completado'),
        ('CANCELADO', 'Cancelado')
    ])

    class Meta:
        db_table = "pedidos"

# Model for Order Details
class DetallePedido(models.Model):
    detalle_id = models.AutoField(primary_key=True)
    fk_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    fk_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "detalle_pedido"

# Model for Customer Addresses
class DireccionesClientes(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    fk_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)

    class Meta:
        db_table = "direcciones_clientes"

# Model for Payment Information
class Pagos(models.Model):
    pago_id = models.AutoField(primary_key=True)
    fk_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=50, choices=[
        ('TARJETA', 'Tarjeta de Crédito/Débito'),
        ('PAYPAL', 'PayPal'),
        ('TRANSFERENCIA', 'Transferencia Bancaria')
    ])
    estado_pago = models.CharField(max_length=50, choices=[
        ('PENDIENTE', 'Pendiente'),
        ('COMPLETADO', 'Completado'),
        ('FALLIDO', 'Fallido')
    ])
    fecha_pago = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "pagos"