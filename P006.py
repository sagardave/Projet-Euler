import math;

numOfTerms = 100;

sumOfSeries = (numOfTerms)*(1 + numOfTerms)/2;

squareOfSums = math.pow(sumOfSeries,2);

sumOfSquares = (numOfTerms * (numOfTerms + 1) * (2 * numOfTerms + 1))/6;

print squareOfSums - sumOfSquares;
