from pkgutil import iter_modules
import sys
import subprocess

# To be replaced by: from setuptools_scm import get_version
def get_version():
    return "0.9.1"


def _zivid_sdk_version():
    return "1.6.0"


def _zivid_python_version():
    scm_version = get_version()

    if "+" in scm_version:
        base_version, scm_metadata = scm_version.split("+", 1)
    else:
        base_version = scm_version
        scm_metadata = None

    base_version = "{}.{}".format(base_version, _zivid_sdk_version())

    if scm_metadata:
        version = "{}+{}".format(base_version, scm_metadata)
    else:
        version = base_version

    return version


def _check_dependency(module_name, package_hint=None):
    if module_name not in [module[1] for module in iter_modules()]:
        raise ImportError(
            "Missing module '{}'. Please install '{}' manually or use PIP>=19 to handle build dependencies automatically (PEP 517).".format(
                module_name, package_hint
            )
        )


def _run_process(args):
    sys.stdout.flush()
    try:
        process = subprocess.Popen(args)
        exit_code = process.wait()
        if exit_code != 0:
            raise RuntimeError("Wait failed with exit code {}".format(exit_code))
    except Exception as ex:
        raise type(ex)("Process failed: '{}'.".format(" ".join(args))) from ex
    finally:
        sys.stdout.flush()


def _install_conan():
    _run_process(("pip3", "install", "conan"))


def _main():
    # This list is a duplicate of the build-system requirements in pyproject.toml.
    # The purpose of these checks is to help users with PIP<19 lacking support for
    # pyproject.toml
    # Keep the two lists in sync
    _check_dependency("skbuild", "scikit-build")
    _check_dependency("cmake")
    _check_dependency("ninja")
    print(
        "all modules: {}".format("\n".join([module[1] for module in iter_modules()])),
        flush=True,
    )
    #_install_conan()
    print(
        "all modules: {}".format("\n".join([module[1] for module in iter_modules()])),
        flush=True,
    )
    _check_dependency("conan")

    from skbuild import setup

    setup(
        name="zivid",
        version=_zivid_python_version(),
        description="Defining the Future of 3D Machine Vision",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        url="https://www.zivid.com",
        author="Zivid AS",
        author_email="support@zivid.com",
        license="BSD 3-Clause",
        packages=["zivid", "_zivid"],
        package_dir={"": "modules"},
        install_requires=["numpy", "conan"],
        cmake_args=[
            "-DZIVID_PYTHON_VERSION=" + _zivid_python_version(),
            "-DZIVID_SDK_VERSION=" + _zivid_sdk_version(),
            "-Dpybind11_DIR=src/3rd-party/pybind11-2.2.4/share/cmake/pybind11/",
            # "-B_builds",
            # "-DHUNTER_STATUS_DEBUG=ON",
            # "-DCMAKE_BUILD_TYPE=Release",
            # "-DEigen3_DIR=/host/zivid-python-dependencies/eigen-eigen-323c052e1731/cmake/",
            # "-DCMAKE_PREFIX_PATH=/host/zivid-python-dependencies/eigen-eigen-323c052e1731/cmake/",
            # "-DCMAKE_MODULE_PATH=/host/zivid-python-dependencies/eigen-eigen-323c052e1731/cmake/",
        ],
        classifiers=[
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Scientific/Engineering",
        ],
    )


if __name__ == "__main__":
    _main()
