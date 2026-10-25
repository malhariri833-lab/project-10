def total_bill(bill_amount, tip_perc):
    return bill_amount + (bill_amount * tip_perc / 100)

print(total_bill(150, 20))


def seating_arrangements(guests):
    """Calculate the number of seating arrangements for guests."""
    if guests == 0 or guests == 1:
        return 1
    return guests * seating_arrangements(guests - 1)


print(seating_arrangements.__doc__)

print(seating_arrangements(1))
print(seating_arrangements(2))
print(seating_arrangements(3))
print(seating_arrangements(5))