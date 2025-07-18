import pandas as pd
from pathlib import Path

def export_df(df: pd.DataFrame, output_path: Path, output_format: str = "csv"):
    """
    Exporta un DataFrame a CSV o Parquet según el formato indicado.
    """
    if output_format == "csv":
        df.to_csv(output_path, index=False)
    elif output_format == "parquet":
        df.to_parquet(output_path, index=False, compression="snappy")
    else:
        raise ValueError(f"Formato no soportado: {output_format}")
