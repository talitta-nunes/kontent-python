class DataValidationError(Exception):
    ...


# chaves obrigatórias,  usando a content models como base
class ContentSerializer:
    valid_inputs = {
        "title": str,
        "module": str,
        "students": int,
        "description": str,
        "is_active": bool,
    }

    # uso args para não ficar restrita somente as chaves passadas no models.
    # e conseguir capturar as possíveis chaves extras
    def __init__(self, *args, **kwargs):
        self.data = kwargs
        self.errors = {}

    # consolida todas as demais validações num único método
    def is_valid(self) -> bool:
        self.clean_extra_keys()

        try:
            self.validate_required_keys()
            self.validate_data_types()

            return True
        except DataValidationError:
            return False

    # para capturar e excluir chaves extras
    def clean_extra_keys(self):

        data_keys = set(self.data.keys())

        for key in data_keys:
            if key not in self.valid_inputs.keys():
                self.data.pop(key)

    # todas as chaves obrigatórias devem ser passadas, limpar os extras antes.
    def validate_required_keys(self):
        for valid_key in self.valid_inputs.keys():
            if valid_key not in self.data.keys():
                self.errors[valid_key] = "Required key"

        if self.errors:
            raise DataValidationError

    def validate_data_types(self):
        for valid_key, valid_type in self.valid_inputs.items():
            if type(self.data[valid_key]) is not valid_type:

                self.errors.update(
                    {valid_key: f"Wrong data type {valid_type.__name__}"}
                )

        if self.errors:
            raise DataValidationError
