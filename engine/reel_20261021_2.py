"""Stop sending 'just checking in' -- follow up with something useful instead."""
from reel_chat import *

ACC = (190, 130, 255)   # violet
GOLD = (255, 214, 92)
RED = (255, 96, 110)
bg = Background(top=(26, 10, 44), bottom=(58, 20, 74), blobs=[(170, 80, 255), (255, 80, 150), (90, 90, 255)], seed=2952)


def crossed_bubble(sub, t, start, cy, txt, strike_at, size=60):
    k = p(t, start, 0.4)
    if k <= 0: return
    d = ImageDraw.Draw(sub)
    f = font(F_SEMI, size)
    tw = d.textlength(txt, font=f)
    w, h = tw + 100, size + 70
    s = out_back(k)
    x0, y0 = W / 2 - w * s / 2, cy - h * s / 2
    al = int(255 * out_cubic(k))
    d.rounded_rectangle([x0, y0, x0 + w * s, y0 + h * s], radius=40 * s, fill=(0, 132, 255, al))
    draw_text(sub, txt, F_SEMI, size, W / 2, cy, WHITE, alpha=out_cubic(k), scale=s)
    ks = p(t, strike_at, 0.35)
    if ks > 0:
        d.line([x0 - 20, cy, x0 - 20 + (w + 40) * out_cubic(ks), cy], fill=(*RED, 255), width=14)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Stop sending this", "to clients"], t, 0.0, 520, 96, (WHITE, RED), gap=0.08, highlight={"stop"})
        crossed_bubble(sub, t, 0.4, 860, "Just checking in 👋".replace(" 👋", ""), 1.2)
        kx = p(t, 1.3, 0.35)
        place_emoji(sub, "🚫", W / 2 + 330, 760, 120 * out_back(kx), alpha=out_cubic(kx))
        kp = p(t, 1.9, 0.4)
        pill(sub, W / 2, 1110, "Send this instead", F_BLACK, 58, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(50, 24), icon="👇")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Why it gets", "ignored"], t, s1 + 0.1, 330, 96, (WHITE, RED), gap=0.08, highlight={"ignored"})
        checklist(sub, t, s1 + 0.8, ["It asks for their time", "It gives nothing new", "It's easy to skip"], 660, 160, ACC, size=58, x0=200, every=0.8, icon="❌")
        kp = p(t, s1 + 3.6, 0.4)
        pill(sub, W / 2, 1220, "Fix: every follow-up adds value", F_XB, 48, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="💡")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Before vs after"], t, s2 + 0.1, 290, 92, (WHITE, GOLD), gap=0.08, highlight={"after"})
        phone_chat(sub, t, s2 + 0.3, W / 2, 380, [
            ("me", "Just checking in!", s2 + 0.4, "Before"),
            ("me", "Hi Sam! Saw your new fall menu. Tip: shoot the photos next to a window, it fixes the dark look. Want 2 more quick ideas?", s2 + 1.6, "typed"),
        ], header="Sam's Cafe", h=780)
        kx = p(t, s2 + 1.0, 0.3)
        if kx > 0:
            ImageDraw.Draw(sub).line([540, 612, 905, 612], fill=(*RED, int(255 * out_cubic(kx))), width=10)
        labels = [("💡", "A useful tip"), ("❓", "One easy question")]
        for i, (ic, lab) in enumerate(labels):
            kk = p(t, s2 + 4.6 + i * 0.8, 0.4)
            pill(sub, W / 2, 1290 + i * 125, lab, F_XB, 50, GOLD if i else (245, 246, 250), INK, alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["3 things to add", "in 5 minutes"], t, s3 + 0.1, 330, 92, (WHITE, ACC), gap=0.08, highlight={"3", "5", "minutes"})
        opts = [("📸", "A quick tip for their photos"), ("🎨", "A rough Canva mockup"), ("🔗", "A free tool that helps them")]
        for i, (ic, lab) in enumerate(opts):
            kk = p(t, s3 + 0.9 + i * 0.7, 0.4)
            pill(sub, W / 2, 620 + i * 160, lab, F_XB, 50, (245, 246, 250), INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(46, 28), icon=ic)
        notification(sub, t, s3 + 3.6, 1180, "Sam's Cafe", "Oh nice, yes please!", icon="☕")
        draw_text(sub, "Example message. Results depend on your work.", F_MED, 34, W / 2, 1370, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
