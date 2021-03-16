import rich.console
import rich.table
import os


class MessageService:
    def __init__(self):
        pass
    
    @staticmethod
    def show_screen(situation : list, header : str = "Jogo" , message: str="", positions_played=(None, None)):
        
        situation_text_formatted = "".join([f"[bold white on red] {situation[i]} [/bold white on red]"
                                                if i in positions_played 
                                                else (f"[bold white on green] {situation[i]} [/bold white on green]"
                                                        if situation[i] == 1
                                                        else f" {situation[i]} ")
                                                for i in range(len(situation)) ]
                                            )
        os.system('cls' if os.name=='nt' else 'clear')

        table = rich.table.Table(show_header=False, show_lines=False, show_edge=False)
        console = rich.console.Console()

        table.add_column()
        table.add_column()
        table.add_column()

        table.add_row("   teclas ->", " 0  1  2  3  4  5  6  7  8  9 ", "", style="bold white on #016064")    
        table.add_row("resultado ->", situation_text_formatted, "")       
        
        print()
        console.print(header, style="bold white on #03ab5d", justify="center")
        print()
        console.print(table, justify="center")
        print()
        console.print(message, justify="center")

