from commands.commands import Help, Add, Show, Edit, Search, Unknown


class CommandFactory:
    def __init__(self, io, repository):
        self.io = io
        self.repository = repository

        self.commands = {
            "h": Help(self.io, self.repository),
            "add": Add(self.io, repository),
            "show": Show(self.io, repository),
            "edit": Edit(self.io, repository),
            "search": Search(self.io, repository),
        }
    
    def set_command(self, command):
        if command in self.commands:
            return self.commands[command]
        return Unknown(self.io)