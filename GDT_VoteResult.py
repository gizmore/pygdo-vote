from gdo.core.GDT_Decimal import GDT_Decimal


class GDT_VoteResult(GDT_Decimal):

    def __init__(self, name: str):
        super().__init__(name)
        self.digits(2, 1)
