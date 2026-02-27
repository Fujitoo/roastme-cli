#!/usr/bin/env python3
"""
RoastMe CLI - A savage terminal game for bored students.
"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.table import Table
from rich.text import Text

from roast_engine import RoastEngine

console = Console()

LEVELS = ["easy", "medium", "savage"]
STYLES = ["all", "academic", "nerd", "overconfident", "existential", "lifestyle"]


def print_header():
    """Print the game header."""
    header = Text()
    header.append("🔥 ", style="bold")
    header.append("ROASTME", style="bold red")
    header.append(" CLI", style="bold")
    header.append(" 🔥", style="bold")
    console.print(Panel(header, style="bold yellow"))
    console.print()


def show_main_menu():
    """Display the main menu and return user's choice."""
    console.print("[bold cyan]Select an option:[/bold cyan]\n")
    console.print("  [bold]1[/bold]. 🎮 Start Roast Session")
    console.print("  [bold]2[/bold]. ⚡ Quick Roast")
    console.print("  [bold]3[/bold]. 🎭 View Styles")
    console.print("  [bold]4[/bold]. 📊 View Levels")
    console.print("  [bold]5[/bold]. 🚪 Exit")
    console.print()
    
    choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5"], default="1")
    return choice


def select_level():
    """Let user select difficulty level interactively."""
    console.print("\n[bold cyan]📊 Select Difficulty Level:[/bold cyan]\n")
    console.print("  [bold]1[/bold]. 🧸 Easy   - Playful teasing, gentle jabs")
    console.print("  [bold]2[/bold]. 🌶️ Medium - Sharp sarcasm, actual burns")
    console.print("  [bold]3[/bold]. 🔥 Savage - Brutal honesty, maximum damage")
    console.print()
    
    choice = Prompt.ask("Choose level", choices=["1", "2", "3"], default="2")
    return LEVELS[int(choice) - 1]


def select_style():
    """Let user select roast style interactively."""
    console.print("\n[bold cyan]🎭 Select Roast Style:[/bold cyan]\n")
    console.print("  [bold]1[/bold]. 📚 Academic    - Roasts about grades & study habits")
    console.print("  [bold]2[/bold]. 🤓 Nerd        - Tech-focused burns")
    console.print("  [bold]3[/bold]. 💪 Overconfident - For big egos, small results")
    console.print("  [bold]4[/bold]. 🌌 Existential - Deep, philosophical roasts")
    console.print("  [bold]5[/bold]. 🏠 Lifestyle   - Daily habits & living situations")
    console.print("  [bold]6[/bold]. 🎲 All Styles  - Mix of everything (default)")
    console.print()
    
    choice = Prompt.ask("Choose style", choices=["1", "2", "3", "4", "5", "6"], default="6")
    if choice == "6":
        return "all"
    return STYLES[int(choice)]


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
    Prompt.ask("Press Enter to continue")


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
    Prompt.ask("Press Enter to continue")


def start_game():
    """Start a new roast session with interactive menu."""
    print_header()

    # Select level and style through menus
    level = select_level()
    style = select_style()

    # Collect user info
    console.print("\n[bold cyan]📝 Let's get to know you...[/bold cyan]\n")

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
    Prompt.ask("Press Enter to continue")


def quick_roast():
    """Quick roast someone without full interactive mode."""
    print_header()

    # Get name directly
    name = Prompt.ask("Enter name to roast")
    
    # Select level and style
    level = select_level()
    style = select_style()
    
    # Get count
    count = IntPrompt.ask("Number of roasts", default=3, show_default=True)
    count = max(1, min(10, count))

    # Create engine with minimal info
    engine = RoastEngine(name, "existing", "regret", 5, level)

    style_display = style.capitalize() if style != "all" else "All Styles"
    console.print(f"\n[bold red]🎤 Roasting {name} at {level} difficulty ({style_display})...[/bold red]\n")

    roasts = engine.generate_roasts(count, style if style != "all" else None)

    for i, roast in enumerate(roasts, 1):
        console.print(Panel(
            roast,
            title=f"Roast #{i}",
            style="bold red",
            border_style="yellow",
        ))

    console.print()
    Prompt.ask("Press Enter to continue")


def main():
    """Main entry point with menu loop."""
    while True:
        print_header()
        choice = show_main_menu()
        
        if choice == "1":
            start_game()
        elif choice == "2":
            quick_roast()
        elif choice == "3":
            show_styles()
        elif choice == "4":
            show_levels()
        elif choice == "5":
            console.print("\n[bold green]👋 Thanks for playing RoastMe CLI! Stay humble and touch grass.[/bold green]\n")
            break


if __name__ == "__main__":
    main()
