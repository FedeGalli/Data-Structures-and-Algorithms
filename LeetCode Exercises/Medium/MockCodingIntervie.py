def findBestPlace(blocks, pref):

    structures_count = {}
    for i, block in enumerate(blocks):

        count = 0

        for building in pref:

            if block[building] == 1:
                count += 1
        
        if count not in structures_count:
            structures_count[count] = [i]
        else:
            structures_count[count].append(i)