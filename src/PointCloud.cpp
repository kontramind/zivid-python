#include <Zivid/Frame.h>
#include <ZividPython/PointCloud.h>

#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>

#include <stdexcept>

namespace py = pybind11;

#define IS_SAME_MEMBER(T1, T2, m)                                                                                      \
    (std::is_same_v<decltype(T1::m), decltype(T2::m)> && offsetof(T1, m) == offsetof(T2, m))

namespace
{
    auto toPointCloudSize(const py::buffer_info &info)
    {
        if(info.ndim != 2)
        {
            throw std::runtime_error("Point cloud dimension must be 2");
        }

        const auto rows = info.shape[0];
        const auto cols = info.shape[1];

        if(rows < 0 || cols < 0)
        {
            throw std::out_of_range{ "Invalid point cloud size [" + std::to_string(rows) + "," + std::to_string(cols)
                                     + "]" };
        }

        return std::make_pair(static_cast<size_t>(rows), static_cast<size_t>(cols));
    }

#pragma pack(push)
    struct DataType
    {
        float x, y, z;
        float contrast;
        uint8_t b, g, r, a;
    };
#pragma pack(pop)

    py::buffer_info makeBufferInfo(Zivid::PointCloud &pointCloud)
    {
        const auto data = pointCloud.dataPtr();

        using NativeDataType = std::remove_pointer_t<decltype(data)>;

        static_assert(sizeof(NativeDataType) == sizeof(DataType), "Unexpected point cloud format");
        static_assert(IS_SAME_MEMBER(NativeDataType, DataType, x), "Unexpected point cloud format");
        static_assert(IS_SAME_MEMBER(NativeDataType, DataType, y), "Unexpected point cloud format");
        static_assert(IS_SAME_MEMBER(NativeDataType, DataType, z), "Unexpected point cloud format");
        static_assert(IS_SAME_MEMBER(NativeDataType, DataType, contrast), "Unexpected point cloud format");
        static_assert(offsetof(NativeDataType, rgba) == offsetof(DataType, b), "Unexpected point cloud format");
        static_assert(sizeof(NativeDataType::rgba)
                          == sizeof(DataType::r) + sizeof(DataType::g) + sizeof(DataType::b) + sizeof(DataType::a),
                      "Unexpected point cloud format");

        return py::buffer_info{ data,
                                sizeof(DataType),
                                py::format_descriptor<DataType>::format(),
                                2,
                                { pointCloud.height(), pointCloud.width() },
                                { sizeof(DataType) * pointCloud.width(), sizeof(DataType) } };
    }

    void copyFromBuffer(Zivid::PointCloud &dest, py::array_t<DataType> source)
    {
        const py::buffer_info info = source.request();

        const auto [rows, cols] = toPointCloudSize(info);

        // TODO: Make this work and delete line below
        // dest.resize(rows, cols);
        dest = Zivid::PointCloud{ rows, cols };

        memcpy(dest.dataPtr(), static_cast<DataType *>(info.ptr), sizeof(DataType) * dest.size());
    }
} // namespace

namespace ZividPython
{
    void wrapClass(pybind11::class_<Zivid::PointCloud> pyClass)
    {
        PYBIND11_NUMPY_DTYPE(DataType, x, y, z, contrast, b, g, r, a);

        pyClass.def(py::init()).def_buffer(makeBufferInfo).def("__init__", copyFromBuffer);
    }
} // namespace ZividPython
