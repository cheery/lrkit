def diagnose(results):
    if len(results.conflicts) > 0:
        for index, sym, conflict in results.conflicts:
            print "conflict in simulating itemset"
            for item in results.kernelsets[index]:
                print "  ", item
            print "at {}".format(sym)
            for obj in conflict:
                if isinstance(obj, int):
                    print "  ", "shift {} ".format(sym)
                    for item in results.kernelsets[obj]:
                        print "     ", item
                else:
                    print "  ", "reduce {} ".format(sym)
                    print "     ", obj
            print
    else:
        print "no conflicts"
