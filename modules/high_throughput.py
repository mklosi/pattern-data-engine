from abc import ABC, abstractmethod

from modules.ontology_mapper import OntologyMapper


class Data(ABC):
    def __init__(self, input_reference):
        """
        :param input_reference: (dict or json)
        """
        self.class_version = 1
        self.metadata = None
        self.data = None
        self.input_reference = input_reference

    @abstractmethod
    def load_data(self):
        """Load data from a source."""
        pass

    @abstractmethod
    def validate_data(self):
        """Validate the data for consistency."""
        pass

    @abstractmethod
    def harmonize_metadata(self):
        """Standardize metadata based on ontology rules."""
        pass

    @abstractmethod
    def save_data(self):
        """Save data in their respective formats and store metadata in Redshift."""
        pass


class HighThroughputData(Data):
    def __init__(self, assay_type, input_reference):
        super().__init__(input_reference)
        self.assay_type = assay_type

    @abstractmethod
    def process_data(self):
        """Process the raw sequencing data."""
        pass


class MRNASeqData(HighThroughputData):
    def __init__(self, input_reference):
        super().__init__("mRNA-seq", input_reference)

    def load_data(self):
        """Load data from external source.

        This method will be responsible for loading raw data from a system external
          to Data Engine. This external system could be itself internal or
          external to PatternBio. The data is loaded raw, and it will load
          both the data and metadata. It's the first method that would be called
          when a new set of data is to be ingested into the Data Engine.

        The `input_reference` variable should probably be a dictionary or
          json with all relevant information on how to query the data that
          needs to be ingested. It could be BAM files for DNA-seq, or VCF files,
          or CVS files, or it could be data sitting in another database. It
          could also be an API that would need to be called. I've used this
          pattern before, and I've also used additional Loader classes for each
          data type, but keeping it simple here. This method is the entry
          point for any HighThroughputData type.
        """
        print("Loading RNA-seq data...")

    def validate_data(self):
        print("Validating RNA-seq data for consistency...")

    def harmonize_metadata(self):
        """Standardize mRNA-seq metadata using ontology mappings."""
        print("Harmonizing mRNA-seq metadata...")

        # Map tissue type
        if "tissue_type" in self.metadata:
            self.metadata["tissue_type"] = OntologyMapper.map_tissue(self.metadata["tissue_type"])

        # Map organism
        if "organism" in self.metadata:
            self.metadata["organism"] = OntologyMapper.map_organism(self.metadata["organism"])

        # Example of handling additional mappings if needed
        if "disease_status" in self.metadata:
            # Hypothetical mapping for disease status, might involve additional logic
            self.metadata["disease_status"] = self.metadata["disease_status"].capitalize()

        print("Completed harmonizing mRNA-seq metadata.")

    def process_data(self):
        print("Processing RNA-seq sequences...")

    def save_data(self):
        """Save data in their respective formats and store metadata in Redshift."""
        print("Saving data...")


class SingleCellRNASeqData(HighThroughputData):
    def __init__(self, input_reference):
        super().__init__("scRNA-seq", input_reference)

    def load_data(self):
        print("Loading single-cell RNA-seq data...")

    def validate_data(self):
        print("Validating scRNA-seq data for consistency across cells...")
        # Example: Check that all cells have the same number of genes represented
        if not all(len(row) == len(self.data[0]) for row in self.data):
            raise ValueError("Inconsistent gene counts across cells")

    def harmonize_metadata(self):
        print("Standardizing scRNA-seq metadata using cell ontology...")
        # Example: Convert cell types to a consistent format, e.g., using UBERON or Cell Ontology IDs

        # Map tissue type
        if "tissue_type" in self.metadata:
            self.metadata["tissue_type"] = OntologyMapper.map_tissue(self.metadata["tissue_type"])

        # Map cell type
        if "cell_type" in self.metadata:
            self.metadata["cell_type"] = OntologyMapper.map_cell_type(self.metadata["cell_type"])

        # Map organism
        if "organism" in self.metadata:
            self.metadata["organism"] = OntologyMapper.map_organism(self.metadata["organism"])

        print("Completed harmonizing scRNA-seq metadata.")

    def process_data(self):
        print("Processing single-cell RNA-seq data...")
        # Example: Normalize gene expression across cells, like log-normalization

    def save_data(self):
        """Save data in their respective formats and store metadata in Redshift."""
        print("Saving data...")


class DNASeqData(HighThroughputData):
    def __init__(self, input_reference):
        super().__init__("DNA-seq", input_reference)

    def load_data(self):
        """Load DNA-seq data from external source.

        This method loads raw DNA-seq data based on the provided input_reference,
        which could include paths to BAM files, VCF files, or external API references.
        It initializes both data and metadata for further processing.
        """
        print("Loading DNA-seq data from external source...")
        # Example: Use input_reference to locate and load BAM or VCF files.
        # Set self.metadata and self.data based on loaded content.
        # self.data = <loaded data>
        # self.metadata = <loaded metadata>

    def validate_data(self):
        """Validate DNA-seq data for consistency."""
        print("Validating DNA-seq data for consistency...")
        # Example validation: Check if coverage data is within acceptable ranges.
        if "coverage" in self.metadata and self.metadata["coverage"] < 10:
            raise ValueError("Insufficient sequencing coverage detected for DNA-seq sample")

    def harmonize_metadata(self):
        """Standardize DNA-seq metadata using ontology mappings."""
        print("Harmonizing DNA-seq metadata...")

        # Map tissue type
        if "tissue_type" in self.metadata:
            self.metadata["tissue_type"] = OntologyMapper.map_tissue(self.metadata["tissue_type"])

        # Map organism
        if "organism" in self.metadata:
            self.metadata["organism"] = OntologyMapper.map_organism(self.metadata["organism"])

        print("Completed harmonizing DNA-seq metadata.")

    def process_data(self):
        """Process the raw sequencing data for DNA-seq."""
        print("Processing DNA-seq sequences...")
        # Example processing: Filter out low-quality reads, calculate variant frequencies.
        # This would typically include aligning reads or calling variants as needed.
        # Example: self.data = self.filter_low_quality_reads(self.data)

    def save_data(self):
        """Save data in their respective formats and store metadata in Redshift."""
        print("Saving data...")
