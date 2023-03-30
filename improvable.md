## from_wq
* group_zscore(-(open - high)/(open - low), market)
* group_rank(-(open - high)/(open - low), market)
* group_scale(-(open - high)/(open - low), market)
* group_zscore(-(open - high)/(open - low), sector)
* group_rank(-(open - high)/(open - low), sector)
* group_zscore((open - high)/(open - low), industry)
* group_rank((open - high)/(open - low), industry)
* group_scale((open - high)/(open - low), industry)
* group_zscore((open - high)/(open - low), subindustry)
* group_rank((open - high)/(open - low), subindustry)
* group_rank((open - high)/(open - low), subindustry)
* group_zscore(-(open - high)/(open - low), market)
* group_rank(-(open - high)/(open - low), market)
* group_rank((open - high)/(open - low), sector)

## abner_try
* rank(0 - (1 * ((close - vwap) / ts_decay_linear(rank(ts_arg_max(close, 30)), 2))))
* sigmoid(0 - (1 * ((close - vwap) / ts_decay_linear(rank(ts_arg_max(close, 30)), 2))))