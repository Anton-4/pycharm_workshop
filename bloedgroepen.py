# the same blood group occurs for multiple configurations of alleles
poss_alleles_for_group = {"A": [("A", "A"), ("A", "O")],"AB": [("A", "B")],"B": [("B", "B"), ("B", "O")],"O": [("O", "O")],"+": [("+", "+"), ("+", "-")],"-": [("-", "-")],"?": [("?", "?")],"": [("?", "?")],}
# get the blood group given two alleles
group_from_2_alleles = {("A", "A"): "A",("A", "O"): "A",("A", "B"): "AB",("B", "B"): "B",("B", "O"): "B",("O", "O"): "O",("+", "+"): "+",("+", "-"): "+",("-", "-"): "-",}
# all possible blood groups
poss_parents = ["A+", "A-", "AB+", "AB-", "B+", "B-", "O+", "O-"]

# calculate the possible blood groups for the missing parent or child
def calcGroup(par_one, par_two, child):
    par_list = []
    if par_one== "?":
        for i in poss_parents:
            if child in submit_parents(i, par_two):
                par_list.append(i)
        par_list = sorted(par_list, key=cmp_to_key(cmp_fun))
        ans_list="{"+",".join(par_list) + "}"
        if len(par_list) == 0:
            ans_list = "ONMOGELIJK"
        return ans_list+" "+par_two+" "+child
    elif par_two == "?":
        for i in poss_parents:
            if child in submit_parents(par_one, i):
                par_list.append(i)
        par_list=sorted(par_list, key=cmp_to_key(cmp_fun))
        ans_list="{" + ",".join(par_list) + "}"
        if len(par_list)==0:
            ans_list="ONMOGELIJK"
        return par_one+ " " +ans_list+ " " + child
    else:
        return generate_answer(
            submit_parents(par_one, par_two), par_one + " " + par_two + " ?"
        )
# find all possible allele configurations for a child given parents blood group
def submit_parents(par_one, par_two):
    par_one_group = poss_alleles_for_group.get(par_one[0:-1])
    par_one_rhesus = poss_alleles_for_group.get(par_one[-1])
    par_two_group = poss_alleles_for_group.get(par_two[0:-1])
    par_two_rhesus = poss_alleles_for_group.get(par_two[-1])
    possible_groups = []
    rhesus_groups = []
    for i in par_one_group:
        for k in i:
            for j in par_two_group:
                for z in j:
                    possible_groups.append(k + z)
    for i in par_one_rhesus:
        for k in i:
            for j in par_two_rhesus:
                for z in j:
                    rhesus_groups.append(k + z)
    final_rhesus_groups = restore_rhesus(rhesus_groups)
    final_groups = restore_list(possible_groups)
    return get_type_list(final_groups, final_rhesus_groups)
def generate_answer(type_list, question):
    ans_list = "{"
    for i in type_list:
        ans_list += i + ","
    ans_list = ans_list[0:-1]
    ans_list += "}"
    if len(ans_list) < 6:
        ans_list = ans_list[1:-1]
    return question.replace("?", ans_list)
# function used for sorting of output
def cmp_fun(x: str, y: str):
    if x == y:
        return 0
    elif x[:-1] == y[:-1]:
        if x[-1] == "-":
            return 1
        else:
            return -1
    else:
        if x < y:
            return -1
        else:
            return 1
# allow cmp function to be used as key function
def cmp_to_key(my_cmp):
    "Convert a cmp= function into a key= function"
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return my_cmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return my_cmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return my_cmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return my_cmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return my_cmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return my_cmp(self.obj, other.obj) != 0
    return K
# combine all possible blood groups with all possible rhesus groups
def get_type_list(possible_groups, rhesus_groups):
    type_list = []
    for i in possible_groups:
        for j in rhesus_groups:
            type_list.append(i + j)
    type_list = list(set(type_list))
    return type_list
def restore_rhesus(rhesus_groups):
    for i in range(0, len(rhesus_groups)):
        temp_lst = list(rhesus_groups[i])
        temp_lst.sort()
        temp_lst = list(set(temp_lst))
        if len(temp_lst) == 2:
            temp_lst = "+"
        else:
            temp_lst = "-"
        rhesus_groups[i] = temp_lst
    return list(set(rhesus_groups))
# convert allele config into blood group, for example: ["A","B"] into "AB", ["A", "O"] into "A"...
def restore_list(possible_groups):
    final_groups = []
    for i in range(0, len(possible_groups)):
        temp_lst = list(possible_groups[i])
        if temp_lst == ["A", "B"]:
            temp_lst = "AB"
        elif "A" in temp_lst:
            temp_lst = "A"
        elif "B" in temp_lst:
            temp_lst = "B"
        else:
            temp_lst = "O"
        final_groups.append(temp_lst)
    return list(set(final_groups))
