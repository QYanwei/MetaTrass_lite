import argparse
import os

config_file_pwd = os.path.realpath(__file__)
config_file_pwd = '/'.join(config_file_pwd.split('/')[:-1]) + '/'

print(config_file_pwd)
parser = argparse.ArgumentParser()
parser.add_argument('-fastq1',      required=True,  type=str,                       help='stlfr clean reads1')
parser.add_argument('-fastq2',      required=True,  type=str,                       help='stlfr clean reads2')

parser.add_argument('-pairdepth',   required=False, type=str,   default=2,          help='filter less X pair barcode reads(default = 2)')
parser.add_argument('-maprate',     required=False, type=str,   default=8,          help='mapping ratio (default=8)')
parser.add_argument('-thread',      required=False, type=str,   default=10,         help='number of threads use(default = 10)')
parser.add_argument('-memory',      required=False, type=str,   default=150,        help='number of memory use(GB,default = 150)',)

parser.add_argument('-prefix',      required=True,  type=str,                       help='output prefix')
parser.add_argument('-outdir',      required=False, type=str,                       help='output folder')

args = parser.parse_args()

fastq1 = args.fastq1
fastq2 = args.fastq2

pairdepth = str(args.pairdepth)
maprate = str(args.maprate)
memory = str(args.memory)
thread = str(args.thread)

output = args.outdir
prefix = args.prefix
tools_dir = config_file_pwd + '../'

if os.listdir(output):
    os.system('rm -rf ' + output + '/*')
os.system('ln -s ' + fastq1 +' '+ output + '/split_reads.1.fq.gz.clean.gz')
os.system('ln -s ' + fastq2 +' '+ output + '/split_reads.2.fq.gz.clean.gz')

os.system('/usr/bin/bash ' + config_file_pwd + 'shell_barcode')

wl = tools_dir + '../config/4M-with-alts-february-2016.txt'
os.system('perl ' + config_file_pwd + 'merge_barcodes.pl barcode_clean_freq.txt ' + wl + ' merge.txt ' + pairdepth + ' ' + maprate +' 1> merge_barcode.log  2>merge_barcode.err')
os.system('perl ' + config_file_pwd + 'fake_10x.pl ' + fastq1 + ' ' + fastq2 + ' merge.txt >fake_10X.log 2>fake_10X.err')
os.system('mv read-I1_si-TTCACGCG_lane-001-chunk-001.fastq.gz ' + output + '/sample_S1_L001_I1_001.fastq.gz')
os.system('mv read-R1_si-TTCACGCG_lane-001-chunk-001.fastq.gz ' + output + '/sample_S1_L001_R1_001.fastq.gz')
os.system('mv read-R2_si-TTCACGCG_lane-001-chunk-001.fastq.gz ' + output + '/sample_S1_L001_R2_001.fastq.gz')

os.system('mv *.log ' + output)
os.system('mv *.err ' + output)

os.system( tools_dir + 'longranger basic --localcores=' + thread + ' --localmem=' + memory + ' --id=longranger --fastqs=' + output + ' 1>_log 2>_err')
os.system( tools_dir + 'spades.py --gemcode1-12 ' + output + '/longranger/outs/barcoded.fastq.gz  -o ' + output + '/cloudspades_out/' + ' -t ' + thread + ' -m ' + memory + ' 1>>_log 2>>_err')
os.system( 'mv ' + output + '/cloudspades_out/scaffolds.fasta ' + output + '/' + prefix + '_scaffold.fa' )
#os.system(args.supernova + 'supernova run --id=supernova_out --maxreads=' + maxreads + ' --fastqs=' + output + ' --accept-extreme-coverage --localcores=' + thread + ' --localmem=' + memory + ' --nopreflight 1>_log 2>_err')

#os.system(args.supernova + 'supernova mkoutput --style=pseudohap --asmdir=supernova_out/outs/assembly --outprefix=' + prefix + '_supernova_result')
