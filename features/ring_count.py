from rdkit.Chem import Lipinski
from rdkit import Chem


class RingCount:

    def __call__(self, mol):
        molecule = Chem.RemoveAllHs(mol)
        rings = {
            'TOTAL RINGS': Lipinski.RingCount(molecule),
            'ALIPHATIC CARBO RINGS': Lipinski.NumAliphaticCarbocycles(molecule),
            'ALIPHATIC HETERO RINGS': Lipinski.NumAliphaticHeterocycles(molecule),
            'AROMATIC CARBO RINGS': Lipinski.NumAromaticCarbocycles(molecule),
            'AROMATIC HETERO RINGS': Lipinski.NumAromaticHeterocycles(molecule)

        }

        return rings
