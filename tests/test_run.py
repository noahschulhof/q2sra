import unittest
import shutil
import os
from q2sra.proj import Proj

class RunTest(unittest.TestCase):
    def setUp(self):
        self.p = Proj('test_proj')
    

    def tearDown(self):
        shutil.rmtree('test_proj')
    

    def test_paired(self):
        self.p.run('chang', 'PRJNA601807')
        self.assertEqual(len(os.listdir('chang/fastq-files')), 20)
        assert os.path.exists('chang/chang_deblur.qza')
        assert os.path.exists('chang/chang_repseqs.qza')
        
        self.p.run('arizza', 'PRJNA481425')
        self.assertEqual(len(os.listdir('arizza/fastq-files')), 36)
        assert os.path.exists('arizza/arizza_deblur.qza')
        assert os.path.exists('arizza/arizza_repseqs.qza')
    

    def test_single(self):
        self.p.paired = False
        self.nsamples = 8

        self.p.run('chang', 'PRJNA601807')
        self.assertEqual(len(os.listdir('chang/fastq-files')), 8)
        assert os.path.exists('chang/chang_deblur.qza')
        assert os.path.exists('chang/chang_repseqs.qza')
        
        self.p.run('arizza', 'PRJNA481425')
        self.assertEqual(len(os.listdir('arizza/fastq-files')), 8)
        assert os.path.exists('arizza/arizza_deblur.qza')
        assert os.path.exists('arizza/arizza_repseqs.qza')



if __name__ == '__main__':
    unittest.main()