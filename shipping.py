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
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code,contents= None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code,contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, contents):
        self.contents = contents
        self.bic = self._make_bic_code(owner_code = owner_code, serial= ShippingContainer._get_next_serial())

class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    FRIGE_VOLUME_FT3 = 100

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code,str(serial).zfill(6),'R')

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 +32

    def __init__(self, owner_code, contents, celsius):
        super(RefrigeratedShippingContainer, self).__init__(owner_code, contents)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError('Temperature too hot!')
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self,value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)