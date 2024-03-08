import unittest
import os
import shutil
from q2sra.filter_fastq import filter_fastq
from q2sra.prefetch import prefetch

class FilterTest(unittest.TestCase):

    def setUp(self):
        shutil.copytree('tests/ning', 'ning')
        shutil.copytree('tests/jiang', 'jiang')
    

    def tearDown(self):
        os.chdir('../')
        shutil.rmtree('ning')
        shutil.rmtree('jiang')


    def test_filter_nsamples(self):
        os.chdir('ning')
        filter_fastq([], [], True, nsamples = 15)
        self.assertEqual(len(os.listdir('fastq-files')), 30)

        os.chdir('../jiang')
        filter_fastq([], [], False, nsamples = 8)
        self.assertEqual(len(os.listdir('fastq-files')), 8)


    def test_remove_reverse(self):
        os.chdir('ning')
        filter_fastq([], [], False, nsamples = 24)
        self.assertEqual(len(os.listdir('fastq-files')), 24)
    

    def test_include(self):
        os.chdir('ning')
        filter_fastq(['835'], [], False, nsamples = 8)
        self.assertEqual(len(os.listdir('fastq-files')), 8)
        self.assertTrue(all('835' in f for f in os.listdir('fastq-files')))

        os.chdir('../jiang')
        filter_fastq(['Captive'], [], False, nsamples = 8)
        self.assertEqual(len(os.listdir('fastq-files')), 3)
        self.assertTrue(all('Captive' in f for f in os.listdir('fastq-files')))
    

    def test_exclude(self):
        os.chdir('ning')
        filter_fastq([], ['835'], True, nsamples = 35)
        self.assertEqual(len(os.listdir('fastq-files')), 50)
        self.assertTrue(all(not '835' in f for f in os.listdir('fastq-files')))

        os.chdir('../jiang')
        filter_fastq([], ['in'], False, nsamples = 30)
        self.assertEqual(len(os.listdir('fastq-files')), 16)
        self.assertTrue(all(not 'in' in f for f in os.listdir('fastq-files')))

    
    def test_include_exclude(self):
        os.chdir('ning')
        filter_fastq(['835', '836'], ['9'], True, nsamples = 20)
        self.assertEqual(len(os.listdir('fastq-files')), 36)
        self.assertTrue(all('835' in f or '836' in f and not '9' in f for f in os.listdir('fastq-files')))

        os.chdir('../jiang')
        filter_fastq(['from'], ['Wild'], False, nsamples = 5)
        self.assertEqual(len(os.listdir('fastq-files')), 3)
        self.assertTrue(all('from' in f and not 'Wild' in f for f in os.listdir('fastq-files')))



if __name__ == '__main__':
    unittest.main()