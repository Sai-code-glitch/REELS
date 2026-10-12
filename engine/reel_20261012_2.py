"""Stop waiting on Fiverr orders: find local clients on Google Maps."""
from reel_common import *

ACC = (255, 176, 50)    # amber
GOLD = (255, 224, 120)
GREEN = (70, 210, 130)
RED = (255, 90, 90)
bg = Background(top=(30, 16, 6), bottom=(52, 28, 10), blobs=[(255, 150, 40), (255, 90, 60), (60, 160, 140)], seed=83)


def dashboard(sub, cx, cy, t, start):
    w, h = 820, 420
    k = out_back(p(t, start, 0.5))
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=(250, 250, 252, 255))
    d.text((40, 55), "My gig · Orders this week", font=font(F_XB, 40), fill=INK, anchor="lm")
    days = "MTWTFSS"
    for i, ch in enumerate(days):
        x = 90 + i * 105
        hh = 10 + 6 * math.sin(t * 3 + i) * p(t, start + 0.6, 0.5)
        d.rounded_rectangle([x - 30, 330 - hh, x + 30, 330], radius=8, fill=(200, 206, 220, 255))
        d.text((x, 370), ch, font=font(F_SEMI, 32), fill=(130, 136, 150, 255), anchor="mm")
    kz = p(t, start + 1.0, 0.4)
    if kz > 0:
        d.text((w / 2, 200), "0 orders", font=font(F_BLACK, 96), fill=(*RED, int(255 * out_cubic(kz))), anchor="mm")
    card = card.resize((int(w * k), int(h * k)))
    sub.alpha_composite(card, (int(cx - card.width / 2), int(cy - card.height / 2)))


def maps_listing(sub, cx, cy, t, start):
    w, h = 820, 520
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(250, 250, 252, 255))
    d.rounded_rectangle([30, 26, w - 30, 100], radius=37, fill=(236, 238, 244, 255))
    typed = "bakery near me"[: int(len("bakery near me") * p(t, start + 0.3, 0.8))]
    d.text((70, 63), "🔍" if False else "Search:", font=font(F_SEMI, 34), fill=(130, 136, 150, 255), anchor="lm")
    d.text((200, 63), typed, font=font(F_SEMI, 36), fill=INK, anchor="lm")
    kl = out_cubic(p(t, start + 1.2, 0.4))
    if kl > 0:
        a = int(255 * kl)
        d.rounded_rectangle([30, 130, 230, 300], radius=20, fill=(225, 210, 190, a))
        d.text((130, 215), "1 photo", font=font(F_SEMI, 30), fill=(140, 120, 100, a), anchor="mm")
        d.text((260, 160), "Corner Bakery", font=font(F_XB, 46), fill=(*INK, a), anchor="lm")
        d.text((260, 215), "★★★★½  4.6 · Bakery", font=font(DEJAVU, 32), fill=(240, 160, 30, a), anchor="lm")
        d.text((260, 265), "Open · closes 6 PM", font=font(F_MED, 32), fill=(40, 150, 80, a), anchor="lm")
    flags = [("No website listed", 2.0), ("Only 1 old photo", 2.6), ("Owner never replies to reviews", 3.2)]
    for i, (lab, at) in enumerate(flags):
        kk = out_cubic(p(t, start + at, 0.35))
        if kk <= 0: continue
        y = 345 + i * 58
        d.text((40 + 30 * (1 - kk), y), "✗", font=font(DEJAVU, 40), fill=(*RED, int(255 * kk)), anchor="lm")
        d.text((90 + 30 * (1 - kk), y), lab, font=font(F_SEMI, 38), fill=(*INK, int(255 * kk)), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 80 * (1 - out_cubic(k)))))


def email(sub, cx, cy, t, start):
    w, h = 840, 520
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=(250, 250, 252, 255))
    d.text((40, 50), "To: Corner Bakery", font=font(F_MED, 32), fill=(130, 136, 150, 255), anchor="lm")
    d.text((40, 105), "Quick fix for your Google listing", font=font(F_XB, 40), fill=INK, anchor="lm")
    d.line([40, 145, w - 40, 145], fill=(225, 228, 236, 255), width=3)
    lines = ["Hi! Your listing has no website", "and 1 photo. I can add photos,", "hours + a simple page this week.", "Want me to send 2 quick ideas?"]
    for i, ln in enumerate(lines):
        kk = out_cubic(p(t, start + 0.5 + i * 0.45, 0.3))
        d.text((40, 195 + i * 58), ln, font=font(F_SEMI, 38), fill=(*INK, int(255 * kk)), anchor="lm")
    ks = p(t, start + 2.6, 0.35)
    if ks > 0:
        d.rounded_rectangle([w - 230, h - 70, w - 40, h - 20], radius=25, fill=(30, 120, 255, int(255 * out_cubic(ks))))
        d.text((w - 135, h - 45), "Send", font=font(F_XB, 32), fill=(255, 255, 255, int(255 * out_cubic(ks))), anchor="mm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.35)
        place_emoji(sub, "🛑", W / 2, 540 - 18 * math.sin(t * 6), 190 * out_back(k), alpha=k)
        pop_words(sub, ["Stop waiting", "on Fiverr orders.", "Do this instead"], t, 0.0, 980, 102, (WHITE, ACC), gap=0.07, highlight={"stop", "instead"})
        pill(sub, W / 2, 1370, "Clients are on Google Maps", F_SEMI, 46, WHITE, INK, alpha=out_cubic(p(t, 1.4, 0.4)), scale=out_back(p(t, 1.4, 0.4)), icon="📍")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Waiting for orders", "is not a plan"], t, s1 + 0.1, 360, 84, (WHITE, RED), gap=0.07, highlight={"not"})
        dashboard(sub, W / 2, 740, t, s1 + 0.6)
        tags = [("New gigs get buried", 2.6, "🫥"), ("You can't control traffic", 3.4, "🎲")]
        for i, (lab, at, ic) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1080 + i * 118, lab, F_SEMI, 46, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Find a business with", "a fixable problem"], t, s2 + 0.1, 340, 80, (WHITE, ACC), gap=0.07, highlight={"fixable", "problem"})
        maps_listing(sub, W / 2, 770, t, s2 + 0.5)
        checklist(sub, t, s2 + 4.6, ["Search any local niche", "Pick ONE thing to fix"], 1160, 105, ACC, size=50, x0=170, every=0.8)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Send a 4-line email"], t, s3 + 0.1, 330, 88, (WHITE, GOLD), highlight={"4-line"})
        email(sub, W / 2, 680, t, s3 + 0.4)
        k2 = p(t, s3 + 3.4, 0.4)
        draw_text(sub, "Example: listing refresh", F_XB, 50, W / 2, 1030, WHITE, alpha=out_cubic(k2))
        k3 = p(t, s3 + 3.6, 1.4)
        if k3 > 0:
            draw_text(sub, f"${int(round(150 * out_cubic(k3)))}", F_BLACK, 170, W / 2, 1175, GOLD, alpha=out_cubic(p(t, s3 + 3.6, 0.3)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1340, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
