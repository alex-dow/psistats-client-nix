#!/bin/bash
rm -rf /psikon/python/envs/psistats-client-nix
virtualenv --system-site-packages /psikon/python/envs/psistats-client-nix
source /psikon/python/envs/psistats-client-nix/bin/activate
pip install -r $WORKSPACE/requirements.txt
pip install pylint

PYTHONPATH=$WORKSPACE:$PYTHONPATH

pylint -f parseable $WORKSPACE/ | tee pylint.out
/usr/bin/slocccount --duplicates --wide --details $WORKSPACE > sloccount.sc

cd $WORKSPACE
/psikon/sonar-runner/bin/sonar-runner
