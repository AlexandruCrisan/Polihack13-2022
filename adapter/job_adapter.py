from model.job import Job


class JobAdapter():
    def toJSON(o):
        if isinstance(o, Job):
            Item = {
                'id': o.get_id(),
                'title': o.get_title(),
                'description': o.get_description(),
                'min_salary': o.get_min_salary(),
                'username': o.get_username(),
                'city': o.get_city(),
            }
            return Item
        return None