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
#       C03: One way Subscribe: Root path. Null Version. Mutate data in Publisher. Client cancels
#       L05: Stress One way Subscribe: Root path. Null Version. Mutate data in Publisher. Client cancels
#

import unittest
import set_test_path
from weave_wdm_next_test_base import weave_wdm_next_test_base
import WeaveUtilities


class test_weave_wdm_next_one_way_subscribe_05(weave_wdm_next_test_base):

    def test_weave_wdm_next_one_way_subscribe_05(self):
        wdm_next_args = {}

        wdm_next_args['wdm_option'] = "one_way_subscribe"

        wdm_next_args['total_client_count'] = 2
        wdm_next_args['final_client_status'] = 0
        wdm_next_args['timer_client_period'] = 5000
        count = self.test_client_iterations
        wdm_next_args['test_client_delay'] = 2000
        wdm_next_args['enable_client_flip'] = 0

        wdm_next_args['total_server_count'] = 2
        wdm_next_args['final_server_status'] = 4
        wdm_next_args['timer_server_period'] = 4000
        wdm_next_args['enable_server_flip'] = 1

        wdm_next_args['client_clear_state_between_iterations'] = True
        wdm_next_args['server_clear_state_between_iterations'] = True

        wdm_next_args['client_log_check'] = [('Client\[0\] \[(ALIVE|CONFM)\] EndSubscription Ref\(\d+\)', count * 1),
                                             ('Client->kEvent_OnNotificationProcessed', count * (wdm_next_args['total_server_count'] + 1)),
                                             ('Client\[0\] moving to \[ FREE\] Ref\(0\)', count * 1)]
        wdm_next_args['server_log_check'] = [('Handler\[0\] \[(ALIVE|CONFM)\] CancelRequestHandler Ref\(\d+\)', count * 1),
                                             ('Handler\[0\] Moving to \[ FREE\] Ref\(0\)', count * 1)]
        wdm_next_args['test_tag'] = self.__class__.__name__[19:].upper()
        wdm_next_args['test_case_name'] = ['L05: Stress One way Subscribe: Root path, Null Version. Mutate data in Publisher. Client cancels']
        print 'test file: ' + self.__class__.__name__
        print "weave-wdm-next test C03 and L05"
        super(test_weave_wdm_next_one_way_subscribe_05, self).weave_wdm_next_test_base(wdm_next_args)


if __name__ == "__main__":
    WeaveUtilities.run_unittest()

