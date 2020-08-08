from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_manufacturers_name')
def get_manufacturers_name():
    response = jsonify({
        'manufacturers': util.get_manufacturer_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_models_name')
def get_models_name():
    response = jsonify({
        'models': util.get_models_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_transmission_name')
def get_transmission_name():
    response = jsonify({
        'transmission': util.get_transmission_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_color_name')
def get_color_name():
    response = jsonify({
        'color': util.get_color_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_engineFuel_name')
def get_engineFuel_name():
    response = jsonify({
        'engineFuel': util.get_engineFuel_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_engineType_name')
def get_engineType_name():
    response = jsonify({
        'engineType': util.get_engineType_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_body_name')
def get_body_name():
    response = jsonify({
        'body': util.get_body_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_state_name')
def get_state_name():
    response = jsonify({
        'state': util.get_state_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_drivetrain_name')
def get_drivetrain_name():
    response = jsonify({
        'drivetrain': util.get_drivetrain_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_used_car', methods=['POST'])
def predict_used_car():
    manufacturers = request.form['manufacturers']
    models = request.form['models']
    transmission = request.form['transmission']
    color = request.form['color']
    engine_fuel = request.form['engine_fuel']
    engine_type = request.form['engine_type']
    body = request.form['body']
    state = request.form['state']
    drivetrain = request.form['drivetrain']
    odometer_value = int(request.form['odometer_value'])
    year_produced = int(request.form['year_produced'])
    engine_has_gas = int(request.form['engine_has_gas'])
    engine_capacity = float(request.form['engine_capacity'])
    has_warranty = int(request.form['has_warranty'])
    is_exchangeable = int(request.form['is_exchangeable'])
    number_of_photos = float(request.form['number_of_photos'])
    up_counter = int(request.form['up_counter'])
    duration_listed = int(request.form['duration_listed'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(manufacturers, models, transmission, color, engine_fuel,engine_type, body, state,
                                                    drivetrain, odometer_value,
                                                    year_produced, engine_has_gas, engine_capacity, has_warranty,
                                                    is_exchangeable,
                                                    number_of_photos, up_counter, duration_listed)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    print("Starting Python Flask Server For Used Cars Prediction ...")
    app.run()
