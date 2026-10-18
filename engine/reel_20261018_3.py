"""Never paste this into a free AI tool (Free AI for freelancers, part 3)."""
from reel_common import *

ACC = (60, 220, 200)    # teal
GOLD = (255, 214, 100)
GREEN = (80, 220, 150)
RED = (255, 88, 104)
bg = Background(top=(6, 24, 30), bottom=(10, 44, 48), blobs=[(40, 200, 190), (255, 80, 100), (60, 120, 255)], seed=2933)

NEVER = [("🔑", "Passwords + logins"), ("📇", "Client's customer list"), ("📄", "Private contracts")]
SAFE = ["Use placeholders, not real names", "Check the tool's data settings", "Not sure? Ask the client first"]
ORIG = ["Email for Sarah Lee,", "412 Oak St. Her order", "#88213 is late."]
SWAP = ["Email for [CUSTOMER],", "[ADDRESS]. Her order", "[ORDER #] is late."]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = clamp(p(t, 0.0, 0.3) + 0.4)
        place_emoji(sub, "⛔", W / 2, 500 + 8 * math.sin(t * 6), 200 * out_back(k), alpha=k)
        pop_words(sub, ["Never paste", "this into a", "free AI tool"], t, -0.25, 930, 116, (WHITE, RED), gap=0.07, highlight={"never", "this"})
        kk = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1320, "Freelancers, read this first", F_SEMI, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="⚠️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Keep these OUT", "of AI chats"], t, s1 + 0.1, 330, 88, (WHITE, RED), gap=0.07, highlight={"out"})
        for i, (em, lab) in enumerate(NEVER):
            k = p(t, s1 + 1.0 + i * 0.9, 0.4)
            if k <= 0: continue
            y = 600 + i * 210
            x = 120 + int(60 * (1 - out_cubic(k)))
            row = Image.new("RGBA", (840, 170), (0, 0, 0, 0)); rd = ImageDraw.Draw(row)
            rd.rounded_rectangle([0, 0, 839, 169], radius=44, fill=(255, 255, 255, 245))
            e = emoji_img(em, 76); row.alpha_composite(e, (36, int(85 - e.height / 2)))
            rd.text((140, 85), lab, font=font(F_XB, 48), fill=(*INK, 255), anchor="lm")
            sub.alpha_composite(with_alpha(row, out_cubic(k)), (x, y))
            kx = p(t, s1 + 1.4 + i * 0.9, 0.3)
            place_emoji(sub, "❌", x + 770, y + 85, 90 * out_back(kx), alpha=out_cubic(kx))
        kk = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1330, "It's your client's data, not yours", F_XB, 44, RED, WHITE, alpha=out_cubic(kk), scale=out_back(kk), icon="🔒")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Swap the details", "before you paste"], t, s2 + 0.1, 300, 80, (WHITE, ACC), gap=0.07, highlight={"swap"})
        kb = p(t, s2 + 0.8, 0.45)
        if kb > 0:
            box = Image.new("RGBA", (840, 470), (0, 0, 0, 0)); bd = ImageDraw.Draw(box)
            bd.rounded_rectangle([0, 0, 839, 469], radius=40, fill=(255, 255, 255, 250))
            sw = p(t, s2 + 3.0, 0.6)
            label = "Before" if sw < 0.5 else "After"
            bd.rounded_rectangle([40, 34, 240, 96], radius=30, fill=(*(RED if sw < 0.5 else GREEN), 255))
            bd.text((140, 65), label, font=font(F_BLACK, 36), fill=(255, 255, 255, 255), anchor="mm")
            lines = ORIG if sw < 0.5 else SWAP
            for i, ln in enumerate(lines):
                bd.text((44, 170 + i * 92), ln, font=font(F_XB, 52), fill=(*INK, 255), anchor="lm")
            if sw < 0.5:
                # highlight risky bits
                fb = font(F_XB, 52)
                ka = p(t, s2 + 1.6, 0.4)
                for li, pre, word in [(0, "Email for ", "Sarah Lee"), (1, "", "412 Oak St"), (2, "", "#88213")]:
                    x0 = 44 + bd.textlength(pre, font=fb); x1 = x0 + bd.textlength(word, font=fb); y0 = 170 + li * 92
                    bd.rounded_rectangle([x0 - 8, y0 - 36, x1 + 8, y0 + 36], radius=12, outline=(*RED, int(255 * ka)), width=5)
            box = box.resize((int(840 * (1 + 0.04 * math.sin(math.pi * clamp((sw - 0.4) / 0.2)))), 470))
            sub.alpha_composite(with_alpha(box, out_cubic(kb)), (int(W / 2 - box.width / 2), int(560 + 50 * (1 - out_cubic(kb)))))
        kk = p(t, s2 + 4.4, 0.4)
        pill(sub, W / 2, 1170, "Same result. Zero private info.", F_XB, 50, GREEN, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✅")
        draw_text(sub, "Put the real details back in yourself", F_SEMI, 40, W / 2, 1300, SOFT, alpha=out_cubic(p(t, s2 + 5.2, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Your 3-rule", "AI safety check"], t, s3 + 0.1, 320, 84, (WHITE, GOLD), gap=0.07, highlight={"3-rule"})
        checklist(sub, t, s3 + 1.0, SAFE, 640, 170, ACC, size=46, x0=130, every=0.9)
        kk = p(t, s3 + 4.2, 0.4)
        pill(sub, W / 2, 1230, "Clients rehire people they trust", F_XB, 48, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🤝")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
