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
        self.p.run('zhang', 'PRJNA516815')
        self.assertEqual(len(os.listdir('test_proj/zhang/fastq-files')), 44)
        assert os.path.exists('test_proj/zhang/zhang_table.qza')
        assert os.path.exists('test_proj/zhang/zhang_repseqs.qza')
        
        self.p.run('murphy', 'PRJNA504404')
        self.assertEqual(len(os.listdir('test_proj/murphy/fastq-files')), 18)
        assert os.path.exists('test_proj/murphy/murphy_table.qza')
        assert os.path.exists('test_proj/murphy/murphy_repseqs.qza')

        self.p.run('wu', 'PRJNA847054')
        self.assertEqual(len(os.listdir('test_proj/wu/fastq-files')), 6)
        assert os.path.exists('test_proj/wu/wu_table.qza')
        assert os.path.exists('test_proj/wu/wu_repseqs.qza')
    

    def test_single(self):
        self.p.paired = False
        self.nsamples = 8

        self.p.run('zhang', 'PRJNA516815')
        self.assertEqual(len(os.listdir('test_proj/zhang/fastq-files')), 22)
        assert os.path.exists('test_proj/zhang/zhang_table.qza')
        assert os.path.exists('test_proj/zhang/zhang_repseqs.qza')
        
        self.p.run('murphy', 'PRJNA504404')
        self.assertEqual(len(os.listdir('test_proj/murphy/fastq-files')), 9)
        assert os.path.exists('test_proj/murphy/murphy_table.qza')
        assert os.path.exists('test_proj/murphy/murphy_repseqs.qza')

        self.p.run('wu', 'PRJNA847054')
        self.assertEqual(len(os.listdir('test_proj/wu/fastq-files')), 12)
        assert os.path.exists('test_proj/wu/wu_table.qza')
        assert os.path.exists('test_proj/wu/wu_repseqs.qza')



if __name__ == '__main__':
    unittest.main()