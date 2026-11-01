"""Your first pre-order form: 10 minutes, $0 (Google Forms build walkthrough)."""
from reel_preorder import *
from reel_portfolio import timer

ACC = (120, 220, 255)   # sky
GOLD = (255, 214, 92)
bg = Background(top=(10, 14, 50), bottom=(36, 30, 110), blobs=[(103, 58, 183), (40, 120, 220), (220, 120, 60)], seed=3052)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "pre-order form:", "10 minutes, $0"], t, -0.3, 470, 104, (WHITE, ACC), gap=0.06, highlight={"10", "minutes,", "$0"})
        kp = p(t, 0.8, 0.35)
        pill(sub, W / 2, 770, "Make it for 1 local bakery", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🥧")
        gform(sub, t, 1.1, 860, "Thanksgiving Pie Pre-Orders", scale=0.6, fill_at=1.6)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Step 1: open", "Google Forms"], t, s1 + 0.1, 300, 88, (WHITE, ACC), gap=0.07, highlight={"Google", "Forms"})
        checklist(sub, t, s1 + 0.9, ["Go to forms.google.com", "Tap  +  Blank form", "Title: Thanksgiving Pie Pre-Orders", "Note: order by + pay at pickup"], 520, 110, ACC, size=44, x0=120, every=0.8)
        kb = p(t, s1 + 1.7, 0.45)
        if kb > 0:
            c, d = gbase(300, 340, fill=(255, 255, 255), radius=36)
            d.rectangle([0, 0, 299, 30], fill=(*FORM_PURPLE, 255))
            d.text((150, 160), "+", font=font(F_BLACK, 190), fill=(*FORM_PURPLE, 255), anchor="mm")
            d.text((150, 292), "Blank form", font=font(F_XB, 36), fill=(*INK, 255), anchor="mm")
            mask = Image.new("L", (300, 340), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, 299, 339], radius=36, fill=255)
            c.putalpha(mask)
            sc = 0.6 + 0.4 * out_back(kb)
            c = c.resize((int(300 * sc), int(340 * sc)))
            with_alpha(c, out_cubic(kb))
            sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(1330 - c.height / 2)))
            place_emoji(sub, "👆", W / 2 + 150, 1430 + 18 * math.sin(t * 7), 100, alpha=out_cubic(p(t, s1 + 2.3, 0.3)))
        kx = p(t, s1 + 4.4, 0.4)
        pill(sub, W / 2, 1050, "Free with any Google account", F_XB, 48, WHITE, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="✅")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Step 2: add", "5 questions"], t, s2 + 0.1, 280, 88, (WHITE, ACC), gap=0.07, highlight={"5", "questions"})
        st = [s2 + 0.9 + i * 0.85 for i in range(5)]
        idx = sum(1 for x in st if t >= x) - 1
        gform(sub, t, s2 + 0.5, 410, "Thanksgiving Pie Pre-Orders", steps=st, scale=0.82, sel=idx if idx >= 0 else None)
        labels = ["Short answer", "Short answer", "Dropdown: pie flavors", "Dropdown: 1, 2, 3", "Multiple choice: pickup days"]
        if idx >= 0:
            kk = p(t, st[idx], 0.3)
            pill(sub, W / 2, 1480, labels[idx], F_XB, 44, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Step 3: link it", "to a Sheet"], t, s3 + 0.1, 280, 88, (WHITE, ACC), gap=0.07, highlight={"Sheet"})
        pill(sub, W / 2, 470, "Responses tab → Link to Sheets", F_XB, 44, WHITE, INK, alpha=out_cubic(p(t, s3 + 0.6, 0.35)), scale=out_back(p(t, s3 + 0.6, 0.35)), icon="📊")
        order_sheet(sub, t, s3 + 1.2, 580, every=0.5, rows=ORDERS[:3], title="Orders (sample)")
        timer(sub, t, s3 + 3.4, 1.8, W / 2, 1290, 10, GOLD)
        draw_text(sub, "Send 1 test order before you share it", F_SEMI, 38, W / 2, 1420, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
