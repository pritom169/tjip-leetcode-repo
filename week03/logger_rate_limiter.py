class Logger:
    # TC: 0(1), everytime a message comes, lookups are done in constant amount of time.
    # SC: 0(M), M = Number of unique messages.
    def __init__(self):
        self.message_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # If it's not in dictionary, means this message has come for the
        # first time. Hence it should return True
        if message not in self.message_dict:
            self.message_dict[message] = timestamp
            return True
        
        # If it is in dictionary, it means this message has been appeared
        # before. Now we check the different ot timestamp. If it is >= 10,
        # we return True otherwise False 
        if timestamp - self.message_dict[message] >= 10:
            self.message_dict[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
