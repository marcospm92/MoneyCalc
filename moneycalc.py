# MoneyCalc
# v1.0
# 31/10/2018
# Marcos Pérez Martín

# Configuration of the program. On future versions maybe a different file that
# can be changed inside program and loaded to have all variables.

# Assign names to each different group
# Each group will have two different subgroups. For future versions ask how
# many subgroups are needed inside any group
g1 = "Group 1"
g2 = "Group 2"
g3 = "Group 3"
g4 = "Group 4"

# Assign number of people on each subgroup.
n_g1_1 = 0
n_g1_2 = 0
n_g2_1 = 0
n_g2_2 = 0
n_g3_1 = 0
n_g3_2 = 0
n_g4_1 = 0
n_g4_2 = 0

# Assign percentage of incoming money for each group
p_g1 = 50
p_g2 = 50
p_g3 = 50
p_g4 = 50

# Assign prize to each subgroup
e_g1_1 = 1
e_g1_2 = 2
e_g2_1 = 3
e_g2_2 = 4
e_g3_1 = 1
e_g3_2 = 2
e_g4_1 = 3
e_g4_2 = 4

# ----------------------

money_g1 = (n_g1_1 * e_g1_1 + n_g1_2 * e_g1_2) * (p_g1/100)
money_g2 = (n_g2_1 * e_g2_1 + n_g2_2 * e_g2_2) * (p_g2/100)
money_g3 = (n_g3_1 * e_g3_1 + n_g3_2 * e_g3_2) * (p_g3/100)
money_g4 = (n_g4_1 * e_g4_1 + n_g4_2 * e_g4_2) * (p_g4/100)

print(f"Total {g1} for me: {money_g1} €")
print(f"Total {g2} for me: {money_g2} €")
print(f"Total {g3} for me: {money_g3} €")
print(f"Total {g4} for me: {money_g4} €")
print(f"Total for me: {money_g1+money_g2+money_g3+money_g4} €")

money_g1_pay = (n_g1_1 * e_g1_1 + n_g1_2 * e_g1_2) * ((100 - p_g1)/100)
money_g2_pay = (n_g2_1 * e_g2_1 + n_g2_2 * e_g2_2) * ((100 - p_g2)/100)
money_g3_pay = (n_g3_1 * e_g3_1 + n_g3_2 * e_g3_2) * ((100 - p_g3)/100)
money_g4_pay = (n_g4_1 * e_g4_1 + n_g4_2 * e_g4_2) * ((100 - p_g4)/100)

print(f"Total {g1} to pay: {money_g1_pay} €")
print(f"Total {g2} to pay: {money_g2_pay} €")
print(f"Total {g3} to pay: {money_g3_pay} €")
print(f"Total {g4} to pay: {money_g4_pay} €")
print(f"Total to pay: {money_g1_pay + money_g2_pay + money_g3_pay + money_g4_pay} €")
