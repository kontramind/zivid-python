import _zivid


def calibrate_eye_in_hand(calibration_input):
    _zivid.firmware.calibrate_eye_in_hand(
        calibration_input
    )  # pylint: disable=protected-access


def calibrate_hand_in_eye(calibration_input):
    _zivid.firmware.calibrate_hand_in_eye(
        calibration_input
    )  # pylint: disable=protected-access
