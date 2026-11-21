import math

def drift(audio_ts, video_ts):
    """音画偏差。"""
    return audio_ts - video_ts

def audio_time(samples, rate):
    """按采样计数。"""
    return samples / rate

def resample_ratio(nominal, actual):
    """重采样比率。"""
    return nominal / actual

def on_drop(pts, frame_dur):
    """丢帧顺延。"""
    return pts + frame_dur

def seek_sync(pos):
    """seek 同步重置。"""
    return (pos, pos)

def speed_scale(ts, rate):
    """倍速缩放。"""
    return ts / rate

def latency(ts, delay):
    """延迟补偿。"""
    return ts - delay

def freeze(clock, frozen):
    """重建期冻结。"""
    return clock

def eof_end(audio_end, video_end):
    """EOF 等待。"""
    return max(audio_end, video_end)

def clamp_drift(value, limit):
    """偏差钳制。"""
    return max(-limit, min(limit, value))

def frames_time(frames, fps):
    """帧数转时间。"""
    return frames / fps

def time_frames(seconds, fps):
    """时间转帧。"""
    return int(seconds * fps)

def sync_key(audio, video):
    """同步键。"""
    return f"{audio}:{video}"

def is_synced(value, tolerance):
    """同步判定。"""
    return abs(value) <= tolerance

def correct(pts, value):
    """校正时间戳。"""
    return pts + value
