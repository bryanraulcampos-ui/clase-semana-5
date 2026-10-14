producto = ["Cafe", 5000, 20]

nombre = producto[0]
precio_actual = producto[1]
unidades_actuales = producto[2]

descuento = precio_actual * 15 / 100
precio_promocional = precio_actual - descuento

ingreso_actual = precio_actual * unidades_actuales

aumento_unidades = unidades_actuales * 20 / 100
unidades_proyectadas = unidades_actuales + aumento_unidades

ingreso_promocion = precio_promocional * unidades_proyectadas
diferencia = ingreso_promocion - ingreso_actual

if diferencia > 0:
    recomendacion = "lanzar"
else:
    recomendacion = "no lanzar"

print(f"""
ANÁLISIS DE PROMOCIÓN
Producto: {nombre}
Precio actual: ₡{int(precio_actual)}
Unidades actuales: {unidades_actuales}
Ingreso actual: ₡{int(ingreso_actual)}
Descuento: 15%
Precio promocional: ₡{int(precio_promocional)}
Unidades proyectadas (supuesto +20%): {int(unidades_proyectadas)}
Ingreso con promoción: ₡{int(ingreso_promocion)}
Diferencia: ₡{int(diferencia)}
RECOMENDACIÓN: {recomendacion}.
""")