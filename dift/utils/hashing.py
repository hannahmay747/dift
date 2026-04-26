from __future__ import annotations

import polars as pl


def row_hash_expr(columns: list[str]) -> pl.Expr:
    """Create a stable-ish row hash expression across shared columns."""
    if not columns:
        return pl.lit("").hash()
    return pl.struct([pl.col(column) for column in columns]).hash()
