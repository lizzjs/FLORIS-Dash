
user_defined_dict = {
    "floris_version": "v2.3.0",
    "name": "floris_input_file_Example",
    "description": "Example FLORIS Input file",
    "type": "floris_input",
    "logging": {
        "console": {
            "enable": True,
            "level": "INFO"
        },
        "file": {
            "enable": False,
            "level": "INFO"
        }
    },

    "farm": {
        "description": "Example 2x2 Wind Farm",
        "name": "farm_example_2x2",
        "type": "farm",
        "properties": {},
    },

    "turbine": {
        "description": "NREL 5MW",
        "name": "nrel_5mw",
        "type": "turbine",
        "properties": {},
    },
    
    "wake": {
        "description": "wake",
        "name": "wake_default",
        "type": "wake",
        "properties": {},
    }

}

default_input_dict = {
    "floris_version": "v2.3.0",
    "name": "floris_input_file_Example",
    "description": "Example FLORIS Input file",
    "type": "floris_input",
    "logging": {
        "console": {
            "enable": True,
            "level": "INFO"
        },
        "file": {
            "enable": False,
            "level": "INFO"
        }
    },

    "farm": {
        "description": "Example 2x2 Wind Farm",
        "name": "farm_example_2x2",
        "type": "farm",
        "properties": {
            "air_density": 1.225,
            "layout_x": [
                0.0
            ],
            "layout_y": [
                0.0
            ],
            "specified_wind_height": -1,
            "turbulence_intensity": [
                0.06
            ],
            "wind_direction": [
                270.0
            ],
            "wind_shear": 0.12,
            "wind_speed": [
                9.0
            ],
            "wind_veer": 0.0,
            "wind_x": [
                0
            ],
            "wind_y": [
                0
            ]
        },
    },

    "turbine": {
        "description": "NREL 5MW",
        "name": "nrel_5mw",
        "type": "turbine",
        "properties": {
            "TSR": 8.0,
            "blade_count": 3,
            "blade_pitch": 0.0,
            "generator_efficiency": 1.0,
            "hub_height": 90.0,
            "ngrid": 5,
            "pP": 1.88,
            "pT": 1.88,
            "power_thrust_table": {
                "power": [
                    0.0,
                    0.0,
                    0.1780851,
                    0.28907459,
                    0.34902166,
                    0.3847278,
                    0.40605878,
                    0.4202279,
                    0.42882274,
                    0.43387274,
                    0.43622267,
                    0.43684468,
                    0.43657497,
                    0.43651053,
                    0.4365612,
                    0.43651728,
                    0.43590309,
                    0.43467276,
                    0.43322955,
                    0.43003137,
                    0.37655587,
                    0.33328466,
                    0.29700574,
                    0.26420779,
                    0.23839379,
                    0.21459275,
                    0.19382354,
                    0.1756635,
                    0.15970926,
                    0.14561785,
                    0.13287856,
                    0.12130194,
                    0.11219941,
                    0.10311631,
                    0.09545392,
                    0.08813781,
                    0.08186763,
                    0.07585005,
                    0.07071926,
                    0.06557558,
                    0.06148104,
                    0.05755207,
                    0.05413366,
                    0.05097969,
                    0.04806545,
                    0.04536883,
                    0.04287006,
                    0.04055141
                ],
                "thrust": [
                    1.19187945,
                    1.17284634,
                    1.09860817,
                    1.02889592,
                    0.97373036,
                    0.92826162,
                    0.89210543,
                    0.86100905,
                    0.835423,
                    0.81237673,
                    0.79225789,
                    0.77584769,
                    0.7629228,
                    0.76156073,
                    0.76261984,
                    0.76169723,
                    0.75232027,
                    0.74026851,
                    0.72987175,
                    0.70701647,
                    0.54054532,
                    0.45509459,
                    0.39343381,
                    0.34250785,
                    0.30487242,
                    0.27164979,
                    0.24361964,
                    0.21973831,
                    0.19918151,
                    0.18131868,
                    0.16537679,
                    0.15103727,
                    0.13998636,
                    0.1289037,
                    0.11970413,
                    0.11087113,
                    0.10339901,
                    0.09617888,
                    0.09009926,
                    0.08395078,
                    0.0791188,
                    0.07448356,
                    0.07050731,
                    0.06684119,
                    0.06345518,
                    0.06032267,
                    0.05741999,
                    0.05472609
                ],
                "wind_speed": [
                    2.0,
                    2.5,
                    3.0,
                    3.5,
                    4.0,
                    4.5,
                    5.0,
                    5.5,
                    6.0,
                    6.5,
                    7.0,
                    7.5,
                    8.0,
                    8.5,
                    9.0,
                    9.5,
                    10.0,
                    10.5,
                    11.0,
                    11.5,
                    12.0,
                    12.5,
                    13.0,
                    13.5,
                    14.0,
                    14.5,
                    15.0,
                    15.5,
                    16.0,
                    16.5,
                    17.0,
                    17.5,
                    18.0,
                    18.5,
                    19.0,
                    19.5,
                    20.0,
                    20.5,
                    21.0,
                    21.5,
                    22.0,
                    22.5,
                    23.0,
                    23.5,
                    24.0,
                    24.5,
                    25.0,
                    25.5
                ]
            },
            "rloc": 0.5,
            "rotor_diameter": 126.0,
            "tilt_angle": 0.0,
            "use_points_on_perimeter": False,
            "yaw_angle": 0.0
        },
    },
    
    "wake": {
        "description": "wake",
        "name": "wake_default",
        "type": "wake",
        "properties": {
            "combination_model": "sosfs",
            "deflection_model": "gauss",
            "turbulence_model": "crespo_hernandez",
            "velocity_model": "gauss_legacy",
            "parameters": {
                "wake_deflection_parameters": {
                    "gauss": {
                        "dm": 1.0,
                        "eps_gain": 0.2,
                        "use_secondary_steering": True
                    }
                },
                "wake_turbulence_parameters": {
                    "crespo_hernandez": {
                        "ai": 0.8,
                        "constant": 0.5,
                        "downstream": -0.32,
                        "initial": 0.1
                    }
                },
                "wake_velocity_parameters": {
                    "gauss_legacy": {
                        "calculate_VW_velocities": True,
                        "eps_gain": 0.2,
                        "ka": 0.38,
                        "kb": 0.004,
                        "use_yaw_added_recovery": True
                    }
                }
            }
        },
    }
}

