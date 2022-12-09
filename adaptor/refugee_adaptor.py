from model.refugee import Refugee


class RefugeeAdaptor():
    def toJSON(o):
        if isinstance(o, Refugee):
            Item = {
                'id': o.get_id(),
                'name': o.get_name(),
                'phone_number': o.get_phone_number(),
                'nationality': o.get_nationality(),
                'location': o.get_location(),
                'skills': o.get_skills()
            }
            return Item
        return None



# USE : UserEncoder().toJSON(compt)