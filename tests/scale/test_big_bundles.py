import os
import unittest

from ..dataset_fixture import DatasetFixture
from ..dataset_runner import DatasetRunner


class TestBigBundles(unittest.TestCase):

    def test_one_submission_with_100_bundles(self):
        self._run(fixture_name='gliob_100')

    def test_one_submission_with_1000_bundles(self):
        self._run(fixture_name='gliob_1000')

    def _run(self, fixture_name):
        print("")
        dataset = DatasetFixture(fixture_name, deployment=os.environ['TRAVIS_BRANCH'])
        runner = DatasetRunner(deployment=os.environ['TRAVIS_BRANCH'])
        runner.run(dataset_fixture=dataset, run_name_prefix="scale")
