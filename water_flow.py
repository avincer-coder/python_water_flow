def water_column_height(tower_height, tank_height):
    h = tower_height + (3 * tank_height) / 4
    return round(h,1)

def pressure_gain_from_water_height(height):
    water_density = 998.2
    gravity = 9.80665  
    pressure = (water_density * gravity * height) / 1000
    return round(pressure,3)

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    water_density = 998.2 
    pressure_loss = - (friction_factor * pipe_length * water_density * fluid_velocity**2) / (2000 * pipe_diameter)
    return round(pressure_loss,3)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    # Valores iniciales
    p = 998.2  # densidad del agua en kg/m^3
    # Fórmula para calcular la pérdida de presión debido a los fittings
    P = (-0.04 * p * fluid_velocity**2 * quantity_fittings) / 2000

    return(round(P,3))



























#----------------------------- CONTINUACION ----------------------------

# # print(pressure_loss_from_fittings(1.65,2))

def reynolds_number(hydraulic_diameter, fluid_velocity):
    # Constants
    density_water = 998.2  # in kg/m^3
    dynamic_viscosity_water = 0.0010016  # in Pa·s (kg/(m·s))

    # Calculate Reynolds number
    R = (density_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity_water
    
    return(round(R))
    
# def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
#     # Constants
#     density_water = 998.2  # in kg/m^3

#     # Formula for k
#     k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)

#     # Formula for pressure loss P
#     pressure_loss = (-k * density_water * fluid_velocity**2) / 2000  # in kilopascals

#     return round(pressure_loss,3)

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    # Constantes
    water_density = 998.2  # kg/m^3
    
    # Fórmula para calcular el valor de k
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    
    # Fórmula para calcular la pérdida de presión en kPa
    pressure_loss = - (k * water_density * fluid_velocity**2) / 2000
    return round(pressure_loss,3)



# # Example usage:
# larger_diameter = 0.28687  # in meters
# smaller_diameter = 	0.048692  # in meters
# fluid_velocity = 1.65  # in m/s
# reynolds_number_dos = 471729  # Example Reynolds number

# pressure_loss = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number_dos, smaller_diameter)
# print(f"Pressure loss: {pressure_loss} kPa")

# # COPY AND PASTE
# PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
# PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
# SUPPLY_VELOCITY = 1.65               # (meters / second)
# HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
# HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
# HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
# def main():
#     tower_height = float(input("Height of water tower (meters): "))
#     tank_height = float(input("Height of water tank walls (meters): "))
#     length1 = float(input("Length of supply pipe from tank to lot (meters): "))
#     quantity_angles = int(input("Number of 90° angles in supply pipe: "))
#     length2 = float(input("Length of pipe from supply to house (meters): "))
#     water_height = water_column_height(tower_height, tank_height)
#     pressure = pressure_gain_from_water_height(water_height)
#     diameter = PVC_SCHED80_INNER_DIAMETER
#     friction = PVC_SCHED80_FRICTION_FACTOR
#     velocity = SUPPLY_VELOCITY
#     reynolds = reynolds_number(diameter, velocity)
#     loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
#     pressure += loss
#     loss = pressure_loss_from_fittings(velocity, quantity_angles)
#     pressure += loss
#     loss = pressure_loss_from_pipe_reduction(diameter,
#             velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
#     pressure += loss
#     diameter = HDPE_SDR11_INNER_DIAMETER
#     friction = HDPE_SDR11_FRICTION_FACTOR
#     velocity = HOUSEHOLD_VELOCITY
#     loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
#     pressure += loss
#     print(f"Pressure at house: {pressure:.1f} kilopascals")
# if __name__ == "__main__":
#     main()



PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()