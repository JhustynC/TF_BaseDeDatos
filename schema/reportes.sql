--Para Desempeño de Agente

SELECT a.cedula, a.nombre, a.apellido, sum(t.comision*t.precio_venta)
FROM agente a
JOIN transaccion t ON a.cedula = t.ce_agente
WHERE t.estado = true AND t.fecha_final <= '2024-01-01' AND t.fecha_final >= '2024-01-01'
GROUP BY a.cedula

--Porcentaje de Venta por parroquia

SELECT
    p.nombre AS parroquia,
    COUNT(t.id) AS cantidad_ventas,
    (COUNT(t.id) * 100.0 / (SELECT COUNT(id) FROM transaccion)) AS porcentaje_venta
FROM
    parroquia p
JOIN
    inmueble i ON p.id = i.id_parroquia
JOIN
    transaccion t ON i.clave_castral = t.id_inmueble
WHERE
    t.estado = true
GROUP BY
    p.id, p.nombre
ORDER BY
    porcentaje_venta DESC;

--Ventas Mensuales

SELECT
    TO_CHAR(t.fecha_final, 'YYYY-MM') AS mes,
    COUNT(t.id) AS cantidad_ventas,
    SUM(t.precio_venta) AS total_ventas,
    SUM(t.precio_venta * t.comision) AS total_comisiones
FROM
    transaccion t
WHERE
    t.estado = true
    AND EXTRACT(YEAR FROM t.fecha_final) = 2024  -- Reemplaza '2024' con el año deseado
GROUP BY
    TO_CHAR(t.fecha_final, 'YYYY-MM')
ORDER BY
    mes;
