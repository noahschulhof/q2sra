import unittest
import os
import shutil
from q2sra.prefetch import prefetch

class PrefetchTest(unittest.TestCase):

    def setUp(self):
        os.makedirs('test_dir')
    

    def tearDown(self):
        os.chdir('../')
        shutil.rmtree('test_dir')


    def test_valid_accession1(self):
        prefetch('PRJNA737199', 'test_dir')

        self.assertEqual(len(os.listdir()), 35)
    

    def test_valid_accession2(self):
        prefetch('SRP107074', 'test_dir')

        self.assertEqual(len(os.listdir()), 60)


    def test_valid_accession2(self):
        prefetch('ERP017462', 'test_dir')

        self.assertEqual(len(os.listdir()), 170)


    def test_invalid_accession(self):
        prefetch('PRJNA12345678', 'test_dir')

        self.assertEqual(len(os.listdir()), 0)



if __name__ == '__main__':
    unittest.main()