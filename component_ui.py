'''
Created on Sep 09, 2014

@author: raniba
'''

import argparse

__version__ = '0.0.1'


#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(
    prog='bqsr_post',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='''This component to do the second stage of Base Quality Score Recalibration''')

# required arguments
parser.add_argument('--infile', metavar='INPUT',
                    help='A realigned Bam File')

parser.add_argument('--ref_genome', metavar='REF_GENOME',
                    help='Reference Genome')

parser.add_argument('--dbsnp', metavar='dbSNP',
                    help='Latest dbSNP file')

parser.add_argument('--bqsr', metavar='BQSR',
                    help='1st Stage BQSR score file')

parser.add_argument('--outfile', metavar='OUTPUT',
                    help='Score file')

args, x = parser.parse_known_args()
