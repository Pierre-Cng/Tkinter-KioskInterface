class Actions:
    def __init__(self, root, menu, content, footer):
        self.root = root 
        self.menu = menu 
        self.content = content 
        self.footer = footer
        self.configure_buttons()

    def configure_buttons(self):
        self.menu.verify_button.config(command=self.verify_config)
        self.menu.config_button.config(command=self.modify_config)
        self.menu.recording_button.config(command=self.start_recording)
        self.menu.send_button.config(command=self.send_data)

    def verify_config(self):
        self.menu.verify_button.config(text='working', command=self.verify_config, bg='blue')
        # lauch script to verify list of the connect stack and their configuration dbc 
        # config file store default conf 
        # update config label 

    def modify_config(self):
        self.menu.config_button.config(text='working', command=self.verify_config, bg='blue')
        # open pop up with list of available stack and available dbc - allow user to associate them together 
        # option to refresh dbc and stack and fetch latest 
        # update config label 

    def start_recording(self):
        # verify if combos are set - verify config - start stopwatch - launch script for stack to record - lauch oscilloscope 
        self.menu.stopwatch.start_stopwatch()
        self.content.graph.switch_oscilloscope()
        self.menu.recording_button.config(text="Stop Recording", command=self.stop_recording, bg='red')
        #execute_bash_script()

    def stop_recording(self):
        # lauch script to save logs and stop stack - stop stopwatch - stop oscilloscope - allow send data button  
        self.menu.stopwatch.stop_stopwatch()
        self.content.graph.switch_oscilloscope()
        self.menu.recording_button.config(text="Start Recording", command=self.start_recording, bg='green')
        
    def send_data(self):
        pass
    # when allowed send recorded logs under vehicule + number file name to s3 server 
