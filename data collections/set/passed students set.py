total={"chikku","parvathy","megha","miza","clara","emy"}
passed=set()
print(total,"total students")
failed={"clara","emy"}
print("failed", failed)

for i in total:
    if i not in failed:
        passed.add(i)  #adding elements from total to new set passed
print(passed,"passed students")

