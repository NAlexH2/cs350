print("X1 and Y1 are the co-ordinates of the farthest point from the dividing line\n"
      "of your convex hull. X2 and Y2 are either of your points farthest apart on the\n"
      "hull. X3 and Y3 are the points you are trying to find out if where if T > 0.\n"
      "If t > 0 then your point is on the convex hull.\n\nGo!\n\n")

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))
    
print(f"t = {(((x1*y2)+(x2*y3)+(x3+y1))-((x2*y1)+(x3*y2)+(x1*y3)))}")

 # for i in range(len(l)):
    #     if l[i] not in lrp and l[i][1] < lrp[0][1] and l[i][1] < lrp[1][1]:
    #         lower.append(l[i])
    #     if l[i] not in lrp and l[i][1] > lrp[0][1] and l[i][1] > lrp[1][1]:
    #         upper.append(l[i])