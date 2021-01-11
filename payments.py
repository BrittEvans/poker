#!/usr/bin/env python

import sys

class Payment:
  def __init__(self, name, balance, seven2=0):
    self.name = name
    self.balance = balance
    self.seven2 = seven2
  def __str__(self):
    return f"{self.name}\t{self.balance}\t{self.seven2}"


## Set the payment amounts
TOTALS = [Payment("Britt",   55.90, 0),
          Payment("Zach",    39.89, 0),
          Payment("Alex",    38.75, 1),
          Payment("Michael",  2.56, 0),
          Payment("Danny",  -34.35, 0),
          Payment("Colin",  -62.75, 1),
          Payment("Steiny", -40.00, 0)]
for i in TOTALS:
  print(i)

# Set the payment amounts
# 7/15
TOTALS = [Payment("Britt",    6.02, 0),
          Payment("Zach",   -40.00, 0),
          Payment("Alex",    83.71, 1),
          Payment("Michael", 21.56, 0),
          Payment("Danny",   37.94, 0),
          Payment("Colin",  -60.00, 1),
          Payment("Tucker", -25.23, 0),
          Payment("Steiny", -24.00, 1)]
for i in TOTALS:
  print(i)

# 8/7
TOTALS = [Payment("Britt",    8.08, 0),
          Payment("Zach",   -19.03, 0),
          Payment("Alex",     1.76, 0),
          Payment("Danny",   29.32, 1),
          Payment("Colin",  -20.13, 0)]
for i in TOTALS:
  print(i)

# 8/31
TOTALS = [Payment("Britt",  -30.17, 0),
          Payment("Zach",    11.84, 0),
          Payment("Michael",-20.00, 0),
          Payment("Danny",  -13.10, 1),
          Payment("Colin",   57.56, 0),
          Payment("Tucker",  -6.13, 1)]
for i in TOTALS:
  print(i)

# 9/16
TOTALS = [Payment("Britt",  -15.02, 0),
          Payment("Alex",   -40.00, 0),
          Payment("Michael",-20.00, 0),
          Payment("Danny",   54.79, 0),
          Payment("Colin",  140.23, 0),
          Payment("Tucker", -60.00, 0),
          Payment("Steiny", -60.00, 1)]
for i in TOTALS:
  print(i)

# 10/22
TOTALS = [Payment("Britt",  -40.25, 0),
          Payment("Danny",  -13.28, 2),
          Payment("Colin",   24.63, 0),
          Payment("Tucker",  48.90, 2),
          Payment("Steiny", -20.00, 0)]
for i in TOTALS:
  print(i)

# 11/03
TOTALS = [Payment("Britt",   23.49, 0),
          Payment("Danny",  -40.00, 1),
          Payment("Colin",   45.82, 0),
          Payment("Tucker", -13.30, 0),
          Payment("Steiny", -16.01, 1)]
for i in TOTALS:
  print(i)

# 11/05
TOTALS = [Payment("Britt",  -68.93, 0),
          Payment("Danny",   31.06, 1),
          Payment("Colin",   23.39, 1),
          Payment("Tucker",  44.98, 1),
          Payment("Steiny", -30.50, 1)]
for i in TOTALS:
  print(i)

TOTALS = [Payment("Britt",  -68.54, 0),
          Payment("Danny",   44.82, 0),
          Payment("Colin",   48.35, 0),
          Payment("Tucker",  35.37, 0),
          Payment("Steiny", -60.00, 0)]
for i in TOTALS:
  print(i)

# 11/29
TOTALS = [Payment("Britt",  -37.50, 0),
          Payment("Danny",   88.30, 1),
          Payment("Colin", -104.79, 0),
          Payment("Tucker",  53.61, 0),
          Payment("Steiny",  00.38, 0)]
for i in TOTALS:
  print(i)

# Deal with 7-2s
n_payers = len(TOTALS)
total_72 = sum(i.seven2 for i in TOTALS)
for i in TOTALS:
  i.balance -= total_72
  i.balance += i.seven2 * n_payers


if sum(i.balance for i in TOTALS) >= 0.01:
  print("ERROR - Payments don't sum to zero,", sum(i.balance for i in TOTALS))
  sys.exit(1)

# Do the computations
while max(i.balance for i in TOTALS) >= 0.01:
  # Who is most negative?
  most_neg = min(TOTALS, key=lambda i: i.balance)

  # Who is most positive?
  most_pos = max(TOTALS, key=lambda i: i.balance)

  # Figure out how much to pay
  if most_pos.balance >= -most_neg.balance:
    amt = -most_neg.balance
  else:
    amt = most_pos.balance

  # Make the payment
  most_pos.balance -= amt
  most_neg.balance += amt
  print(f"{most_neg.name} pays {amt:.2f} to {most_pos.name}")
