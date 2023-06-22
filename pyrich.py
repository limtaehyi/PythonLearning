from rich import print
from rich.table import Table
from rich.console import Console
from rich.progress import Progress
import time

# 예제 1. 스타일링된 텍스트 출력
print("[bold blue]Hello, World![/bold blue]")

# 예제 2. 테이블 출력
console = Console()

table = Table(title="Rich Table")

table.add_column("ID", justify="right", style="cyan", no_wrap=True)
table.add_column("Name", style="magenta")
table.add_column("Age", justify="right", style="green")

table.add_row("1", "John Doe", "30")
table.add_row("2", "Jane Doe", "28")
table.add_row(
    "3",
    "[red]my name[/red]: is what?",
    "[bold]bold[/bold] text",
)


console.print(table)

# 예제 3. 진행 표시줄 사용
with Progress() as progress:
    task_id = progress.add_task("[cyan]Processing...", total=100)

    while not progress.finished:
        time.sleep(0.02)
        progress.update(task_id, advance=1)
