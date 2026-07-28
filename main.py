from textual.app import App 
from textual.widgets import Label, Static  

class AgendaCli(App): 
    CSS_PATH= "style.tcss"
    def compose(self): 
        yield Static(
            "AgendaCli", 
        )

        yield Static(
            "Date", 
        )

        yield Label(
            "What are the tasks for today?", 
            id="task_header"
        )


if __name__ == "__main__": 
    app = AgendaCli()
    app.run()
