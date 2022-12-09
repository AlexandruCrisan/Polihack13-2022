from model.provider import Provider


class ProviderAdapter():
    def toJSON(o):
        if isinstance(o, Provider):
            Item = {
                'username': o.get_username(),
                'password': o.get_password(),
                'name': o.get_name(),
                'phone_number': o.get_phone_number(),
                'email': o.get_email(),
                'account_type': type(o).__name__
            }
            return Item
        return None
