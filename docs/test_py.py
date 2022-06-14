year = int(input("Which year do you want to check? "))

"""HVA ER ET SKUDDÅR?
Årstall som er delelig på 4 (uten resttall). Unntatt hvis det er delelig på 100, med mindre det også er delelig på 400"""

fire = (year % 4)
print(f"fire {fire}")
hundre = (year % 100)
print(f"hundre {hundre}")
fh = (year % 400)
print(f"fh {fh}")

if fire == 0:
    print("ja delelig med 4")
    if hundre == 0:
        print("Ja, delelig med 100")
        if fh == 0:
            print("Ja, delelig med 400")
            print("Leap year B.")  #
        else:
            print("Nei, ikke delelig med 400")
            print("Not leap year 2.")
    else:
        print("Ikke delelig med 100")
        print("Leap year A.")  #
else:
    print("Ikke delelig med fire")
    print("Not leap year1.")
