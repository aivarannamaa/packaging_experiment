#!/usr/bin/env bash
set -e

VER="0.6"
NAME_VER="mp_packaging_experiment-${VER}"

rm -rf build

# create regular py3 wheel
python3 setup.py bdist_wheel -d dist

# create micropython wheels
cd dist
tags="micropython1"

for tag in $tags; do
  echo "Building wheel for $tag ..."
  python3 -m wheel unpack ${NAME_VER}-py3-none-any.whl

  # tag-specific post-processing
  sed -i "s/<TAG>/${tag}/" "${NAME_VER}/packaging_experiment.py"
  sed -i "s/py3-none-any/${tag}-none-any/" "${NAME_VER}/${NAME_VER}.dist-info/WHEEL"

  # create specific wheel
  python3 -m wheel pack ${NAME_VER}

done


