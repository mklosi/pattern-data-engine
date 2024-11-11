CREATE TABLE dna_seq_metadata (
    id VARCHAR PRIMARY KEY,                    -- Unique identifier for each DNA-seq dataset (matrix_id)
    file_path_bam VARCHAR,                     -- S3 URI to the BAM file with aligned reads
    file_path_vcf VARCHAR,                     -- S3 URI to the VCF file with variant data (optional)
    sample_id VARCHAR,                         -- Identifier for the source sample
    tissue_type VARCHAR,                       -- Tissue origin (e.g., blood, tumor)
    assay_type VARCHAR,                        -- Type of DNA-seq assay (e.g., "whole-genome sequencing", "targeted sequencing")
    sequencing_instrument VARCHAR,             -- Sequencing instrument (e.g., "Illumina HiSeq")
    organism VARCHAR,                          -- Organism (e.g., human, mouse)
    validated BOOLEAN,                         -- Indicates if the sample passed validation
    harmonized BOOLEAN,                        -- Indicates if metadata has been harmonized to a standard ontology
    batch_id VARCHAR,                          -- Batch identifier for the sample
    reference_genome VARCHAR,                  -- Reference genome version used (e.g., "GRCh38")
    sequence_dt TIMESTAMPTZ,                   -- Sequencing date (timezone-aware datetime)
    data_format VARCHAR,                       -- Format of the data file (e.g., "BAM", "VCF")
    -- DNA-seq specific fields ---------------
    coverage FLOAT,                            -- Average coverage or read depth across the target regions
    target_region VARCHAR,                     -- Specifies the target region (e.g., "whole genome", "exome", "custom panel")
    variant_caller VARCHAR,                    -- Variant calling software used (e.g., "GATK", "FreeBayes")
    quality_control_passed BOOLEAN,            -- Indicates if sample passed QC specific to DNA-seq
    format_fields VARCHAR,                     -- GT:AD:DP:GQ:PL
    -- Admin fields --------------------------
    created_at TIMESTAMPTZ,                    -- Record creation timestamp (timezone-aware)
    updated_at TIMESTAMPTZ,                    -- Last update timestamp (timezone-aware)
    class_name VARCHAR,                        -- User-defined class for handling this data
    class_version INT                          -- Version of the data model/class
);
