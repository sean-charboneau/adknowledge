def run_overlap_report():
    counts = {}
    filenames = [
        "1137.log",
        "1138.log",
        "1139.log",
        "1140.log",
        "1141.log",
        "1142.log",
        "1266.log",
        "1267.log",
        "1268.log",
        "1269.log"
        ]
    for file in filenames:
        with open("user_ids/" + file) as f:
            uniques = {}
            for line in f:
                if line not in uniques:
                    uniques[line] = True
            for line in uniques:
                if line in counts:
                    counts[line] += 1
                else:
                    counts[line] = 1
    ret = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for key in counts:
        ret[counts[key]] += 1
    return ret
