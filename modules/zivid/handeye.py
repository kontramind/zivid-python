import _zivid


def detect_feature_points(point_cloud):
    print(type(point_cloud))
    zivid_point = point_cloud._PointCloud__impl  # _zivid.PointCloud(point_cloud)
    return DetectionResult(_zivid.handeye.detect_feature_points(zivid_point))
    # return DetectionResult(_zivid.handeye.detect_feature_points(zivid_point))
    # return DetectionResult(
    #    _zivid.handeye.detect_feature_points(point_cloud._PointCloud__impl)
    # )


def calibrate_eye_in_hand(calibration_input):
    return _zivid.handeye.calibrate_eye_in_hand(calibration_input)


def calibrate_eye_to_hand(calibration_input):
    return _zivid.handeye.calibrate_eye_to_hand(
        [
            (pose._Pose__impl, detection_result._DetectionResult__impl)
            for [pose, detection_result] in calibration_input
        ]
    )  # pylint: disable=protected-access


class Pose:  # pylint: disable=too-few-public-methods
    def __init__(self, matrix):
        self.__impl = _zivid.handeye.Pose(matrix)

    def __str__(self):
        return self.__impl.to_string()


class DetectionResult:  # pylint: disable=too-few-public-methods
    def __init__(self, impl):
        self.__impl = impl

    def __str__(self):
        return self.__impl.to_string()

class CalibrationInput:
    def __init__(self, pose, detected_features):
        self.__impl = _zivid.handeye.CalibrationInput(pose, detected_features)

    def __str__(self):
        return self.__impl.to_string()