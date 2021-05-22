An experiment for creating and using dedicated wheels for MicroPython 
=====================================================================

The result is here: https://pypi.org/project/mp-packaging-experiment/#files

Can be installed with

::

  pip3 install --target=temp_dir mp_packaging_experiment --implementation=micropython --python-version=1 --only-binary=:all:

Note that micropython1 gets split into two arguments: ``--implementation=micropython`` and ``--python-version=1`` (https://discuss.python.org/t/how-does-implementation-option-of-pip-install-work/8830).

The argument ``--only-binary=:all:`` is required by ``pip`` whenever ``--implementation`` or ``--python-version`` is used. This means all dependencies must also have wheels with same Python version tag.

I imagine the more general tag ``micropython1`` could be used for uncompiled packages (ie containing py-scripts) and ``micropython115`` etc could be used for compiled packages (ie. containing mpy files).

I didn't find good means for specifying arbitrary python tag while building the wheel (I guess you are supposed to build a wheel on the same platform the wheel is for). So I created a regular py3 wheel, unpacked it, made changes in the content and metadata and then repacked it -- see create_dist.sh
