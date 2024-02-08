import unittest
import os
import shutil
from q2sra.filter_fastq import filter_fastq
from q2sra.prefetch import prefetch

class FilterTest(unittest.TestCase):

    def setUp(self):
        shutil.copytree('tests/ning', 'ning')
        os.chdir('ning')
    

    def tearDown(self):
        os.chdir('../')
        shutil.rmtree('ning')


    def test_filter_nsamples(self):
        filter_fastq([], [], True, nsamples = 15)

        self.assertEqual(len(os.listdir('fastq-files')), 30)


    def test_remove_reverse(self):
        filter_fastq([], [], False, nsamples = 24)

        self.assertEqual(len(os.listdir('fastq-files')), 24)
    

    def test_include(self):
        filter_fastq(['835'], [], False, nsamples = 8)

        self.assertEqual(len(os.listdir('fastq-files')), 8)
    

    def test_exclude(self):
        filter_fastq([], ['835'], True, nsamples = 35)

        self.assertEqual(len(os.listdir('fastq-files')), 50)
    
    def test_include_exclude(self):
        filter_fastq(['835', '836'], ['9'], True, nsamples = 20)

        self.assertEqual(len(os.listdir('fastq-files')), 36)



if __name__ == '__main__':
    unittest.main()