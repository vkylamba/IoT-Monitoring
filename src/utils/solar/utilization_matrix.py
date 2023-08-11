
SYSTEM_VARIABLES = {
    "GRID",
    "WEATHER",
    "GENERATION",
    "LOAD",
    "DAYHOUR"
}

GRID_STATES = [
    "ABSENT",
    "PRESENT",
    "IMPORTING",
    "EXPORTING"
]

WEATHER_STATES = [
    "SUNNY",
    "CLOUDY",
    "RAINY"
]

GENERATION_STATES = [
    "HIGH",
    "MEDIUM",
    "LOW",
    "ZERO"
]

LOAD_STATES = [
    "HIGH",
    "MEDIUM",
    "LOW",
    "ZERO"
]

DAYTIME = [
    "NIGHT",
    "MORNING",
    "NOON",
    "EVENING"
]

SYSTEM_STATES = {
    "SOLAR_UNDER_UTILIZED": [
        # (DAYTIME, GRID_STATE, WEATHER_STATE, GENERATION_STATE, LOAD_STATE)
        ("NOON", "ABSENT", "SUNNY", "MEDIUM", "MEDIUM"),
        ("NOON", "ABSENT", "SUNNY", "LOW", "LOW")
    ],
    "SOLAR_DISCONNECTED": [
        ("MORNING", "*", "*", "ZERO", "*"),
        ("NOON", "*", "*", "ZERO", "*"),
        ("EVENING", "*", "*", "ZERO",  "*"),
    ],
    "SYSTEM_POWER_LEAKAGE": [
        ("NOON", "IMPORTING", "SUNNY", "HIGH", "MEDIUM"),
        ("NOON", "IMPORTING", "SUNNY", "HIGH", "LOW")
    ]
}


def get_solar_system_state(grid_status, solar_status, day_status, load_status, weather_status):

    overall_state = ""
    for state in SYSTEM_STATES:
        state_condition_day = SYSTEM_STATES[state][0]
        state_condition_grid = SYSTEM_STATES[state][1]
        state_condition_weather = SYSTEM_STATES[state][2]
        state_condition_generation = SYSTEM_STATES[state][3]
        state_condition_load = SYSTEM_STATES[state][4]

        match = True
        match = match and (state_condition_day == "*" or state_condition_day == day_status)
        match = match and (state_condition_grid == "*" or state_condition_grid == grid_status)
        match = match and (state_condition_weather == "*" or state_condition_weather == weather_status)
        match = match and (state_condition_generation == "*" or state_condition_generation == solar_status)
        match = match and (state_condition_load == "*" or state_condition_load == load_status)

        if match:
            overall_state = f"{overall_state}, {state}"

    return overall_state

def generate_matrix():
    pass


if __name__ == "__main__":
    generate_matrix()

    print(get_solar_system_state("ABSENT", "HIGH", "NOON", "LOW", "SUNNY"))
    print(get_solar_system_state("ABSENT", "MEDIUM", "NOON", "LOW", "SUNNY"))
    print(get_solar_system_state("PRESENT", "MEDIUM", "NOON", "LOW", "SUNNY"))