# 1 вариант
var_1 = 37
var_2 = 99
var_1 = 99
var_2 = 37
print("var_1 =", var_1,"var_2 =", var_2)

# 2 вариант
var_1 = 37
var_2 = 99
var_1,var_2 = var_2,var_1
print("var_1 =", var_1,"var_2 =", var_2)

# 3 вариант
var_1 = 37
var_2 = 99
v_1 = var_1
var_1 = var_2
var_2 = v_1
print("var_1 =", var_1,"var_2 =", var_2)