#!/bin/bash


#
#    Copyright (c) 2016-2017 Nest Labs, Inc.
#    All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

#
#    @file
#       Sample code for manually running happy WdmNext tests
#
# Enable case and make tests hit frontdoor
# generate case certificate
# python device-mfg/weave-provisioning-tool/weave-provisioning-tool.py  export-key-files --db 'weave-certificates/simulator-weave-provisioning-db.sqlite'  --outdir /tmp/ --start 18B430AA00000010  --end 18B430AA0000001A

export CASE=1
export USE_SERVICE_DIR=1
export weave_service_address='frontdoor.lt3.nestlabs.com'
export happy_dns='8.8.8.8 172.16.255.1 172.16.255.153 172.16.255.53'
# export RESOURCE_IDS='gsrbr1'
# exit if something fails
set -e

# By default, run a mutual subscription test. If tests have been
# listed as arguments, run those instead

# pairing/test_weave_pairing_01.py
# echo/test_weave_echo_02.py
# wdmNext/test_weave_wdm_next_service_mutual_subscribe_01.py
# wdmNext/test_weave_wdm_next_service_update_*

if [[ $# -eq 0 ]]
then
    #wdmNext/test_weave_wdm_next_service_mutual_subscribe_01.py
else
    for test_to_run in $* ; do python $test_to_run ;  done
fi

echo All tests have run
