import unittest
import shutil
import os
from q2sra.filter_fastq import filter_fastq
from q2sra.manifest import manifest
from q2sra.demux import demux
from q2sra.deblur import deblur

class DeblurTest(unittest.TestCase):
    def setUp(self):
        shutil.copytree('tests/ning', 'ning')
        shutil.copytree('tests/jiang', 'jiang')
    

    def tearDown(self):
        os.chdir('../')
        shutil.rmtree('ning')
        shutil.rmtree('jiang')
    

    def test_paired(self):
        os.chdir('ning')
        filter_fastq([], [], True, 8)
        manifest('ning', True)
        artifact = demux(True, 'ning_manifest.txt')
        deblur('ning', artifact)
        assert os.path.exists('ning_table.qza')
        assert os.path.exists('ning_repseqs.qza')
        assert os.path.exists('ning_stats.qza')


    def test_single(self):
        os.chdir('ning')
        filter_fastq([], [], False, 5)
        manifest('ning', False)
        artifact = demux(False, 'ning_manifest.txt')
        deblur('ning', artifact)
        assert os.path.exists('ning_table.qza')
        assert os.path.exists('ning_repseqs.qza')
        assert os.path.exists('ning_stats.qza')

        os.chdir('../jiang')
        filter_fastq([], [], False, 5)
        manifest('jiang', False)
        artifact = demux(False, 'jiang_manifest.txt')
        deblur('jiang', artifact)
        assert os.path.exists('jiang_table.qza')
        assert os.path.exists('jiang_repseqs.qza')
        assert os.path.exists('jiang_stats.qza')



if __name__ == '__main__':
    unittest.main()