#this code takes in a DNA sequence and inserts a space every 10 nucleotides. It also starts a new line after 5 spaces have been entered
#the modified string is then written to a text file

fasta = "TAATTTTAAACTTAATAAATTTATAATTTTATCTTTTATTATTAATTTTATAATTTTTTTATATTTAAATTTTAAATTAAATTTATTTTACTCATTAATTAAAAAATATAATTTTTCCGAATCTAATTATTTAATAAAACTTAATGAAATAAATTTTCAAAATATTTTATATTTATATGAATACCCATTGAATAATATCACCATTAGATCAATATTTTACTTATTGATTTCTATATTTTCTATTATTAAAATCTGTTCTATAAAATCTATCTCCATACGTAAAATCAATTAATTAACCCTTAATATTAAATAACAATTATGAATAAAAATTTAATTAATTTTATAAAAATATCTATAATGAATCTACCCTCACCTGTGAATATTTCATACTTATGAAATTTTGGATCTTTACTTGGATTATTTCTAATAATTCAAATTATAAGAGGATTCTTTTTATCTATACACTATTGCCCCAACACAAATTTTGCTTTTTTTAGAATTATTCACATCATTCAAAATGTAAAAATAGGATGATTAATTCATAATATTCATATTAATGGAGCTTCAATATTTTTTATTTGTATATATTTACATATCAGACGAGGATTATATTATAATTCATATAAATTAATTAATACTTGATTAATTGGAGTATCAATTTATCTTCTATCAATAGCTACTGCTTTTTTAGGTTATGTACTTCCTTGAGGACAAATATCATTCTGAGGAGCAACTGTTATTACTAATTTAATATCTACAATTCCTTATATGGAAACTTAATAGTACAATGAATCTGAGGAGGATTTTCAATTAATAACGCTACATTAAATCGATTTTATTCAATCCATTTTATTCTTCCATTTATTATTACAATAATAGTAATATTACATTTATTTTTTTTACATACCACAGGCTCATCAAACCCATTAGGAATTAATAGAAATTTATATAAAATTCCTTTTCATATCTATTTTTCAATTAAAGATATTTTAGGGTTCATAATTTTTATTTTTTTTTTCTGATTAATCAATCTTGAATACCCATATATTTTTAGAGATCCAGATAATTTTATTCCAGCAAATCCTATAGTAACCCCTATCCATATTCAACCAGAATGATATTTTTTATTCGCATATGCAATTTTACGATCCATTCCTAATAAATTAGGAGGTGTGATTGCTTTATTATCATCAATTATTATCCTATATTTCTTACCTTTAATTAATCCTAAATTTAATTCATTCACATTTTATCCTATTAATCAAATTATATATTGAATTTTTTCTAATACATTTATTCTCTTAACTTGAGCAGGATCTCAAGTCATTGAATATCCATTTATTATTATTACCCAAATCCTATCATATATTTATTTTTTATACTTTATATTTTCTTACATCTGCTTAAAAATATGAGATAAAATAATTTTTTATTATAATTAAAATATATTAAAAATAAAATTAAACTTAAATTTATCACACTAATTTTTTTATTTAGTTAATGATCTTGATTAAAGTTTATGTTT"
newLine = 0
temp = ""
for i in range(0, len(fasta)):
    
    if i % 10 == 0 and i > 0:

        if newLine == 5:
            temp += fasta[i-10: i] + "\n\n"
            newLine = 0

        else:
            temp += fasta[i-10: i] + " "
            newLine += 1


fastaText = open('insert name of the text file', "w")
fastaText.write(temp)
fastaText.close()
