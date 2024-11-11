class OntologyMapper:
    """A helper class for mapping raw metadata to standardized ontology terms."""

    tissue_mapping = {
        "lung": "UBERON_0002048",
        "liver": "UBERON_0002107",
        "brain": "UBERON_0000955",
        # Add more mappings as needed or load from a config
    }

    cell_type_mapping = {
        "t-cell": "CL_0000084",
        "hepatocyte": "CL_0000182",
        # Additional cell type mappings
    }

    organism_mapping = {
        "homo sapiens": "NCBI_9606",
        "mus musculus": "NCBI_10090",
        # Additional organism mappings
    }

    @staticmethod
    def map_tissue(tissue):
        return OntologyMapper.tissue_mapping.get(tissue.lower(), "UNKNOWN")

    @staticmethod
    def map_cell_type(cell_type):
        return OntologyMapper.cell_type_mapping.get(cell_type.lower(), "UNKNOWN")

    @staticmethod
    def map_organism(organism):
        return OntologyMapper.organism_mapping.get(organism.lower(), "UNKNOWN")
