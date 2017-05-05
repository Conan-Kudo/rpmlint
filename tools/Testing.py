# -*- coding: utf-8 -*-

import glob
import os
import tempfile

import Pkg


def _testpath():
    return os.environ.get(
        'TESTPATH',
        os.path.join(os.path.dirname(__file__), "..", "test")
    )


TEST_CONFIG = os.path.join(_testpath(), "test.config")
with open(TEST_CONFIG) as f:
    exec(compile(f.read(), TEST_CONFIG, 'exec'))

currently_testing = 0
output = []


def isTest():
    return currently_testing


def startTest():
    global currently_testing
    global output
    output = []
    currently_testing = 1


def addOutput(s):
    global output
    output.append(s)


def getOutput():
    global output
    return output


def getTestedPackage(name):
    pkg_path = glob.glob(os.path.join(_testpath(), name) + "-*.rpm")[0]
    return Pkg.Pkg(pkg_path, tempfile.gettempdir())


def getTestedSpecPackage(name):
    pkg_path = glob.glob(os.path.join(_testpath(), name) + ".spec")[0]
    return Pkg.FakePkg(pkg_path)


class OutputTest(object):

    check = None
    check_spec = None

    def _rpm_test_output(self, rpm, check=None):
        with getTestedPackage(rpm) as pkg:
            startTest()
            (check or self.check)(pkg)
            return getOutput()

    def _spec_test_output(self, spec, check=None):
        with getTestedSpecPackage(spec) as pkg:
            startTest()
            # call check_spec() directly, as check() doesn't work with
            # getTestedSpecPackage()
            (check or self.check_spec)(pkg, pkg.name)
            return getOutput()
