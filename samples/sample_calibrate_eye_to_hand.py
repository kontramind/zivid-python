"""Capture sample."""
import datetime
import zivid
import sys
import cv2


def _load_pose(index):
    fileName = f"/home/mathias/Downloads/martin_eth/pos{index+1:02}.yaml"
    print(f"Loading: {fileName}")
    file = cv2.FileStorage(fileName, cv2.FILE_STORAGE_READ)
    return zivid.handeye.Pose(file.getNode("PoseState").mat().transpose())


def _load_frame(index):
    fileName = f"/home/mathias/Downloads/martin_eth/img{index+1:02}.zdf"
    print(f"Loading: {fileName}")
    return zivid.handeye.detect_feature_points(zivid.Frame(fileName).get_point_cloud())


def _get_input(index):
    return (_load_pose(index), _load_frame(index))


def _main():
    app = zivid.Application()

    calibration = zivid.handeye.calibrate_eye_to_hand(
        list(_get_input(i) for i in range(int(sys.argv[1])))
    )

    print(calibration)


if __name__ == "__main__":
    _main()
