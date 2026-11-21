import pytest
import math
from media import avclock_drift as mod

CASES = [
    ("drift", 'm.drift(2, 1.5) == approx(0.5)'),
    ("samples", 'm.audio_time(48000, 48000) == 1'),
    ("ratio", 'm.resample_ratio(48000, 48002) == approx(0.999958, abs=1e-5)'),
    ("drop", 'm.on_drop(1, 0.04) == approx(1.04)'),
    ("seek", 'm.seek_sync(3) == (3, 3)'),
    ("speed", 'm.speed_scale(2, 2) == 1'),
    ("latency", 'm.latency(1, 0.2) == approx(0.8)'),
    ("freeze", 'm.freeze(1.5, True) == 1.5'),
    ("eof", 'm.eof_end(10, 10.2) == 10.2'),
    ("clamp", 'm.clamp_drift(0.5, 0.3) == 0.3'),
    ("frames", 'm.frames_time(24, 24) == 1'),
    ("time", 'm.time_frames(1, 24) == 24'),
    ("key", 'm.sync_key(1, 2) == "1:2"'),
    ("synced", 'm.is_synced(0.05, 0.1) is True'),
    ("correct", 'm.correct(1, 0.2) == approx(1.2)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
