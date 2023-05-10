#3 task
casino_blacklist = ['Franklin Gates', 'Jeremy Gallagher', 'Kylie Valdez', 'Ellena Petty', 'Tahlia Cuevas', 'Keane Lane' ]
poker_blacklist = ['Genevieve Owens', 'Ellena Petty', 'Kylie Valdez', 'Franklin Gates', 'Shawn Gutierrez', 'Asad Villega', 'Stella Mays']
alcohol_blacklist = ['Kylie Valdez', 'Lawrence Calhoun', 'Ellena Petty','Zaina Holland', 'Franklin Gates', 'Anna Payne', 'Ruby Hatfield']
casino_set = set(casino_blacklist)
poker_set = set(poker_blacklist)
alcohol_set = set(alcohol_blacklist)
common_set = casino_set.intersection(poker_set, alcohol_set)
print("The people on all three blacklists are:")
print("\n".join(common_set))
