import json
import pickle
import numpy as np

__data_columns = None
__manufacturers = None
__models = None
__transmission = None
__color = None
__engine_fuel = None
__engine_type = None
__body = None
__state = None
__drivetrain = None


def get_estimated_price(manufacturers, models, transmission, color, engine_fuel, engine_type, body, state, drivetrain,
                        odometer_value, year_produced, engine_has_gas, engine_capacity, has_warranty, is_exchangeable,
                        number_of_photos, up_counter, duration_listed):
    try:
        manu_index = __data_columns.index(manufacturers.lower())
    except:
        manu_index = -1

    try:
        models_index = __data_columns.index(models.lower())
    except:
        models_index = -1

    try:
        color_index = __data_columns.index(color.lower())
    except:
        color_index = -1

    try:
        engineType_index = __data_columns.index(engine_type.lower())
    except:
        engineType_index = -1

    try:
        engineFuel_index = __data_columns.index(engine_fuel.lower())
    except:
        engineFuel_index = -1

    try:
        body_index = __data_columns.index(body.lower())
    except:
        body_index = -1

    try:
        state_index = __data_columns.index(state.lower())
    except:
        state_index = -1

    try:
        drivetrain_index = __data_columns.index(drivetrain.lower())
    except:
        drivetrain_index = -1

    try:
        transmission_index = __data_columns.index(transmission.lower())
    except:
        transmission_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = odometer_value
    x[1] = year_produced
    x[2] = engine_has_gas
    x[3] = engine_capacity
    x[4] = has_warranty
    x[5] = is_exchangeable
    x[6] = number_of_photos
    x[7] = up_counter
    x[8] = duration_listed

    if manu_index >= 0:
        x[manu_index] = 1

    if models_index >= 0:
        x[models_index] = 1

    if color_index >= 0:
        x[color_index] = 1

    if engineType_index >= 0:
        x[engineType_index] = 1

    if engineFuel_index >= 0:
        x[engineFuel_index] = 1

    if body_index >= 0:
        x[body_index] = 1

    if state_index >= 0:
        x[state_index] = 1

    if drivetrain_index >= 0:
        x[drivetrain_index] = 1

    if transmission_index >= 0:
        x[transmission_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts ... start")
    global __data_columns
    global __manufacturers
    global __models
    global __transmission
    global __color
    global __engine_type
    global __engine_fuel
    global __body
    global __state
    global __drivetrain

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __manufacturers = __data_columns[9:59]
        __models = __data_columns[59:1090]
        __transmission = __data_columns[1090:1092]
        __color = __data_columns[1092:1104]
        __engine_fuel = __data_columns[1104:1109]
        __engine_type = __data_columns[1109:1111]
        __body = __data_columns[1111:1123]
        __state = __data_columns[1123:1126]
        __drivetrain = __data_columns[1126: 1129]

    global __model

    with open("./artifacts/used_cars_rf.pickle", "rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts .. done")

def get_manufacturer_name():
    manufacturers = []
    for i in range(len(__manufacturers)):
        manufacturers.append(__manufacturers[i].replace('manufacturer_name_', ''))
    return manufacturers


def get_models_name():
    models = []
    for i in range(len(__models)):
        models.append(__models[i].replace('model_name_', ''))
    return models


def get_transmission_name():
    transmission = []
    for i in range(len(__transmission)):
        transmission.append(__transmission[i].replace('transmission_', ''))
    return transmission


def get_color_name():
    color = []
    for i in range(len(__color)):
        color.append(__color[i].replace('color_', ''))
    return color


def get_engineFuel_name():
    engineFuel = []
    engineFuel1 = []
    for i in range(len(__engine_fuel)):
        engineFuel.append(__engine_fuel[i].replace('engine_fuel_', ''))
    for i in range(len(engineFuel)):
        engineFuel1.append(engineFuel[i].replace('-', ' '))
    return engineFuel1


def get_engineType_name():
    engineType = []
    for i in range(len(__engine_type)):
        engineType.append(__engine_type[i].replace('engine_type_', ''))
    return engineType


def get_body_name():
    body = []
    for i in range(len(__body)):
        body.append(__body[i].replace('body_type_', ''))
    return body


def get_state_name():
    state = []
    for i in range(len(__state)):
        state.append(__state[i].replace('state_', ''))
    return state


def get_drivetrain_name():
    drivetrain = []
    for i in range(len(__drivetrain)):
        drivetrain.append(__drivetrain[i].replace('drivetrain_', ''))
    return drivetrain


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_manufacturer_name())
    print(get_models_name())
    print(get_transmission_name())
    print(get_color_name())
    print(get_engineFuel_name())
    print(get_engineType_name())
    print(get_body_name())
    print(get_state_name())
    print(get_drivetrain_name())
    print(get_estimated_price('subaru', 'outback', "automatic", "silver", "gasoline", "gasoline", "universal", "owned",
                              "front", 190000, 2010, 0, 2.5, 0, 0, 9, 13, 16))
