class Point:
    """ 2D Point """

    def __init__(self, id, x, y):
        """ Initializes the x/y coordinates """

        if not isinstance(id, int) or id < 0:
            raise ValueError("ID must be a positive int")

        if not isinstance(x, int) or x < 0:
            raise ValueError("X must be a positive int")

        if not isinstance(y, int) or y < 0:
            raise ValueError("Y must be a positive int")

        self._id = id
        self._x = x
        self._y = y

    def get_id(self):
        """ Returns the unique id of the point """

        return self._id

    def get_x(self):
        """ Returns the x coordinate """

        return self._x

    def get_y(self):
        """ Returns the y coordinate """

        return self._y

    def to_dict(self):
        """ Returns a dictionary representation of a point """
        dict = {}
        dict['id'] = self._id
        dict['x'] = self._x
        dict['y'] = self._y

        return dict
