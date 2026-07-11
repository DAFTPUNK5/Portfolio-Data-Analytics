SELECT 
    t1.id_operacion,
    t1.id_asesor,
    COALESCE(t2.nombre_completo, 'ASESOR_NO_REGISTRADO') AS nombre_asesor,
    COALESCE(t2.tipo_contrato, 'INVESTIGACION_AUDITORIA') AS auditoria_contrato,
    t1.monto_venta,
    t1.canal_ingreso
FROM hechos_comisiones AS t1
LEFT JOIN dim_asesores AS t2
ON t1.id_asesor = t2.cod_asesor
WHERE t1.codigo_error = 0 AND t1.monto_venta > 50000
ORDER BY t1.monto_venta DESC;
