from qiime2 import Artifact

def demux(paired, manifest_filepath):
    if paired:
        artifact = Artifact.import_data('SampleData[PairedEndSequencesWithQuality]', manifest_filepath, view_type = 'PairedEndFastqManifestPhred33V2')
    else:
        artifact = Artifact.import_data('SampleData[SequencesWithQuality]', manifest_filepath, view_type = 'SingleEndFastqManifestPhred33')

    demux_filename = manifest_filepath.replace('manifest.txt', 'demux.qza')

    artifact.save(demux_filename)

    return artifact