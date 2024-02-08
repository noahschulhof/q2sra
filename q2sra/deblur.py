from qiime2.plugins.deblur.methods import denoise_16S

def deblur(study_name, demux, trim_length = None):
    if not trim_length:
        trim_length = -1

    table, rep_seqs, stats = denoise_16S(demultiplexed_seqs = demux, trim_length = trim_length)

    table.save(f'{study_name}_table.qza')
    rep_seqs.save(f'{study_name}_repseqs.qza')
    stats.save(f'{study_name}_stats.qza')