python="/dellfsqd1/ST_OCEAN/ST_OCEAN/USRS/xumengyang/software/anaconda2/bin/python"


#output=$outdir/Test
#mkdir -p $output

Trass="./MetaTrass_Lite/Trass.py"
ref_db="./database/uhgg_kraken2-db/"
ref_fa="./database/uhgg_kraken2-fa/"
ref_gz="./dababase/uhgg_kraken2-fa/ref_genome_size.txt"

$python $Trass GC -rawfq1 $rawfq1 -rawfq2 $rawfq2 -outdir $output -runnow no

$python $Trass TB -cleanfq1 $output/dir1_cleandata/split_reads.1.fq.gz.clean.gz \
                  -cleanfq2 $output/dir1_cleandata/split_reads.2.fq.gz.clean.gz \
		   -thread 10 -sample $sample -ref_db $ref_db -genome_size $ref_gz -outdir $output -runnow yes
		   
$python $Trass AP -outdir $output -ref_fa $ref_fa -thread 10 -parallel 10 -runnow yes 
