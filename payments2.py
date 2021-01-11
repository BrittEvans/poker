#!/usr/bin/env python

import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


class Payment:
    def __init__(self, name, balance, seven2=0):
        self.name = name
        self.balance = balance
        self.seven2 = seven2

    def __str__(self):
        return f"{self.name}\t{self.balance}\t{self.seven2}"


def handle_72(payments):
    # Deal with 7-2s
    n_payers = len(payments)
    total_72 = sum(i.seven2 for i in payments)
    for i in payments:
        i.balance -= total_72
        i.balance += i.seven2 * n_payers

    if sum(i.balance for i in payments) >= 0.01:
        print("ERROR - Payments don't sum to zero,", sum(i.balance for i in payments))
        sys.exit(1)


def print_payouts(payments):
    # Do the computations
    while max(i.balance for i in payments) >= 0.01:
        # Who is most negative?
        most_neg = min(payments, key=lambda i: i.balance)

        # Who is most positive?
        most_pos = max(payments, key=lambda i: i.balance)

        # Figure out how much to pay
        if most_pos.balance >= -most_neg.balance:
            amt = -most_neg.balance
        else:
            amt = most_pos.balance

        # Make the payment
        most_pos.balance -= amt
        most_neg.balance += amt
        print(f"{most_neg.name} pays {amt:.2f} to {most_pos.name}")


def process_week(payments):
    # Deal with 7-2s
    handle_72(payments)
    print_payouts(payments)


def daily_totals(all_data):
    out = []
    for d, grp in all_data.groupby(["date"]):
        payments = grp.apply(lambda row: Payment(row["name"], row.profit, row.seven2), axis=1)
        handle_72(payments)
        for i in payments:
            out.append(dict(date=d, name=i.name, profit=i.balance))
    return pd.DataFrame(out)


if __name__ == "__main__":

    # Load all the results
    results = pd.read_csv("/Users/britt/poker/pokerlog.csv", parse_dates=["date"])

    # Filter by the last game
    max_date = results.date.max()
    last_game = results.query("date == @max_date")

    # Create payments object
    payments = last_game.apply(lambda row: Payment(row["name"], row.profit, row.seven2), axis=1)

    # Do stats for the week
    process_week(payments)

    # Update the charts
    overall = daily_totals(results)
    totals = []
    for name, df in overall.groupby("name"):
        df = df.sort_values(["date"])
        df["total"] = df.profit.cumsum()
        totals.append(df)
    to_plot = pd.concat(totals)

    sns.set_style("darkgrid")
    p3 = sns.lineplot(x="date",y="total",hue="name", style="name", dashes=False, markers=True, data=to_plot)
    p3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.subplots_adjust(right=0.8)
    plt.xticks(rotation=30)
    p3.get_figure().savefig(f"/Users/britt/poker/winnings_{str(max_date)[:10]}.png")
