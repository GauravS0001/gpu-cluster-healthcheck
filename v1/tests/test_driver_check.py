from gpucheck.checks.driver_check import DriverCheck


def test_driver_check():

    check = DriverCheck()

    result = check.run()

    assert result.name == "NVIDIA Driver Check"