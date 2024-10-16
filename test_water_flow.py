from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction

def test_water_column_height():
    assert water_column_height(0.0, 0.0) == 0
    assert water_column_height(0.0, 10.0) == 7.5
    assert water_column_height(25.0, 0.0) == 25.0
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == 0.000
    assert pressure_gain_from_water_height(30.2) == 295.628
    assert pressure_gain_from_water_height(50.0) == 489.450

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == 0.000
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == 0.000
    assert pressure_loss_from_pipe(0.048692, 200.00	, 0.018, 0.00) == 0.000
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == -113.008
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == -100.462	
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == -61.576
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == -110.884

pytest.main(["-v", "--tb=line", "-rN", __file__])

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0,3) == 0.000
    assert pressure_loss_from_fittings(1.65,0) == 0.000
    assert pressure_loss_from_fittings(1.65,2) == -0.109
    assert pressure_loss_from_fittings(1.75,2) == -0.122
    assert pressure_loss_from_fittings(1.75,5) == -0.306

def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == 0
    assert reynolds_number(0.048692, 1.65) == 80069
    assert reynolds_number(0.048692, 1.75) == 84922
    assert reynolds_number(0.286870, 1.65) == 471729
    assert reynolds_number(0.286870, 1.75) == 500318

# def test_pressure_loss_from_pipe_reduction():
#     assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == 0.000
#     assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == -163.744
#     # assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == -184.182

def test_pressure_loss_from_pipe_reduction():
    # Usamos approx para manejar las diferencias de precisión flotante
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == 0.0
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == pytest.approx(-163.744, rel=1e-3)