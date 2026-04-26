from __future__ import annotations

from dift.reports.models import DiffReport


def assign_risk_level(report: DiffReport) -> str:
    """Assign a simple MVP risk level based on visible changes."""
    score = 0

    if report.schema_diff.columns_added or report.schema_diff.columns_removed:
        score += 2
    if report.schema_diff.type_changes:
        score += 3

    if report.row_diff.changed_rows:
        score += 1
    if report.row_diff.removed_rows:
        score += 2

    if report.quality_diff.duplicate_diff.delta_duplicates > 0:
        score += 1

    null_spikes = [d for d in report.quality_diff.null_diffs if d.delta_null_pct >= 5]
    score += min(len(null_spikes), 3)

    if score >= 6:
        return "high"
    if score >= 3:
        return "medium"
    return "low"
