#!/usr/bin/env python

##
# Copyright (c) 2007-2008 Apple Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

#
# Runs the CalDAVTester test suite ensuring that required packages are available.
#

if __name__ == "__main__":

    import os
    import sys

    cwd = os.getcwd()
    sys.path.append(os.path.join(cwd, "src"))

    from src.browser import shell
    shell.runit()