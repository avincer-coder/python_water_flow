from water_flow import pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
import pytest

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

def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == 0
    assert reynolds_number(0.048692, 1.65) == 80069
    assert reynolds_number(0.048692, 1.75) == 84922
    assert reynolds_number(0.286870, 1.65) == 471729
    assert reynolds_number(0.286870, 1.75) == 500318

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == 0.000
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == -163.744
    # assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == -184.182