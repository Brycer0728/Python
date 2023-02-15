for index in range(5):
    #print("Called from within a for-in loop")
    if index % 2 == 0: continue
    #if index == 2: break
    print(f"{index} - iteration count {index + 1}")

