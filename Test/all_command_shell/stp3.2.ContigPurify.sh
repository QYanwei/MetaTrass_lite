/zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass_Lite/tools/python3 /zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass_Lite/tools/quast/quast.py -r /zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass_Lite/database/uhgg_kraken2-fa//17_genomic.fa -t 2 --min-identity 90 -o /zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass_Lite//Test/dir3_assembly/quast/17 /zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass_Lite//Test/dir3_assembly/supernova/17/17_scaffold.fa
/zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass_Lite/tools/python3 /zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass_Lite/tools/contig_purify.py -rawContig /zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass_Lite//Test/dir3_assembly/supernova/17/17_scaffold.fa -purifySeq /zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass_Lite//Test/dir3_assembly//purify/17.fa -quastAlnTsv /zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass_Lite//Test/dir3_assembly/quast/17/contigs_reports/all_alignments_17_scaffold.tsv -IDY 90 -PCT 50
