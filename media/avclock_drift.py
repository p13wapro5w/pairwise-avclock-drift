import math

def drift(audio_ts, video_ts):
    """音画偏差。"""
    raise NotImplementedError("TODO: drift")

def audio_time(samples, rate):
    """按采样计数。"""
    raise NotImplementedError("TODO: audio_time")

def resample_ratio(nominal, actual):
    """重采样比率。"""
    raise NotImplementedError("TODO: resample_ratio")

def on_drop(pts, frame_dur):
    """丢帧顺延。"""
    raise NotImplementedError("TODO: on_drop")

def seek_sync(pos):
    """seek 同步重置。"""
    raise NotImplementedError("TODO: seek_sync")

def speed_scale(ts, rate):
    """倍速缩放。"""
    raise NotImplementedError("TODO: speed_scale")

def latency(ts, delay):
    """延迟补偿。"""
    raise NotImplementedError("TODO: latency")

def freeze(clock, frozen):
    """重建期冻结。"""
    raise NotImplementedError("TODO: freeze")

def eof_end(audio_end, video_end):
    """EOF 等待。"""
    raise NotImplementedError("TODO: eof_end")

def clamp_drift(value, limit):
    """偏差钳制。"""
    raise NotImplementedError("TODO: clamp_drift")

def frames_time(frames, fps):
    """帧数转时间。"""
    raise NotImplementedError("TODO: frames_time")

def time_frames(seconds, fps):
    """时间转帧。"""
    raise NotImplementedError("TODO: time_frames")

def sync_key(audio, video):
    """同步键。"""
    raise NotImplementedError("TODO: sync_key")

def is_synced(value, tolerance):
    """同步判定。"""
    raise NotImplementedError("TODO: is_synced")

def correct(pts, value):
    """校正时间戳。"""
    raise NotImplementedError("TODO: correct")
