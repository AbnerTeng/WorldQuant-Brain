from database import PRICES, VOLUMES, TS_OP_1D1P, UNARY_OP, one_OP_one, OP_one

def price_vs_volume():
    D1 = [1, 5, 10, 50]
    D2 = [1, 5, 10, 50]
    commands = []
    for price in PRICES:
        for volume in VOLUMES:
            for ts_op_1d1p in TS_OP_1D1P:
                for unary in UNARY_OP:
                    for one_op_one in one_OP_one:
                        for op_one in OP_one:
                            for d1 in D1:
                                for d2 in D2:
                                    command = f'{unary}{ts_op_1d1p}({op_one}(ts_median({price}, {d1}) {one_op_one} ts_median({volume}, {d1})), {d2})'
                                    commands.append(command)
    return commands


def volume_vs_price():
    D1 = [1, 5, 10, 50]
    D2 = [1, 5, 10, 50]
    commands = []
    for price in PRICES:
        for volume in VOLUMES:
            for ts_op_1d1p in TS_OP_1D1P:
                for unary in UNARY_OP:
                    for one_op_one in one_OP_one:
                        for op_one in OP_one:
                            for d1 in D1:
                                for d2 in D2:
                                    command = f'{unary}{ts_op_1d1p}({op_one}(ts_median({volume}, {d1}) {one_op_one} ts_median({price}, {d1})), {d2})'
                                    commands.append(command)
    return commands