"""Contains hand-eye calibration functions and classes."""
import _zivid


def detect_feature_points(point_cloud):
    """Detect feature points from a calibration object in a point cloud.

    The functionality is to be exclusively used in combination with Zivid verified checkerboards.
    For further information please visit Zivid help page.

    Args:
        point_cloud: cloud from a frame containing an image of a calibration object

    Returns:
        Instance of DetectionResult

    """
    return DetectionResult(
        _zivid.handeye.detect_feature_points(
            point_cloud._PointCloud__impl  # pylint: disable=protected-access
        )
    )


def calibrate_eye_in_hand(calibration_inputs):
    """Perform eye-in-hand calibration.

    The procedure requires feature point sets acquired at the minimum from two poses.
    All the input poses have to be different. The feature point sets cannot be empty.
    All the feature point sets have to have same number of feature points.
    An exception will be thrown if the above requirements are not fulfilled.

    Args:
        calibration_inputs: a Sequence of CalibrationInput instances

    Returns:
        Instance of CalibrationOutput

    """
    return _zivid.handeye.calibrate_eye_in_hand(
        [
            calib._CalibrationInput__impl  # pylint: disable=protected-access
            for calib in calibration_inputs
        ]
    )


def calibrate_eye_to_hand(calibration_inputs):
    """Perform eye-to-hand calibration.

    The procedure requires feature point sets acquired at the minimum from two poses.
    All the input poses have to be different. The feature point sets cannot be empty.
    All the feature points have to have same number of elements.
    An exception will be thrown if the above requirements are not fulfilled.

    Args:
        calibration_inputs: a Sequence of CalibrationInput instances

    Returns:
        Instance of CalibrationOutput

    """
    return _zivid.handeye.calibrate_eye_to_hand(
        [
            calib._CalibrationInput__impl  # pylint: disable=protected-access
            for calib in calibration_inputs
        ]
    )


class Pose:  # pylint: disable=too-few-public-methods
    """Describes a robot pose."""

    def __init__(self, matrix):
        """Pose constructor taking a 4x4 transform.

        The constructor throws if the input transform does not describe pure rotation and translation.

        Args:
            matrix: a 4x4 numpy array

        """
        self.__impl = _zivid.handeye.Pose(matrix)

    def __str__(self):
        return self.__impl.to_string()


class DetectionResult:  # pylint: disable=too-few-public-methods
    """A result returned by the detect_feature_points(...) call."""

    def __init__(self, impl):
        """Initialize from internal DetectionResult.

        Args:
            impl: an internal DetectionResult Instance

        """
        self.__impl = impl

    def __str__(self):
        return self.__impl.to_string()


class CalibrationInput:  # pylint: disable=too-few-public-methods
    """Binds together a robot pose and the detection result acquired from the pose."""

    def __init__(self, pose, detected_features):
        """Binds together a robot pose and the detection result acquired from the pose.

        Args:
            pose: a robot pose
            detected_features: a DetectionResult instance

        """
        self.__impl = _zivid.handeye.CalibrationInput(
            pose._Pose__impl,  # pylint: disable=protected-access
            detected_features._DetectionResult__impl,  # pylint: disable=protected-access
        )

    def __str__(self):
        return self.__impl.to_string()
