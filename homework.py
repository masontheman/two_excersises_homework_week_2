def list_comprehension(listt):
    print([i for i in listt if i < 10])
def list_comprehension_two(listtt):
    print({i.title() for i in listtt if type(i) is str and len(i) >= 4})