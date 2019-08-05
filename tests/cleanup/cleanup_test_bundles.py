#!/usr/bin/env python3
import os
import sys
import unittest

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # noqa
sys.path.insert(0, pkg_root)  # noqa

from data_store_agent import DataStoreAgent

class CleanupTestBundles(unittest.TestCase):
    test_bundle_query = {
        "query": {
            "prefix": {
                "files.project_json.project_core.project_short_name": "prod/"
            }
        }
    }

    def setUp(self):
        self.data_store = DataStoreAgent(deployment="prod")

    def test_find_test_bundles(self):
        for fqid in self._test_bundles():
            print(fqid)

    def test_tombstone_test_bundles(self):
        for fqid in self._test_bundles():
            uuid, version = fqid.split(".", 1)
            print("Tombstoning bundle", uuid, version)
            self.data_store.tombstone_bundle(uuid)

    def _test_bundles(self):
        for hit in self.data_store.search_iterate(self.test_bundle_query):
            yield hit['bundle_fqid']


if __name__ == '__main__':
    unittest.main()
