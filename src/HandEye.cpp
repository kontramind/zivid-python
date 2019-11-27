#include <Zivid/HandEye/Calibrate.h>
#include <Zivid/HandEye/Detector.h>
#include <Zivid/HandEye/Pose.h>
#include <Zivid/PointCloud.h>

#include <ZividPython/Calibrate.h>
#include <ZividPython/Detector.h>
#include <ZividPython/Pose.h>
#include <ZividPython/ReleasablePointCloud.h>
#include <ZividPython/Wrappers.h>

#include <pybind11/pybind11.h>

#include <vector>

namespace ZividPython::HandEye
{
    void wrapAsSubmodule(pybind11::module &dest)
    {
        using namespace Zivid::HandEye;

        ZIVID_PYTHON_WRAP_CLASS_FULLPATH(dest, Pose, Zivid::HandEye::Pose);
        ZIVID_PYTHON_WRAP_CLASS_FULLPATH(dest, CalibrationOutput, Zivid::HandEye::CalibrationOutput);
        ZIVID_PYTHON_WRAP_CLASS_FULLPATH(dest, CalibrationInput, Zivid::HandEye::CalibrationInput);
        ZIVID_PYTHON_WRAP_CLASS_FULLPATH(dest, DetectionResult, Zivid::HandEye::DetectionResult);

        dest.def("detect_feature_points",
                 [](const ReleasablePointCloud &releasablePointCloud) {
                     return Zivid::HandEye::detectFeaturePoints(releasablePointCloud.impl());
                 })
            .def("calibrate_eye_in_hand",
                 [](const std::vector<CalibrationInput> &calibrationInputs) {
                     return Zivid::HandEye::calibrateEyeInHand(calibrationInputs);
                 })
            .def("calibrate_eye_to_hand", [](const std::vector<CalibrationInput> &calibrationInputs) {
                return Zivid::HandEye::calibrateEyeToHand(calibrationInputs);
            });
    }
} // namespace ZividPython::HandEye
