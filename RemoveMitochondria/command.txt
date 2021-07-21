#Indexing mitochondria reference
bwa index -a bwtsw /data/fasta_read/mt_ref.fna
samtools faidx mt_ref.fna

#Alignment With Mitochondria genome
bwa mem -t 12 mt_reference/mt_reference.fasta /data/fastq_read/B143/B143-846_1.fq /data/fastq_read/B143/B143-846_2.fq > bwa.sam

#Remove mitochondria from fastq reads
samtools view -b -S -f 12 black_bengal.sam > black_bengal.bam

#Convert Bam To Fastq Conversion
java -Xmx48g -jar ~/Softwares/picard.jar SamToFastq I=unmapped.bam F=read_without_mt_1.fq F2=read_without_mt_2.fq
