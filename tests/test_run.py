import unittest
import shutil
import os
import sys

sys.path.append('q2sra')
from q2sra.proj import Proj

class RunTest(unittest.TestCase):
    def setUp(self):
        self.p = Proj('test_proj')
    

    def tearDown(self):
        shutil.rmtree('test_proj')
    

    def test_paired(self):
        self.p.run('zhang', 'PRJNA516815', use_deblur = False)
        self.assertEqual(len(os.listdir('zhang/fastq-files')), 44)
        assert os.path.exists('zhang/zhang_table.qza')
        assert os.path.exists('zhang/zhang_repseqs.qza')
        
        self.p.run('arizza', 'PRJNA481425')
        self.assertEqual(len(os.listdir('arizza/fastq-files')), 36)
        assert os.path.exists('arizza/arizza_table.qza')
        assert os.path.exists('arizza/arizza_repseqs.qza')
    

    def test_single(self):
        self.p.paired = False
        self.nsamples = 8

        self.p.run('zhang', 'PRJNA516815')
        self.assertEqual(len(os.listdir('zhang/fastq-files')), 8)
        assert os.path.exists('zhang/zhang_table.qza')
        assert os.path.exists('zhang/zhang_repseqs.qza')
        
        self.p.run('arizza', 'PRJNA481425', use_deblur = False)
        self.assertEqual(len(os.listdir('arizza/fastq-files')), 8)
        assert os.path.exists('arizza/arizza_table.qza')
        assert os.path.exists('arizza/arizza_repseqs.qza')



if __name__ == '__main__':
    unittest.main()