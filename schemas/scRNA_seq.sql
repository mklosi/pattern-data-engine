CREATE TABLE scrna_seq_metadata (
    id VARCHAR PRIMARY KEY,                    -- Unique identifier for each matrix (matrix_id)
    file_path VARCHAR,                         -- S3 URI to the Parquet file with scRNA-seq data
    cell_type VARCHAR,                         -- Specific cell type (e.g., T-cell, neuron)
    sample_id VARCHAR,                         -- Identifier for the source sample
    tissue_type VARCHAR,                       -- Tissue origin (e.g., liver, lung)
    assay_type VARCHAR,                        -- Type of scRNA-seq assay used (e.g., "10x Genomics")
    sequencing_instrument VARCHAR,             -- Sequencing instrument (e.g., "Illumina NovaSeq")
    organism VARCHAR,                          -- Organism (e.g., human, mouse)
    validated BOOLEAN,                         -- Indicates if the sample passed validation
    harmonized BOOLEAN,                        -- Indicates if metadata has been harmonized to a standard ontology
    normalized BOOLEAN,                        -- Indicates if expression data has been normalized
    normalization_method VARCHAR,              -- Method used for normalization (e.g., "log-normalization")
    batch_id VARCHAR,                          -- Batch identifier for the sample
    reference_genome VARCHAR,                  -- Reference genome version used (e.g., "GRCh38")
    sequence_dt TIMESTAMPTZ,                   -- Sequencing date (timezone-aware datetime)
    data_format VARCHAR,                       -- Format of the data file (e.g., "Parquet")
    -- Admin fields --------------------------
    created_at TIMESTAMPTZ,                    -- Record creation timestamp (timezone-aware)
    updated_at TIMESTAMPTZ,                    -- Last update timestamp (timezone-aware)
    class_name VARCHAR,                        -- User-defined class for handling this data
    class_version INT                          -- Version of the data model/class
);
