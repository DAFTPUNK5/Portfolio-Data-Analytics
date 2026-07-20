# Portfolio: Data Analytics, ETL & Financial Compliance

Bienvenido a mi portafolio profesional de análisis de datos. En este espacio consolido soluciones de ingeniería y explotación analítica orientadas a la optimización de procesos, auditoría forense de datos y mitigación de riesgos financieros/comerciales.

## 📂 Estructura del Repositorio

*   **`1-Python-Pandas-PowerBI/`**: Pipelines automatizados en memoria RAM para el saneamiento de datos.
    *   `1.py`: Script de procesamiento ETL masivo. Realiza unificación multifuente mediante uniones relacionales (`.merge`), implementa escudos contra valores nulos (`.fillna`) para aislar registros bajo investigación, purga duplicados por identificador único (`.drop_duplicates`) y estructura matrices dinámicas complejas (`.pivot_table`) para reportería ejecutiva.
*   **`2-SQL-Analitico-PowerBI/`**: Consultas estructuradas de alto rendimiento y control interno.
    *   `auditoria_comisiones_canales.sql`: Query forense que ejecuta cruces multitabla (`LEFT JOIN`), gobierna la integridad del dato mediante sustituciones condicionales (`COALESCE`) para detectar asesores no homologados, y aplica filtros multidimensionales en el flujo para identificar desvíos comerciales críticos.

## 🛠️ Tecnologías Utilizadas
*   **Lenguajes y Librerías:** SQL Server, BigQuery, Python (Pandas, NumPy).
*   **Inteligencia de Negocios:** Power BI (Modelado dimensional en estrella, DAX avanzado).
*   **Procesos:** ETL/ELT, Gobierno de Datos, Auditoría Forense de Información Comercial.

