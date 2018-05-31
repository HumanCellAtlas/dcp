import os
import unittest

from ..dataset_fixture import DatasetFixture
from ..dataset_runner import DatasetRunner


class TestBigBundles(unittest.TestCase):

    def test_one_submission_with_100_bundles(self):
        print("")
        dataset = DatasetFixture('gliob_100')
        runner = DatasetRunner(deployment=os.environ['TRAVIS_BRANCH'])
        runner.run(dataset_fixture=dataset)

    def test_one_submission_with_1000_bundles(self):
        print("")
        dataset = DatasetFixture('gliob_1000')
        runner = DatasetRunner(deployment=os.environ['TRAVIS_BRANCH'])
        runner.run(dataset_fixture=dataset)
