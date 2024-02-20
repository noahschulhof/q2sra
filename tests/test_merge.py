import unittest
import os
from q2sra.merge_metadata import merge_metadata
from q2sra.merge_repseqs import merge_repseqs
from q2sra.merge_tables import merge_tables

class MergeTest(unittest.TestCase):
    def setUp(self):
        os.chdir('tests')


    def tearDown(self):
        os.remove('sample_proj/sample_proj_table_merged.qza')
        os.remove('sample_proj/sample_proj_repseqs_merged.qza')

    
    def test_merge(self):
        merge_tables('sample_proj')
        merge_repseqs('sample_proj')

        assert os.path.exists('sample_proj/sample_proj_table_merged.qza')
        assert os.path.exists('sample_proj/sample_proj_repseqs_merged.qza')

        

if __name__ == '__main__':
    unittest.main()