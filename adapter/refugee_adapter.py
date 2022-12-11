from model.refugee import Refugee


class RefugeeAdapter():
    def toJSON(o):
        if isinstance(o, Refugee):
            loc = o.get_location()
            Item = {
                'username': o.get_username(),
                'password': o.get_password(),
                'name': o.get_name(),
                'email': o.get_email(),
                'phone_number': o.get_phone_number(),
                'nationality': o.get_nationality(),
                'location': {"lat": str(loc["lat"]), "lng": str(loc["lng"])},
                'address': o.get_address(),
                'skills': o.get_skills(),
                'donations': o.get_donations(),
                'account_type': type(o).__name__
            }
            return Item
        return None



# USE : UserEncoder().toJSON(compt)