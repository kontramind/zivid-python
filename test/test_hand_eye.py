def test_init_pose(pose_file):
    import zivid
    import cv2

    file = cv2.FileStorage(pose_file, cv2.FILE_STORAGE_READ)
    pose_input = file.getNode("PoseState").mat().transpose()
    pose = zivid.handeye.Pose(pose_input)
    assert pose is not None
    assert isinstance(pose, zivid.handeye.Pose)


def test_detect_feature_points(point_cloud):
    import zivid

    feature_points = zivid.handeye.detect_feature_points(point_cloud)

    assert feature_points is not None
    assert isinstance(feature_points, zivid.handeye.DetectionResult)


def test_calibrate_eye_to_hand(feature_points_and_poses):
    calibration = zivid.handeye.calibrate_eye_to_hand(feature_points_and_poses)
    assert calibration is not None
    assert isinstance(calibration, int)  # TODO fix this


def test_calibrate_hand_in_eye(feature_points_and_poses):
    calibration = zivid.handeye.calibrate_hand_in_eye(feature_points_and_poses)
    assert calibration is not None
    assert isinstance(calibration, int)  # TODO fix this
