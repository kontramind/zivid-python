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


def calibrate_eye_to_hand(calibration_inputs):
    print(calibration_inputs)
    [print(calib) for calib in calibration_inputs]
    return _zivid.handeye.calibrate_eye_to_hand(
        [calib._CalibrationInput__impl for calib in calibration_inputs]
    )
    # return _zivid.handeye.calibrate_eye_to_hand(
    #    [
    #        (pose._Pose__impl, detection_result._DetectionResult__impl)
    #        for [pose, detection_result] in calibration_input
    #    ]
    # )  # pylint: disable=protected-access


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
        print(f"detected features: type: {type(detected_features)}")
        self.__impl = _zivid.handeye.CalibrationInput(
            pose._Pose__impl, detected_features._DetectionResult__impl
        )
        print(self.__impl)
        print(self.__impl.to_string())

    def __str__(self):
        return self.__impl.to_string()
