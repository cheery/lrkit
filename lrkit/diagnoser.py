def diagnose(results):
    if len(results.conflicts) > 0:
        for index, sym, conflict in results.conflicts:
            print("conflict in simulating itemset")
            for item in results.kernelsets[index]:
                print("  {}".format(item))
            print("at {}".format(sym))
            for obj in conflict:
                if isinstance(obj, int):
                    print("  shift {} ".format(sym))
                    for item in results.kernelsets[obj]:
                        print("    {}".format(item))
                else:
                    print("  reduce {}".format(sym))
                    print("    ".format(obj))
            print("")
    else:
        print("no conflicts")
