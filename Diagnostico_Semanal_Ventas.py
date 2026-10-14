"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]

# TODO: calcula total, cantidad, mayor y menor para Centro.

# TODO: calcula promedio, rango, diferencia y porcentaje para Centro.

# TODO: repite los indicadores para Norte.


# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.

# TODO: compara los totales y los rangos.

# TODO: presenta un reporte con etiquetas claras y f-strings.
# TODO: escribe las tres conclusiones solicitadas en la guía.

"""Análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]

# Centro
total_centro = sum(ventas_centro)
cantidad_centro = len(ventas_centro)
mayor_centro = max(ventas_centro)
menor_centro = min(ventas_centro)

promedio_centro = total_centro / cantidad_centro
rango_centro = mayor_centro - menor_centro
diferencia_centro = mayor_centro - promedio_centro
porcentaje_centro = (mayor_centro / total_centro) * 100

# Norte
total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)
mayor_norte = max(ventas_norte)
menor_norte = min(ventas_norte)

promedio_norte = total_norte / cantidad_norte
rango_norte = mayor_norte - menor_norte
diferencia_norte = mayor_norte - promedio_norte
porcentaje_norte = (mayor_norte / total_norte) * 100

# Meta de ejemplo
meta = 120000

if promedio_centro > meta:
    estado_centro = "superó la meta"
elif promedio_centro == meta:
    estado_centro = "igualó la meta"
else:
    estado_centro = "no alcanzó la meta"

if promedio_norte > meta:
    estado_norte = "superó la meta"
elif promedio_norte == meta:
    estado_norte = "igualó la meta"
else:
    estado_norte = "no alcanzó la meta"

# Comparaciones
if total_centro > total_norte:
    mejor_total = "Centro"
else:
    mejor_total = "Norte"

if rango_centro > rango_norte:
    mayor_rango = "Centro"
else:
    mayor_rango = "Norte"

# Reporte
print(f"""
REPORTE DE VENTAS

TIENDA CENTRO
Total: ₡{total_centro}
Cantidad: {cantidad_centro}
Mayor venta: ₡{mayor_centro}
Menor venta: ₡{menor_centro}
Promedio: ₡{promedio_centro:.2f}
Rango: ₡{rango_centro}
Diferencia: ₡{diferencia_centro:.2f}
Porcentaje: {porcentaje_centro:.2f}%
Resultado: {estado_centro}

TIENDA NORTE
Total: ₡{total_norte}
Cantidad: {cantidad_norte}
Mayor venta: ₡{mayor_norte}
Menor venta: ₡{menor_norte}
Promedio: ₡{promedio_norte:.2f}
Rango: ₡{rango_norte}
Diferencia: ₡{diferencia_norte:.2f}
Porcentaje: {porcentaje_norte:.2f}%
Resultado: {estado_norte}

CONCLUSIONES
1. La tienda con mayor total de ventas fue {mejor_total}.
2. La tienda con mayor rango de ventas fue {mayor_rango}.
3. La tienda Norte tuvo un promedio de ventas más alto que Centro.
""")