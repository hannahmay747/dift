from __future__ import annotations

from enum import Enum

import typer
from rich.console import Console

from dift.core.comparator import compare_datasets
from dift.reports.console_report import render_console
from dift.reports.json_report import render_json

app = typer.Typer(help="Dift: Git diff for datasets.")
console = Console()


class ReportFormat(str, Enum):
    console = "console"
    json = "json"


@app.command()
def main(
    old_dataset: str = typer.Argument(..., help="Path to the old dataset."),
    new_dataset: str = typer.Argument(..., help="Path to the new dataset."),
    key: str | None = typer.Option(None, "--key", "-k", help="Primary key column for row comparison."),
    report: ReportFormat = typer.Option(ReportFormat.console, "--report", "-r", help="Report format."),
    output: str | None = typer.Option(None, "--output", "-o", help="Write report to a file."),
) -> None:
    """Compare two datasets and explain what changed."""
    try:
        diff_report = compare_datasets(old_dataset, new_dataset, key=key)
    except Exception as exc:  # noqa: BLE001 - CLI should show readable errors
        console.print(f"[bold red]Error:[/bold red] {exc}")
        raise typer.Exit(code=1) from exc

    if report == ReportFormat.json:
        payload = render_json(diff_report, output=output)
        if output is None:
            console.print(payload)
        else:
            console.print(f"Wrote JSON report to {output}")
    else:
        render_console(diff_report)


if __name__ == "__main__":
    app()
