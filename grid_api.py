from flask import Flask, request
from grid import Grid
from point import Point
import json

app = Flask(__name__)
grid = Grid(10,10)

@app.route('/grid/points', methods=['POST'])
def add_point():
    content = request.json

    try:
        point = Point(content['id'], content['x'], content['y'])
        grid.add_point(point)

        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response

@app.route('/grid/points/<int:point_id>', methods=['GET'])
def get_point(point_id):
    try:
        point = grid.get_point(point_id)

        response = app.response_class(
            status=200,
            response=json.dumps(point.to_dict()),
            mimetype='application/json'
        )
        return response

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response

@app.route('/grid/points/<int:point_id>', methods=['PUT'])
def update_point(point_id):
    content = request.json
    try:
        point = Point(point_id, content['x'], content['y'])
        grid.update_point(point)

        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            status=404
        )
    return response

@app.route('/grid/points/<int:point_id>', methods=['DELETE'])
def delete_point(point_id):
    try:
        point = grid.remove_point(point_id)

        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response


@app.route('/grid/points/all', methods=['GET'])
def get_all_points():
    points = grid.get_all_points()
    point_list = []

    for point in points:
        point_list.append(point.to_dict())
    response = app.response_class(
        status=200,
        response=json.dumps(point_list),
        mimetype='application/json'
    )
    return response

@app.route('/grid', methods=['GET'])
def get_grid():
    grid_details ={}
    grid_details['width'] = grid.get_grid_width()
    grid_details['height'] = grid.get_grid_height()
    grid_details['num_points'] = grid.get_num_points()

    response = app.response_class(
        status=200,
        response=json.dumps(grid_details),
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run()