from rich.console import Console
from rich.table import Table

console = Console()

STATUS_COLORS = {
    "PASS": "green",
    "WARN": "yellow",
    "FAIL": "red"
}


def print_results(results):

    table = Table(title="GPU Cluster Health Report")

    table.add_column("Check")
    table.add_column("Status")
    table.add_column("Severity")
    table.add_column("Message")
    table.add_column("Recommendation")

    for result in results:

        status = (
            f"[{STATUS_COLORS[result.status]}]"
            f"{result.status}[/{STATUS_COLORS[result.status]}]"
        )

        table.add_row(
            result.name,
            status,
            result.severity,
            result.message,
            result.recommendation or "-"
        )

    console.print(table)