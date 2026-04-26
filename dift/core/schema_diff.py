from __future__ import annotations

import polars as pl

from dift.reports.models import SchemaDiff, TypeChange


def compare_schema(old: pl.DataFrame, new: pl.DataFrame) -> SchemaDiff:
    """Compare column presence and column dtypes."""
    old_schema = dict(old.schema)
    new_schema = dict(new.schema)

    old_cols = set(old_schema)
    new_cols = set(new_schema)
    shared_cols = old_cols & new_cols

    type_changes = [
        TypeChange(
            column=column,
            old_type=str(old_schema[column]),
            new_type=str(new_schema[column]),
        )
        for column in sorted(shared_cols)
        if old_schema[column] != new_schema[column]
    ]

    return SchemaDiff(
        columns_added=sorted(new_cols - old_cols),
        columns_removed=sorted(old_cols - new_cols),
        shared_columns=sorted(shared_cols),
        type_changes=type_changes,
    )
