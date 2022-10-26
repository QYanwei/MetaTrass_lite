cp /zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass/config//lane.lst /zfsqd1/ST_OCEAN/USRS/qiyanwei/project2/4.MetaTrass/7.Demo//Test/dir1_cleandata//lane.lst 
cd /zfsqd1/ST_OCEAN/USRS/qiyanwei/project2/4.MetaTrass/7.Demo//Test/dir1_cleandata/ 
/zfsqd1/ST_OCEAN/USRS/qiyanwei/software/api/MetaTrass/tools/SOAPfilter_v2.2 -t 10 -F CTGTCTCTTATACACATCTTAGGAAGACAAGCACTGACGACATGA -R TCTGCTGAGTCGAGAACGTCTCTGTGAGCCAAGGAGTTGCTCTGG -y -p -M 2 -f -1 -Q 10 lane.lst stat.txt
