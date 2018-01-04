import  iso6346
class ShippingContainer:
    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code = owner_code, serial =str(serial).zfill(6))
    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code,contents= None)

    @classmethod

    def __init__(self, owner_code, contents):
        self.contents = contents
        self.bic = self._make_bic_code(owner_code = owner_code, serial= ShippingContainer._get_next_serial())

class RefrigeratedShippingContainer(ShippingContainer):
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code,str(serial).zfill(6),'R')