"""Decline flag and 2×2 segments — no sklearn fit."""

import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.labels import decline_flag
from src.segments import assign_segment


def test_decline_flag():
    s = pd.Series(["Снизилась", "Прежний уровень", "Снизилась"])
    assert list(decline_flag(s)) == [1, 0, 1]


def test_segments_quantile_cut():
    # 10 people, q=0.7 → top 3 risk and top 3 profit
    prob = pd.Series([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    profit = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    seg = assign_segment(prob, profit, q=0.7)
    assert (seg == "high risk, high profit").sum() == 3
    assert (seg == "low risk, low profit").sum() == 7
    assert "high risk, low profit" not in set(seg)  # aligned ranks
    # misaligned: high risk, low profit exists
    profit2 = profit.iloc[::-1].reset_index(drop=True)
    seg2 = assign_segment(prob, profit2, q=0.7)
    assert (seg2 == "high risk, low profit").sum() == 3
    assert (seg2 == "low risk, high profit").sum() == 3
