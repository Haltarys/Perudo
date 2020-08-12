#!/bin/python3

from math import comb


def computeBinomialLaw(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def computeBetProbability(n, k, p):
    return sum(computeBinomialLaw(n, i, p) for i in range(k, n + 1))


def getPerudoInput():
    def getLine(msg):
        line = input(msg)

        if '#' in line:
            return line[:line.index('#')]
        return int(line)

    nbDiceBet = getLine("Number of dice bet: ")
    nbDiceTotal = getLine("Total number of dice in game: ")
    nbDiceKnown = getLine("Number of dice in your hand: ")
    nbMatchingDice = getLine("Number of matching dice in your hand: ")

    return nbDiceBet, nbDiceTotal, nbDiceKnown, nbMatchingDice


def printPerudo(tup, verboseOutput=True,  allValues=True):
    if allValues:
        if verboseOutput:
            print(f"Chance of success if not ace: {tup[0] * 100:.2f}%")
            print(f"Chance of exact success if not ace: {tup[1] * 100:.2f}%")
            print(f"Chance of success if ace: {tup[2] * 100:.2f}%")
            print(f"Chance of exact success if ace: {tup[3] * 100:.2f}%")
        else:
            print(*tup, sep='\n')
    else:
        if verboseOutput:
            print(f"Chance of success if not ace: {tup[0] * 100:.2f}%")
        else:
            print(tup[0])


def perudo(nbDiceBet, nbDiceTotal, nbDiceKnown, nbMatchingDice, verboseFlag=True, allValues=False):
    n = nbDiceTotal - nbDiceKnown
    k = nbDiceBet - nbMatchingDice
    p = 1/3
    pAce = 1/6

    if n != int(n) or k != int(k) or k < 0 or n < k:
        raise ValueError

    pSuccess = computeBetProbability(n, k, p)
    pExact = computeBinomialLaw(n, k, p)
    pSuccessAce = computeBetProbability(n, k, pAce)
    pExactAce = computeBinomialLaw(n, k, pAce)

    return pSuccess, pExact, pSuccessAce, pExactAce


if __name__ == "__main__":
    tup = perudo(*getPerudoInput())
    printPerudo(tup)