user_defined_dict = default_input_dict

wind_rose_data = {
    "direction": ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"],
    "strength": ["0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "1-2", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "2-3", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "3-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-4", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "4-5", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "5-6", "6+",  "6+",  "6+",  "6+",  "6+",  "6+",  "6+",  "6+",  "6+",  "6+",  "6+",  "6+",  "6+",  "6+",  "6+",  "6+"],
    "frequency": ["0.5", "0.6", "0.5", "0.4", "0.4", "0.3", "0.4", "0.4", "0.6", "0.4", "0.5", "0.6", "0.6", "0.5", "0.4", "0.1", "1.6", "1.8", "1.5", "1.6", "1.6", "1.2", "1.5", "1.7", "2.2", "2", "2.3", "2.4", "2.3", "2.6", "2.3", "0.8", "0.9", "1.3", "1.6", "0.9", "1", "0.6", "0.6", "0.9", "1.4", "1.7", "1.9", "2.2", "1.8", "1.7", "1.8", "0.8", "0.9", "0.8", "1.2", "1", "0.8", "0.4", "0.5", "0.5", "0.8", "0.9", "1.3", "1.1", "1.2", "1.2", "1.3", "1", "0.4", "0.5", "1.2", "0.5", "0.4", "0.2", "0.4", "0.4", "0.7", "0.6", "0.7", "0.8", "0.9", "1", "1", "0.7", "0.3", "0.3", "0.6", "0.2", "0.1", "0.1", "0.05", "0.1", "0.1", "0.2", "0.3", "0.4", "0.9", "0.9", "0.9", "0.3", "0.2", "0.1", "0.1", "0.1", "0.1", "0.1", "0.05", "0.05", "0.1", "0.05", "0.2", "0.2", "0.4", "0.7", "0.7", "0.4", "0.1", "0.1", "0.1", "0.1", "0.1", "0.05", "0.05", "0.05", "0.05", "0.1", "0.1", "0.1", "0.9", "2.2", "1.5", "0.2"]
}

boundary_data = {
   "boundary_x": [-1000,1500, 1500, -1000],
   "boundary_y": [1500, 1500, -500, -500] 
}

wake_model_preview_dict = default_input_dict
wake_model_preview_dict['farm']['properties']['layout_x'] = [0.0, 630.0, 0.0]
wake_model_preview_dict['farm']['properties']['layout_y'] = [0.0, 0.0, 630]
