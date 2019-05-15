class Push():
    def __init__(self, _payload):

        self.repository = None
        self.sender = None
        self.commits = []
        self.message = None
        self.payload = _payload

    def process(self):
        try:
            self.repository = self.payload['repository']
            self.sender = self.payload['sender']["login"]

            for commit in self.payload['commits']:
                self.commits.append(commit)
        except:
            pass
        # Start building message

        message = '{} pushed {} {} to {} \n\n'.format(
            self.sender,
            len(self.commits),
            "commits" if len(self.commits) > 1 else "commit",
            self.payload['ref']
        )
        # Compose lists of added|removed|modified filenames

        added = []
        removed = []
        modified = []

        for commit in self.commits:
            # Append commits messages
            message += "Message: " + commit["message"] + '\n'

            if len(commit["added"]):
                for added_file in commit["added"]:
                    if added_file not in added:
                        added.append(added_file)
            if len(commit["removed"]):
                for removed_file in commit["removed"]:
                    if removed_file not in removed:
                        removed.append(removed_file)
            if len(commit["modified"]):
                for modified_file in commit["modified"]:
                    if modified_file not in modified:
                        modified.append(modified_file)
        if len(added):
            message += '\nNew files: \n'
            for file_name in added:
                message += file_name + '\n'

        if len(removed):
            message += '\nRemoved files: \n'
            for file_name in removed:
                message += file_name + '\n'

        if len(modified):
            message += '\nModified files: \n'
            for file_name in modified:
                message += file_name + '\n'

        message += '\n ' + 'Compare: ' + self.payload['compare']
        self.message = message
        return

