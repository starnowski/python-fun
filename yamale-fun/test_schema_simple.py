from yamale import YamaleTestCase
import os

class TestYaml(YamaleTestCase):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    schema = 'schemas/schema_simple.yaml'
    #yaml = 'data.yaml'
    # or
    # yaml = ['data/data_*.yaml']
    yaml = ['data/data_schema_simple.yaml']
    #yaml = ['data/data_schema_simple-invalid.yaml']


    def runTest(self):
        self.assertTrue(self.validate())