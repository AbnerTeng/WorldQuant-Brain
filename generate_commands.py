from tkinter.ttk import Scale
from database import GROUP_DT, GROUP_OP_1D1P, PRICES, TS_OP_1D2P, VOLUMES, TS_OP_1D1P, UNARY_OP, one_OP_one, OP_one, P_or_M

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

def scale_and_corr():
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
                                    for ts_op_1d2p in TS_OP_1D2P:
                                        command = f'(scale(((ts_sum({price}, {d1}){one_op_one}{d1})-{price})) + (20*scale(ts_corr({price}, ts_delay({price}, {d2}), 230))))'
                                        commands.append(command)
    return commands

def from_wq():
    commands = []
    for price1 in PRICES:
        for price2 in PRICES:
            if price1 == price2:
                continue
            for price3 in PRICES:
                for price4 in PRICES:
                    if price3 == price4:
                        continue
                    if price1 == price3 and price2 == price4:
                        continue
                    for p_or_m in P_or_M:
                        for group in GROUP_DT:
                            for group_op in GROUP_OP_1D1P:
                                command = f'{group_op}({p_or_m}({price1} - {price2})/({price3} - {price4}), {group})'
                                commands.append(command)
    return commands