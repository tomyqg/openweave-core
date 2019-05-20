#!/usr/bin/env python


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
#       Calls Weave WDM one way subscribe between nodes.
#       C08: One way Subscribe: Root path. Null Version. Mutate data in publisher. Publisher aborts
#

import unittest
import set_test_path
from weave_wdm_next_test_base import weave_wdm_next_test_base
import WeaveUtilities


class test_weave_wdm_next_one_way_subscribe_12(weave_wdm_next_test_base):

    def test_weave_wdm_next_one_way_subscribe_12(self):
        wdm_next_args = {}

        wdm_next_args['wdm_option'] = "one_way_subscribe"
        wdm_next_args['total_client_count'] = 0
        wdm_next_args['final_client_status'] = 4
        wdm_next_args['timer_client_period'] = 0
        #TODO: use json file to track iteration for each test case iteration.
        self.test_client_iterations = 1
        count = self.test_client_iterations
        wdm_next_args['test_client_delay'] = 15000
        wdm_next_args['enable_client_flip'] = 0

        wdm_next_args['total_server_count'] = 2
        wdm_next_args['final_server_status'] = 3
        wdm_next_args['timer_server_period'] = 5000
        wdm_next_args['enable_server_flip'] = 1

        wdm_next_args['client_log_check'] = [('Client\[0\] \[(ALIVE|CONFM)\] HandleSubscriptionTerminated Ref\(\d+\)', count),
                                             ('Client->kEvent_OnNotificationProcessed', count * wdm_next_args['total_server_count'] + 1),
                                             ('Client\[0\] moving to \[ FREE\] Ref\(0\)', count)]
        wdm_next_args['server_log_check'] = [('Handler\[0\] \[(ALIVE|CONFM)\] AbortSubscription Ref\(\d+\)', count),
                                             ('Handler\[0\] Moving to \[ FREE\] Ref\(0\)', count)]
        wdm_next_args['test_tag'] = self.__class__.__name__[19:].upper()
        wdm_next_args['test_case_name'] = ['C08: One way Subscribe: Root path. Null Version. Mutate data in publisher. Publisher aborts']
        print 'test file: ' + self.__class__.__name__
        super(test_weave_wdm_next_one_way_subscribe_12, self).weave_wdm_next_test_base(wdm_next_args)

if __name__ == "__main__":
    WeaveUtilities.run_unittest()

