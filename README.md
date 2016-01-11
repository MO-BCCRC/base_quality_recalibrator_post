#BQSR : Base Quality Score Recalibration : 2nd Step


```
Development information

date created : Sep 09 2014
last update  : Sep 09  2014
Developer    : Rad Aniba (raniba@bccrc.ca)
Input        : Realigned alignment, BQSR file (1st Step), reference genome, dbsnp 
Output       : grp score file
Seed used    : <no_seed>

```


###Usage

This walker is designed to work as the first pass in a two-pass processing step. It does a by-locus traversal operating only at sites that are not in dbSNP. We assume that all reference mismatches we see are therefore errors and indicative of poor base quality. This walker generates tables based on various user-specified covariates (such as read group, reported quality score, cycle, and context). Since there is a large amount of data one can then calculate an empirical probability of error given the particular covariates seen at this site, where p(error) = num mismatches / num observations. The output file is a table (of the several covariate values, num observations, num mismatches, empirical quality score).

###Dependencies

- GATK
- python



###Example

```
java -Xmx4g -jar GenomeAnalysisTK.jar \
   -T BaseRecalibrator \
   -I my_reads.bam \
   -R resources/Homo_sapiens_assembly18.fasta \
   -knownSites bundle/hg18/dbsnp_132.hg18.vcf \
   -knownSites another/optional/setOfSitesToMask.vcf \
   -o recal_data.table
```

###Known issues

(will update later)

###Last updates

(will update later)

### test data
Reference : /genesis/extscratch/shahlab/raniba/Software/bowtie2/genomes/GRCh37-lite   
seq1 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R1_001.fastq 
seq2 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R2_001.fastq  
outfile : test.bam   

bowtie2 path : /genesis/extscratch/shahlab/raniba/Software/bowtie2/  
samtools path : /extscratch/shahlab/raniba/pipelines/miseq_pipeline/miseq_analysis_pipeline/miseq-pipeline/software/samtools-0.1.19/samtools 


