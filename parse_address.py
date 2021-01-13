

def parse_address(address):
    address_words = address.split()
    address_words_len = len(address_words)
    line1 = line2 = city = state = zipcode = ""
    line1_done = line1_done = False
    index_city_start = None
    index_state = address_words_len - 2
    index_zip = address_words_len - 1
    for i in range(0, address_words_len):
        word = address_words[i]

        # line1
        if line1_done is not True:
            line1 += "{w} ".format(w=word)
        if word in ['St', 'Dr', 'Ave', 'Plaza']:
            line1_done = True
            index_city_start = i + 1
        else:
            index_city_start = None

        # line2
        if word in ['Suite', 'Unit']:
            line2 += "{w} {nw}".format(w=word, nw=address_words[i+1])
            index_city_start = i + 2

        # city
        if index_city_start is not None:
            city = ""
            for i in range(index_city_start, index_state):
                city += "{w} ".format(w=address_words[i])

        # state
        if i == index_state:
            state = word

        # zip
        if i == index_zip:
            zipcode = word

    print("line1: {l1}".format(l1=line1))
    print("line2: {l2}".format(l2=line2))
    print("city: {c}".format(c=city))
    print("state: {s}".format(s=state))
    print("zip: {z}".format(z=zipcode))
    print()


parse_address("185 Meadow Ave Unit 2234 San Antonio TX 78154")
parse_address("18534 Martin Luther King Dr Austin TX 78154-1233")
parse_address("185 Meadow Ave Unit 2234 Dallas TX 78154")
