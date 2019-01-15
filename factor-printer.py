
def print_factor(the_number):

    if the_number == 0:
        print "Cannot find the factors of zero."
        return

    if the_number == 1:
        print "One is the only number with one-ish (or two) factors - both one and itself (one)."
        return

    candidate = 1
    factors = []
    while candidate not in factors:
        if the_number % candidate == 0:
            factors += [candidate]
            factors += [the_number /candidate]
            factors += [-candidate]
            factors += [-the_number / candidate]

        candidate += 1

    factor_stmt = "The list of factors for %s is %s" %(the_number, factors)
    print factor_stmt
    return factor_stmt


import random

mem_killer = []
for n in range(2, 1000000):
    the_subject = random.randint(1, n)
    stmt = print_factor(the_subject)
    mem_killer += ["@@@@@@@@@ => %s\n" % (stmt)]
    if (len(mem_killer) % 100000 == 0):
        print "".join(mem_killer)
