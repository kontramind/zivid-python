import _zivid


def detect_feature_points(point_cloud):
    return DetectionResult(
        _zivid.handeye.detect_feature_points(_zivid.PointCloud(point_cloud))
    )  # pylint: disable=protected-access


def calibrate_eye_in_hand(calibration_input):
    return _zivid.handeye.calibrate_eye_in_hand(
        calibration_input
    )  # pylint: disable=protected-access


def calibrate_eye_to_hand(calibration_input):
    return _zivid.handeye.calibrate_eye_to_hand(
        [
            (pose._Pose__impl, detection_result._DetectionResult__impl)
            for [pose, detection_result] in calibration_input
        ]
    )  # pylint: disable=protected-access


class Pose:
    def __init__(self, matrix):
        self.__impl = _zivid.handeye.Pose(matrix)


class DetectionResult:
    def __init__(self, impl):
        self.__impl = impl
