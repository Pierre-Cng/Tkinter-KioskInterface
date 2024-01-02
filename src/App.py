from Menu import Menu
from Content import Content
from Footer import Footer 
from Actions import Actions

class App:
    def __init__(self, root):
        self.root = root
        self.configure_kiosk_style()
        self.Menu = Menu(self.root)
        self.Content = Content(self.root)
        self.Footer = Footer(self.root)
        self.Actions = Actions(self.root, self.Menu, self.Content, self.Footer)

    def on_close(self):
        pass  # Handle the close event here

    def on_ctrl_k(self, event=None):
        # Close the interface when Ctrl+K is pressed
        self.root.quit()

    def configure_kiosk_style(self):
        # Disable window close button (X button) action
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        # Maximize the window to full-screen
        self.root.attributes('-fullscreen', True)
        # Bind Ctrl+K event to close the application
        self.root.bind('<Control-k>', self.on_ctrl_k)
