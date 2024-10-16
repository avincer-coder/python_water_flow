# def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
#     # Valores iniciales
#     p = 998.2  # densidad del agua en kg/m^3
#     # Fórmula para calcular la pérdida de presión debido a los fittings
#     P = (-0.04 * p * fluid_velocity**2 * quantity_fittings) / 2000

#     return(round(P,3))
    

# # print(pressure_loss_from_fittings(1.65,2))

# def reynolds_number(hydraulic_diameter, fluid_velocity):
#     # Constants
#     density_water = 998.2  # in kg/m^3
#     dynamic_viscosity_water = 0.0010016  # in Pa·s (kg/(m·s))

#     # Calculate Reynolds number
#     R = (density_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity_water
    
#     return(round(R))
    
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    # Constants
    density_water = 998.2  # in kg/m^3

    # Formula for k
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)

    # Formula for pressure loss P
    pressure_loss = (-k * density_water * fluid_velocity**2) / 2000  # in kilopascals

    return pressure_loss

# Example usage:
larger_diameter = 0.28687  # in meters
smaller_diameter = 	0.048692  # in meters
fluid_velocity = 1.65  # in m/s
reynolds_number_dos = 471729  # Example Reynolds number

pressure_loss = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number_dos, smaller_diameter)
print(f"Pressure loss: {pressure_loss} kPa")