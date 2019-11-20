import _zivid


def detect_feature_points(point_cloud):
    return DetectionResult(
        _zivid.handeye.detect_feature_points(
            point_cloud._PointCloud__impl  # pylint: disable=protected-access
        )
    )


def calibrate_eye_in_hand(calibration_input):
    return _zivid.handeye.calibrate_eye_in_hand(calibration_input)


def calibrate_eye_to_hand(calibration_inputs):
    return _zivid.handeye.calibrate_eye_to_hand(
        [
            calib._CalibrationInput__impl  # pylint: disable=protected-access
            for calib in calibration_inputs
        ]
    )


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


class CalibrationInput:  # pylint: disable=too-few-public-methods
    def __init__(self, pose, detected_features):
        self.__impl = _zivid.handeye.CalibrationInput(
            pose._Pose__impl, detected_features._DetectionResult__impl
        )

    def __str__(self):
        return self.__impl.to_string()
