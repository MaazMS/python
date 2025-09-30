class OverLimitException(Exception):

    def __ini__(self, message):
        self.message =  message


def withdrawl(amount):
    if (amount > 500):
        raise OverLimitException("you can not withdraw more then 500 per day")
    print("you can withdraw less then 500 per day")

withdrawl(400)