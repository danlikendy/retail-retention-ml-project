"""Four buckets: model risk × profit. Thresholds are quantiles, not magic constants."""

from __future__ import annotations

import pandas as pd

HIGH_RISK = "high risk"
LOW_RISK = "low risk"
HIGH_PROFIT = "high profit"
LOW_PROFIT = "low profit"


def assign_segment(
    probability: pd.Series,
    profit: pd.Series,
    q: float = 0.7,
) -> pd.Series:
    """q-quantile of each series. Independent cuts, then four labels."""
    p_cut = probability.quantile(q)
    m_cut = profit.quantile(q)
    risk = pd.Series(LOW_RISK, index=probability.index)
    risk = risk.mask(probability >= p_cut, HIGH_RISK)
    money = pd.Series(LOW_PROFIT, index=profit.index)
    money = money.mask(profit >= m_cut, HIGH_PROFIT)
    return risk + ", " + money
