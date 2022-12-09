from model.home import Home


class HomeAdapter():
    def toJSON(o):
        if isinstance(o, Home):
            location = o.get_location()
            Item = {
                'id': o.get_id(),
                'location': {"lat": str(location["lat"]), "lng": str(location["lng"])},
                'max_residents': o.get_max_residents(),
                'owner_username': o.get_owner_username(),
            }
            return Item
        return None