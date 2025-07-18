import argparse
import pandas as pd
from pathlib import Path
import logging

# Importar funciones desde los scripts
from scripts.transform import (
    standardize_column_names,
    convert_types,
    add_total_amount,
    merge_orders_customers,
    normalize_country,
    categorize_vip
)
from scripts.validate import (
    unique_key,
    no_nulls,
    positive_values,
    valid_email,
    allowed_status,
    date_not_future
)
from scripts.export import export_df

# Configurar logging
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main(orders_path, customers_path, output_path, output_format):
    try:
        logging.info("Proceso ETL iniciado.")

        # Leer datos
        df_orders = pd.read_csv(orders_path)
        df_customers = pd.read_csv(customers_path)

        # Transformaciones
        df_orders = standardize_column_names(df_orders)
        df_customers = standardize_column_names(df_customers)

        df_orders = convert_types(df_orders)
        df_orders = add_total_amount(df_orders)

        df = merge_orders_customers(df_orders, df_customers)
        df = normalize_country(df)
        df = categorize_vip(df)

        # Validaciones
        unique_key(df, "order_id")
        no_nulls(df, ["order_id", "order_date", "customer_id", "email"])
        positive_values(df, ["quantity", "unit_price", "total_amount"])
        valid_email(df)
        allowed_status(df)
        date_not_future(df, "order_date")

        # Exportar
        export_df(df, Path(output_path), output_format)
        logging.info("Proceso ETL finalizado exitosamente.")
        print("✅ Proceso completado. Archivo exportado a:", output_path)

    except Exception as e:
        logging.error(f"Error en el proceso ETL: {e}")
        print("❌ Error durante la ejecución:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script ETL")
    parser.add_argument("--orders", required=True, help="Ruta del archivo de pedidos")
    parser.add_argument("--customers", required=True, help="Ruta del archivo de clientes")
    parser.add_argument("--output", required=True, help="Ruta de salida del archivo transformado")
    parser.add_argument("--format", required=False, default="csv", choices=["csv", "parquet"], help="Formato de salida")

    args = parser.parse_args()

    main(args.orders, args.customers, args.output, args.format)
