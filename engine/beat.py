"""Synthesize an original, royalty-free upbeat background track (no samples used)."""
import sys, wave
import numpy as np

SR = 44100

def env(n, a, d):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)
    return e

def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x); acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y

def make(dur=30.0, bpm=118, seed=7, out="beat.wav", root=57):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    mix = np.zeros(n); duck = np.ones(n)
    beat = 60 / bpm
    # chord progression (semitones from root): i - VI - III - VII
    prog = [[0, 3, 7], [-4, 0, 3], [3, 7, 10], [-2, 2, 5]]
    bass_roots = [0, -4, 3, -2]
    f = lambda m: 440 * 2 ** ((m - 69) / 12)
    nbeats = int(dur / beat) + 1
    # kick
    kl = int(0.4 * SR); tk = np.arange(kl) / SR
    kick = np.sin(2 * np.pi * np.cumsum(45 + 90 * np.exp(-tk * 30)) / SR) * np.exp(-tk * 9)
    # clap
    cl = int(0.22 * SR)
    clap = lowpass(rng.standard_normal(cl), 3500) * env(cl, 0.002, 0.06)
    # hat
    hl = int(0.06 * SR)
    hn = rng.standard_normal(hl); hat = (hn - lowpass(hn, 7000)) * env(hl, 0.001, 0.015)
    for b in range(nbeats):
        s = int(b * beat * SR)
        if s >= n: break
        intro = b < 4
        if not intro:
            e = min(n, s + kl); mix[s:e] += 0.9 * kick[: e - s]
            dl = min(n, s + int(0.25 * SR)); duck[s:dl] = np.minimum(duck[s:dl], np.linspace(0.35, 1, dl - s))
        if b % 2 == 1 and not intro:
            e = min(n, s + cl); mix[s:e] += 0.45 * clap[: e - s]
        for h in (0, 0.5):
            hs = int((b + h) * beat * SR)
            if hs < n and b >= 2:
                e = min(n, hs + hl); mix[hs:e] += (0.16 if h else 0.08) * hat[: e - hs]
    # pads + bass, one chord per bar
    bar = 4 * beat
    pad = np.zeros(n); bass = np.zeros(n)
    nbars = int(dur / bar) + 1
    for k in range(nbars):
        s = int(k * bar * SR); e = min(n, int((k + 1) * bar * SR))
        if s >= n: break
        t = np.arange(e - s) / SR
        ch = prog[k % 4]
        for m in ch:
            fr = f(root + 12 + m)
            pad[s:e] += (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * fr * t)) * 0.06
        a = np.minimum(1, t / 0.08) * np.minimum(1, (t[-1] - t + 1e-3) / 0.08)
        pad[s:e] *= a
        # bass eighth notes
        bf = f(root - 12 + bass_roots[k % 4])
        for q in range(8):
            qs = s + int(q * beat / 2 * SR); qe = min(e, qs + int(beat / 2 * SR * 0.85))
            if qs >= e: break
            tq = np.arange(qe - qs) / SR
            saw = 2 * ((bf * tq) % 1) - 1
            bass[qs:qe] += saw * 0.22 * np.exp(-tq * 4)
    bass = lowpass(bass, 380)
    mix += (pad + bass) * duck
    # master: fade in/out, soft clip, normalize
    fi = int(0.6 * SR); fo = int(1.5 * SR)
    mix[:fi] *= np.linspace(0, 1, fi); mix[-fo:] *= np.linspace(1, 0, fo)
    mix = np.tanh(mix * 1.4)
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.5
    st = np.stack([mix, mix], axis=1)
    with wave.open(out, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())
    return out

if __name__ == "__main__":
    make(out=sys.argv[1] if len(sys.argv) > 1 else "beat.wav", seed=int(sys.argv[2]) if len(sys.argv) > 2 else 7)
