#include <Zivid/HandEye/Calibrate.h>
#include <Zivid/HandEye/Detector.h>
#include <Zivid/HandEye/Pose.h>
#include <Zivid/PointCloud.h>

#include <ZividPython/Calibrate.h>
#include <ZividPython/Detector.h>
#include <ZividPython/Pose.h>
#include <ZividPython/Wrappers.h>
#include <ZividPython/ReleasablePointCloud.h>

#include <pybind11/pybind11.h>

#include <vector>

namespace ZividPython::HandEye
{
    //namespace
    //{
    //    using PyCalibrationInputs = std::vector<std::pair<Zivid::HandEye::Pose, Zivid::HandEye::DetectionResult>>;
    //    using CppCalibrationInputs = std::vector<Zivid::HandEye::CalibrationInput>;
//
    //    CppCalibrationInputs transform(const PyCalibrationInputs &pyInputs)
    //    {
    //        CppCalibrationInputs cppInputs;
    //        cppInputs.reserve(pyInputs.size());
    //        std::transform(cbegin(pyInputs), cend(pyInputs), std::back_inserter(cppInputs), [](const auto &element) {
    //            const auto &[pose, detectionResult] = element;
    //            return Zivid::HandEye::CalibrationInput{ pose, detectionResult };
    //        });
    //        return cppInputs;
    //    }
    //} // namespace

    void wrapAsSubmodule(pybind11::module &dest)
    {
        using namespace Zivid::HandEye;

        //ZIVID_PYTHON_WRAP_CLASS(dest, Pose);
        ZIVID_PYTHON_WRAP_CLASS_TEST(dest, Pose, Zivid::HandEye::Pose);
        //ZIVID_PYTHON_WRAP_CLASS(dest, CalibrationOutput);
        ZIVID_PYTHON_WRAP_CLASS_TEST(dest, CalibrationOutput, Zivid::HandEye::CalibrationOutput);
        ZIVID_PYTHON_WRAP_CLASS_TEST(dest, CalibrationInput, Zivid::HandEye::CalibrationInput);
        //ZIVID_PYTHON_WRAP_CLASS(dest, DetectionResult);
        ZIVID_PYTHON_WRAP_CLASS_TEST(dest, DetectionResult, Zivid::HandEye::DetectionResult);
        

        dest.def("detect_feature_points", [](const ReleasablePointCloud &releasablePointCloud) {
                    return Zivid::HandEye::detectFeaturePoints(releasablePointCloud.impl());
                })
                .def("calibrate_eye_to_hand", [](const std::vector<CalibrationInput> &calibrationInputs) {
                    return Zivid::HandEye::calibrateEyeToHand(calibrationInputs);
            });
            //.def("calibrate_eye_in_hand",
            //     [](const PyCalibrationInputs &pyInputs) {
            //         return Zivid::HandEye::calibrateEyeInHand(transform(pyInputs));
            //     })
            //.def("calibrate_eye_to_hand", [](const CalibrationInput &calibrationInput) {
            //    return Zivid::HandEye::calibrateEyeToHand(calibrationInput);
            //});
            //.def("calibrate_eye_to_hand", [](const PyCalibrationInputs &pyInputs) {
            //    return Zivid::HandEye::calibrateEyeToHand(transform(pyInputs));
            //});
    }
} // namespace ZividPython::HandEye
