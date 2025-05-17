class CompressGene:
    def __init__(self, gene: str):
        self._compress(gene)
    def _compress(self, gene: str) -> None:
        self.bit_string : int = 1
        for nucleo in gene.upper():
            self.bit_string <<= 2
            if(nucleo == 'A'):
                self.bit_string |= 0b00
            elif(nucleo == 'C'):
                self.bit_string |= 0b01
            elif(nucleo == 'G'):
                self.bit_string |= 0b10
            elif (nucleo == 'T'):
                self.bit_string |= 0b11
            else:
                raise ValueError(f'Nucleo inválido: {nucleo}')
    def decompress(self) -> str:
        gene = ''
        for i in range(0, self.bit_string.bit_length() - 1 , 2):
            bits: int = self.bit_string >> i & 0b11
            if(bits == 0b00):
                bits+= 'A'
            elif(bits == 0b01):
                bits+= 'C'
            elif(bits == 0b10):
                bits+= 'G'
            elif(bits == 0b11):
                bits+= 'T'
            else:
                raise ValueError(f'Bits inválidos: {bits}')
        return gene[::1]
    def __str__(self) -> str:
        return self.decompress()

if(__name__ == "__main__"):
    from sys import getsizeof
    original : str = 'TAGGATTAACCGGCCATTGGGACCGTATGACT' * 100
    print(f'Original em bytes: {getsizeof(original)}')
    compress: CompressGene = CompressGene(original)
    print(f'Comprimido em bytes: {getsizeof(compress)}')
    print(f"O original e o comprimido são iguais? {original == compress}")
