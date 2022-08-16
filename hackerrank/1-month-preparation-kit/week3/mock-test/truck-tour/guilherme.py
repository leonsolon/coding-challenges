def truckTour(petrolpumps):
    # Write your code here
    # print(petrolpumps)
    start = 0
    pos = 0
    end = len(petrolpumps) - 1
    petrol_level = 0
    # print(start,end)
    while end != pos:
        # print(pos, petrolpumps[pos])
        petrol_level += petrolpumps[pos][0]
        petrol_level -= petrolpumps[pos][1]
        if petrol_level < 0:
            petrol_level = 0
            start += 1
            start = start % len(petrolpumps)
            pos = start
            end = (start + len(petrolpumps) - 1)
            end = end % len(petrolpumps)
            if start == 0:
                break
            # print(start,end)
        else:
            pos += 1
            pos = pos % len(petrolpumps)

    return start

h1 = []
h1.reverse()