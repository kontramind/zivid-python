# """Capture sample."""
# import sys
# import cv2
# import zivid
#
#
# def _load_pose(index):
#     file_name = f"/home/mathias/Downloads/martin_eth/pos{index+1:02}.yaml"
#     print(f"Loading: {file_name}")
#     pose_file = cv2.FileStorage(file_name, cv2.FILE_STORAGE_READ)
#     return zivid.handeye.Pose(pose_file.getNode("PoseState").mat().transpose())
#
#
# def _load_frame(index):
#     file_name = f"/home/mathias/Downloads/martin_eth/img{index+1:02}.zdf"
#     print(f"Loading: {file_name}")
#     return zivid.handeye.detect_feature_points(zivid.Frame(file_name).get_point_cloud())
#
#
# def _get_input(index):
#     return (_load_pose(index), _load_frame(index))
#
#
# def _main():
#     app = zivid.Application()  # pylint: disable=unused-variable
#
#     calibration = zivid.handeye.calibrate_eye_to_hand(
#         list(_get_input(i) for i in range(int(sys.argv[1])))
#     )
#
#     print(calibration)
#
#
# if __name__ == "__main__":
#     _main()


import zivid.handeye
import datetime
import numpy as np


def acquire_checkerboard_frame(camera):
    print("Capturing checkerboard image... ")
    with camera.update_settings() as updater:
        updater.settings.iris = 17
        updater.settings.gain = 1.0
        updater.settings.exposure_time = datetime.timedelta(microseconds=20000)
        updater.settings.filters.gaussian.enabled = True
    print("OK")
    return camera.capture()


def enter_robot_pose(index):
    inputted = input(
        "Enter pose with id={} (a line with 16 space separated values describing 4x4 row-major matrix):".format(
            index
        )
    )
    print(inputted)
    elements = inputted.split(maxsplit=15)
    data = np.array(elements, dtype=np.float64).reshape((4, 4))
    robot_pose = zivid.handeye.Pose(data)
    print("The following pose was entered:\n{}".format(robot_pose))
    return robot_pose


def _main():
    app = zivid.Application()
    camera = app.connect_camera()

    current_pose_id = 0
    calibration_input = list()
    calibrate = False

    while not calibrate:
        command = input(
            "Enter command, p (to add robot pose) or c (to perform calibration):"
        ).strip()
        if command == "p":
            try:
                robot_pose = enter_robot_pose(current_pose_id)

                frame = acquire_checkerboard_frame(camera)

                print("Detecting checkerboard square centers... ")

                result = zivid.handeye.detect_feature_points(frame.get_point_cloud())
                print(result)
                print(type(result))
                if result:
                    print("OK")
                    res = zivid.handeye.CalibrationInput(robot_pose, result)
                    calibration_input.append((robot_pose, res))
                    current_pose_id += 1
                else:
                    print("FAILED")
            except Exception as ex:
                # print(ex)
                raise ex
        elif command == "c":
            calibrate = True
        else:
            print("Unknown command '{}'".format(command))

    print("Performing hand-eye calibration...")
    calibration_result = zivid.handeye.calibrate_eye_to_hand(calibration_input)
    if calibration_result:
        print("OK")
        print("Result:\n{}".format(calibration_result))
    else:
        print("FAILED")


if __name__ == "__main__":
    _main()
