import qiime2.plugins.dada2.actions as dada2_actions

def dada2(study_name, demux, trim_left = 0, trunc_len = 0):
    table, rep_seqs, stats = dada2_actions.denoise_single(demultiplexed_seqs = demux, trim_left = trim_left, trunc_len = trunc_len)
    
    table.save(f'{study_name}_table.qza')
    rep_seqs.save(f'{study_name}_repseqs.qza')
    stats.save(f'{study_name}_stats.qza')