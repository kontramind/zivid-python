#include <Zivid/CaptureAssistant.h>

#include <ZividPython/AmbientLightFrequency.h>
#include <ZividPython/Capture_Assistant.h>
#include <ZividPython/ReleasableCamera.h>
#include <ZividPython/SuggestSettingsParameters.h>
#include <ZividPython/Wrappers.h>

#include <pybind11/pybind11.h>

#include <chrono>
#include <vector>

namespace ZividPython::Capture_Assistant
{
    void wrapAsSubmodule(pybind11::module &dest)
    {
        using namespace Zivid::CaptureAssistant;

        ZIVID_PYTHON_WRAP_ENUM_CLASS(dest, AmbientLightFrequency);
        ZIVID_PYTHON_WRAP_CLASS(dest, SuggestSettingsParameters);

        dest.def("suggest_settings",
                 [](ReleasableCamera &camera,
                    const Zivid::CaptureAssistant::SuggestSettingsParameters &suggestSettingsParameters) {
                     return Zivid::CaptureAssistant::suggestSettings(camera.impl(), suggestSettingsParameters);
                 });
    }
} // namespace ZividPython::Capture_Assistant
