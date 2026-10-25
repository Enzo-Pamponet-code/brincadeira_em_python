from rich.console import Console




console = Console(record=True)
console.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")
console.save_text('textim.txt')
console.export_text()