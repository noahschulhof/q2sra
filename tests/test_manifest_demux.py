import unittest
import shutil
import os
from q2sra.filter_fastq import filter_fastq
from q2sra.manifest import manifest
from q2sra.demux import demux

class DemuxTest(unittest.TestCase):
    def setUp(self):
        shutil.copytree('tests/ning', 'ning')
        os.chdir('ning')
    

    def tearDown(self):
        os.chdir('../')
        shutil.rmtree('ning')
    

    def test_paired(self):
        filter_fastq([], [], True, 30)

        manifest('ning', True)

        assert os.path.exists('ning_manifest.txt')

        demux(True, 'ning_manifest.txt')

        assert os.path.exists('ning_demux.qza')

    def test_single(self):
        filter_fastq([], [], False, 30)

        manifest('ning', False)

        assert os.path.exists('ning_manifest.txt')

        demux(False, 'ning_manifest.txt')
        
        assert os.path.exists('ning_demux.qza')



if __name__ == '__main__':
    unittest.main()