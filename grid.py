class Grid:
    """ Grid holding Points """

    MIN_SIZE = 0
    MAX_SIZE = 100

    def __init__(self, width, height):
        """ Initialize the size of the grid """

        if (width >= Grid.MIN_SIZE and width <= Grid.MAX_SIZE):
            self._width = width
        else:
            raise ValueError("Width is out of bounds")

        if (height >= Grid.MIN_SIZE and height <= Grid.MAX_SIZE):
            self._height = height
        else:
            raise ValueError("Height is out of bounds")

        self._points = []

    def add_point(self, point):
        """ Adds a point to the Grid """
        if point is None:
            raise ValueError("Point must be defined")

        self._check_is_within_grid(point)

        for existing_point in self._points:
            if existing_point.get_id() == point.get_id():
                raise ValueError("Point ID is not unique")

        self._points.append(point)

    def remove_point(self, id):
        """ Removes a point from the Grid """
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Invalid Point Id")

        for point in self._points:
            if point.get_id() == id:
                self._points.remove(point)
                return

        raise ValueError("Point not found")

    def update_point(self, point):
        """ Updates a point on the Grid """
        if point is None:
            raise ValueError("Point must be defined")

        self._check_is_within_grid(point)

        for index in range(len(self._points)):
            if self._points[index].get_id() == point.get_id():
                self._points[index] = point
                return

        raise ValueError("Point not found")

    def get_point(self, id):
        """ Gets a point on the Grid """
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Invalid Point Id")

        for point in self._points:
            if point.get_id() == id:
                return point

        raise ValueError("Point not found")

    def get_all_points(self):
        """ Gets all points on the Grid """
        return self._points

    def get_grid_width(self):
        return self._width

    def get_grid_height(self):
        return self._height
    def get_num_points(self):
        return len(self._points)

    def _check_is_within_grid(self, point):
        if point.get_x() < 0 or point.get_x() >= self._width:
            raise ValueError("Point outside grid (x)")

        if point.get_y() < 0 or point.get_y() >= self._height:
            raise ValueError("Point outside grid (y)")
