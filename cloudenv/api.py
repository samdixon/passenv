from handlers import op


class Create:
    def __init__(self, name, key, project, password_manager):
        self.name = name
        self.key = key
        self.project = project
        self.password_manager = password_manager

        self.PrintMe()
        self.decider()

    def PrintMe(self):
        print(
            "Name: " + str(self.name),
            "Key: " + str(self.key),
            "Project: " + str(self.project),
            "Password Manager: " + str(self.password_manager)
        )

    def decider(self):
        if self.password_manager == '1password':
            op.OnePasswordCreate(self)
        elif self.password_manager == 'LastPass':
            lp.LastPassCreate(self)


class List:
    def __init__(self, force_remote_update, active_only, password_manager):
        self.force_remote_update = force_remote_update
        self.active_only = active_only

        self.decider()

    def decider(self):
        pass
