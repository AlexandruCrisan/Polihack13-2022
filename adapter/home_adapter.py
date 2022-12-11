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
                'street_name': o.get_street_name(),
                'location_image': o.get_location_image(),
                'new': o.get_new(),
            }
            return Item
        return None