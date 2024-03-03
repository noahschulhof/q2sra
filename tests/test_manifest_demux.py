import unittest
import shutil
import os
from q2sra.filter_fastq import filter_fastq
from q2sra.manifest import manifest
from q2sra.demux import demux

class DemuxTest(unittest.TestCase):
    def setUp(self):
        shutil.copytree('tests/ning', 'ning')
        shutil.copytree('tests/jiang', 'jiang')
    

    def tearDown(self):
        os.chdir('../')
        shutil.rmtree('ning')
        shutil.rmtree('jiang')
    

    def test_paired(self):
        os.chdir('ning')
        filter_fastq([], [], True, 7)
        manifest('ning', True)
        assert os.path.exists('ning_manifest.txt')
        demux(True, 'ning_manifest.txt')
        assert os.path.exists('ning_demux.qza')


    def test_single(self):
        os.chdir('ning')
        filter_fastq([], [], False, 6)
        manifest('ning', False)
        assert os.path.exists('ning_manifest.txt')
        demux(False, 'ning_manifest.txt')
        assert os.path.exists('ning_demux.qza')

        os.chdir('../jiang')
        filter_fastq([], [], False, 12)
        manifest('jiang', False)
        assert os.path.exists('jiang_manifest.txt')
        demux(False, 'jiang_manifest.txt')
        assert os.path.exists('jiang_demux.qza')



if __name__ == '__main__':
    unittest.main()