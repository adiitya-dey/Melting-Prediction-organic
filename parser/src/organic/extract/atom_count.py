from rdkit import Chem


class AtomCount:

    def __call__(self, mol):
        molecule = Chem.RemoveAllHs(mol)
        atoms = {
            'H': self.hydrogen_count(molecule),
            'C': self.c_count(molecule),
            'B': self.b_count(molecule),
            'N': self.n_count(molecule),
            'O': self.o_count(molecule),
            'P': self.p_count(molecule),
            'S': self.s_count(molecule),
            'F': self.f_count(molecule),
            'Cl': self.cl_count(molecule),
            'Br': self.br_count(molecule),
            'I': self.i_count(molecule),
            'Si': self.si_count(molecule)
        }
        return atoms

    # Hydrogen Count
    @staticmethod
    def hydrogen_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 1:
                count += 1
        return count

    # Boron Count
    @staticmethod
    def b_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 5:
                count += 1

        return count

    # Carbon Count
    @staticmethod
    def c_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 6:
                count += 1

        return count

    # Nitrogen Count
    @staticmethod
    def n_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 7:
                count += 1

        return count

    # Oxygen Count
    @staticmethod
    def o_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 8:
                count += 1

        return count

    # Silicon Count
    @staticmethod
    def si_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 14:
                count += 1

        return count

    # Phosphorous Count
    @staticmethod
    def p_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 15:
                count += 1

        return count

    # Sulphur Count
    @staticmethod
    def s_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 16:
                count += 1

        return count

    # Fluorine Count
    @staticmethod
    def f_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 9:
                count += 1

        return count

    # Chlorine Count
    @staticmethod
    def cl_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 17:
                count += 1

        return count

    # Bromine Count
    @staticmethod
    def br_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 35:
                count += 1

        return count

    # Iodine Count
    @staticmethod
    def i_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() == 53:
                count += 1

        return count

    # Unwanted Count
    @staticmethod
    def unwanted_count(molecule):

        count = 0
        for atom in molecule.GetAtoms():
            if atom.GetAtomicNum() not in (1, 5, 6, 7, 8, 9, 14, 15, 16, 17, 35, 53):
                count += 1

        return count
