"""Capture sample."""
import sys
import cv2
import zivid


def _load_pose(index):
    file_name = f"/home/mathias/Downloads/martin_eth/pos{index+1:02}.yaml"
    print(f"Loading: {file_name}")
    pose_file = cv2.FileStorage(file_name, cv2.FILE_STORAGE_READ)
    return zivid.handeye.Pose(pose_file.getNode("PoseState").mat().transpose())


def _load_frame(index):
    file_name = f"/home/mathias/Downloads/martin_eth/img{index+1:02}.zdf"
    print(f"Loading: {file_name}")
    return zivid.handeye.detect_feature_points(zivid.Frame(file_name).get_point_cloud())


def _get_input(index):
    return (_load_pose(index), _load_frame(index))


def _main():
    app = zivid.Application()  # pylint: disable=unused-variable

    calibration = zivid.handeye.calibrate_eye_to_hand(
        list(_get_input(i) for i in range(int(sys.argv[1])))
    )

    print(calibration)


if __name__ == "__main__":
    _main()
