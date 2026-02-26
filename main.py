#!/usr/bin/env python3
"""
RoastMe CLI - A savage terminal game for bored students.
"""

import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.table import Table
from rich.text import Text

from roast_engine import RoastEngine

app = typer.Typer(
    name="roastme",
    help="RoastMe CLI - Get roasted in your terminal!",
    add_completion=False,
)
console = Console()


def print_header():
    """Print the game header."""
    header = Text()
    header.append("🔥 ", style="bold")
    header.append("ROASTME", style="bold red")
    header.append(" CLI", style="bold")
    header.append(" 🔥", style="bold")
    console.print(Panel(header, style="bold yellow"))
    console.print()


@app.command("start")
def start_game(
    level: str = typer.Option(
        "medium",
        "--level", "-l",
        help="Difficulty level: easy, medium, or savage",
        case_sensitive=False,
    ),
    style: str = typer.Option(
        "all",
        "--style", "-s",
        help="Roast style: academic, nerd, overconfident, existential, lifestyle, or all",
        case_sensitive=False,
    ),
):
    """Start a new roast session."""
    print_header()

    # Validate level
    if level.lower() not in ["easy", "medium", "savage"]:
        console.print("[red]Invalid level! Using 'medium'.[/red]")
        level = "medium"

    # Validate style
    valid_styles = ["all", "academic", "nerd", "overconfident", "existential", "lifestyle"]
    if style.lower() not in valid_styles:
        console.print(f"[red]Invalid style! Choose from: {', '.join(valid_styles)}. Using 'all'.[/red]")
        style = "all"

    # Collect user info
    console.print("[bold cyan]📝 Let's get to know you...[/bold cyan]\n")

    name = Prompt.ask("Enter your name")
    hobby = Prompt.ask("Enter your hobby")
    major = Prompt.ask("Enter your major")
    confidence = IntPrompt.ask(
        "Rate your confidence",
        default=5,
        show_default=True,
    )

    # Create engine
    engine = RoastEngine(name, hobby, major, confidence, level)

    # Display profile
    style_display = style.capitalize() if style != "all" else "All Styles"
    console.print()
    console.print(Panel(
        f"[bold]Name:[/bold] {engine.name}\n"
        f"[bold]Hobby:[/bold] {engine.hobby}\n"
        f"[bold]Major:[/bold] {engine.major}\n"
        f"[bold]Confidence:[/bold] {engine.confidence}/10\n"
        f"[bold]Difficulty:[/bold] {engine.get_level_description()}\n"
        f"[bold]Style:[/bold] {style_display}",
        title="🎯 Your Profile",
        style="bold magenta",
    ))
    console.print()

    # Greeting
    console.print(f"[italic]{engine.get_greeting()}[/italic]\n")

    # Generate roasts
    console.print("[bold red]🎤 ROAST MODE ACTIVATED[/bold red]\n")
    roasts = engine.generate_roasts(5, style if style != "all" else None)

    for i, roast in enumerate(roasts, 1):
        style_name = list(engine.__dict__.keys())
        console.print(Panel(
            roast,
            title=f"Roast #{i}",
            style="bold red",
            border_style="yellow",
        ))
        console.print()

    # Comeback mode
    console.print("[bold green]💬 COMEBACK MODE[/bold green]\n")
    console.print("Time to defend yourself! Type your comeback below.\n")

    comeback = Prompt.ask("Your comeback")

    if comeback.strip():
        rating, judgment = engine.rate_comeback(comeback)

        # Display rating
        rating_bar = "█" * rating + "░" * (10 - rating)
        console.print()
        console.print(Panel(
            f"[bold]Comeback Rating:[/bold] {rating}/10\n"
            f"[{rating_bar}]\n\n"
            f"[italic]{judgment}[/italic]",
            title="📊 Comeback Analysis",
            style="bold green",
        ))
    else:
        console.print("[yellow]Silence? That's a 0/10 comeback.[/yellow]")

    # Farewell
    console.print()
    console.print(f"[italic]{engine.get_farewell()}[/italic]\n")


@app.command("roast")
def quick_roast(
    name: str = typer.Argument(..., help="Name to roast"),
    level: str = typer.Option(
        "medium",
        "--level", "-l",
        help="Difficulty level: easy, medium, or savage",
    ),
    style: str = typer.Option(
        "all",
        "--style", "-s",
        help="Roast style: academic, nerd, overconfident, existential, lifestyle, or all",
    ),
    count: int = typer.Option(
        3,
        "--count", "-c",
        help="Number of roasts to generate",
        min=1,
        max=10,
    ),
):
    """Quick roast someone without interactive mode."""
    print_header()

    if level.lower() not in ["easy", "medium", "savage"]:
        level = "medium"

    valid_styles = ["all", "academic", "nerd", "overconfident", "existential", "lifestyle"]
    if style.lower() not in valid_styles:
        style = "all"

    # Create engine with minimal info
    engine = RoastEngine(name, "existing", "regret", 5, level)

    style_display = style.capitalize() if style != "all" else "All Styles"
    console.print(f"[bold red]🎤 Roasting {name} at {level} difficulty ({style_display})...[/bold red]\n")

    roasts = engine.generate_roasts(count, style if style != "all" else None)

    for i, roast in enumerate(roasts, 1):
        console.print(f"[{i}] {roast}")

    console.print()


@app.command("styles")
def show_styles():
    """Show available roast styles with examples."""
    print_header()

    table = Table(title="🎭 Available Roast Styles", style="bold cyan", expand=True)
    table.add_column("Style", style="bold yellow", width=15)
    table.add_column("Icon", width=5)
    table.add_column("Description", style="white")
    table.add_column("Best For", style="green")

    styles_info = [
        ("academic", "📚", "Roasts about academic performance and study habits", "Students, researchers"),
        ("nerd", "🤓", "Tech-focused roasts for the digitally obsessed", "Developers, gamers"),
        ("overconfident", "💪", "Roasts for those with big egos and small results", "Show-offs, braggers"),
        ("existential", "🌌", "Deep, philosophical roasts about life's meaning", "Philosophers, overthinkers"),
        ("lifestyle", "🏠", "Roasts about daily habits and living situations", "Everyone with bad habits"),
    ]

    for style, icon, desc, best_for in styles_info:
        table.add_row(style.capitalize(), icon, desc, best_for)

    console.print(table)
    console.print()
    console.print("[bold]Usage:[/bold] python main.py start --style <style_name>")
    console.print("[dim]Example: python main.py start --style academic[/dim]")
    console.print()


@app.command("levels")
def show_levels():
    """Show available difficulty levels with examples."""
    print_header()

    table = Table(title="📊 Difficulty Levels", style="bold cyan", expand=True)
    table.add_column("Level", style="bold yellow", width=12)
    table.add_column("Icon", width=5)
    table.add_column("Description", style="white")
    table.add_column("Intensity", style="red")

    levels_info = [
        ("easy", "🧸", "Playful teasing with gentle jabs. Safe for work and sensitive feelings.", "☆☆☆"),
        ("medium", "🌶️", "Sharp sarcasm with actual burns. Use with friends who can take a joke.", "★★☆"),
        ("savage", "🔥", "Brutal honesty with maximum damage. Not for the faint of heart.", "★★★"),
    ]

    for level, icon, desc, intensity in levels_info:
        table.add_row(level.capitalize(), icon, desc, intensity)

    console.print(table)
    console.print()
    console.print("[bold]Usage:[/bold] python main.py start --level <level_name>")
    console.print("[dim]Example: python main.py start --level savage[/dim]")
    console.print()


def main():
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
