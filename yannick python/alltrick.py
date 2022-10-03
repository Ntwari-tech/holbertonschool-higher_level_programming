# #!/usr/local/bin/python3:
# a, b = 0, 1
# while b < 15:
# print(b)
# a, b = b, a+b
#open_string = "Sammy loves {}."
#print(open_string.format("open source"))

open_string = "Sammy loves {} {}."
print(open_string.format("open source", "this software"))

#open_string2 = "jacs loves  {} {} and {} and {} "
#print(open_string2.format("naps", "food", "these nuts", " i love it" ))

# print("jacs loves {}, {}, {}, {}"). format("naps", "food", dk = " these nuts", "and i love it ")
# print("this girl is {it},{1}, {2}, {4}".format(it = "intense", "unappreciative", "crazy").
print("next time jacs sees this old while man {0:d} % {1}".format(
    99, "gonna be sight"))
using(start iterator)
new_jacs = "pregnant with  {} baby "
3	baby = 1
4 for i in range(6):
5 print(new_jacs.format(baby))


#using (start, stop, step)
for i in range(15, 30, 5):
    print(new_jacs.format(baby))

# using list[ "+, *" operator with "=" compound form and delete]
ntwari_fam = ["Andy", "serge", "gaju", "igor", "ana", "kev"]
for y in range(1, 15):
    ntwari_fam += ['patrick']  # ntwari_fam + ['patrick'],
    del ntwari_fam[5]
    print(ntwari_fam)

def scopes_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
