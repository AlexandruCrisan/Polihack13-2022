from model.refugee import Refugee


class RefugeeAdapter():
    def toJSON(o):
        if isinstance(o, Refugee):
            Item = {
                'username': o.get_username(),
                'password': o.get_password(),
                'name': o.get_name(),
                'phone_number': o.get_phone_number(),
                'nationality': o.get_nationality(),
                'location': o.get_location(),
                'skills': o.get_skills(),
                'donations': o.get_donations(),
                'account_type': type(o).__name__
            }
            return Item
        return None



# USE : UserEncoder().toJSON(compt)