import unittest

from deploy_static_to_public import *

class TestDeployStaticToPublic(unittest.TestCase):

    def test_deploy_static_to_public(self):
        deploy_static_to_public()

if __name__ == "__main__":
	unittest.main()