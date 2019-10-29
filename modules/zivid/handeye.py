import _zivid


def detect_feature_points(point_cloud):
    _zivid.handeye.detect_feature_points(
        point_cloud
    )  # pylint: disable=protected-access


def calibrate_eye_in_hand(calibration_input):
    _zivid.handeye.calibrate_eye_in_hand(
        calibration_input
    )  # pylint: disable=protected-access


def calibrate_eye_to_hand(calibration_input):
    _zivid.handeye.calibrate_eye_to_hand(
        calibration_input
    )  # pylint: disable=protected-access


class Pose:
    def __init__(self, matrix):
        self.__impl = _zivid.handeye.Pose(matrix)
