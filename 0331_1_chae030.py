while (1) :
    a = input()
    if a == "# 0 0" :
        break
    n_a_w = []
    n_a_w = a.split(" ")
    if int(n_a_w[1]) > 17 or int(n_a_w[2]) >= 80 :
        n_a_w.append("Senior")
    else :
        n_a_w.append("Junior")
    print(n_a_w[0], n_a_w[3])