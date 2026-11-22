"""Why do shops pay to find typos? (owners read what they meant -> check prices/dates/buttons first -> example math)."""
from reel_proof import *
from reel_proof import _rich_line

ACC = (255, 196, 60)
BLUE2 = (120, 200, 255)
GOLD = (255, 214, 92)
bg = Background(top=(8, 16, 44), bottom=(22, 42, 108), blobs=[(40, 80, 200), (255, 196, 60), (30, 50, 140)], seed=1223)


def word_card(sub, t, start, cy, flag_at, stamp_at, w=820, h=240):
    k = p(t, start, 0.35)
    if k <= 0: return
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    f = font(F_BLACK, 84)
    _rich_line(c, d, 60, h / 2, "Free {shiping|shipping}", f, t, [(flag_at, None)], 0)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 50 * (1 - out_cubic(k)))))
    km = p(t, start + 0.2, 1.2)
    if km > 0:
        x = lerp(160, 700, in_out(km))
        place_emoji(sub, "🔍", x, cy + 150, 150, alpha=out_cubic(p(t, start + 0.2, 0.3)))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Why do shops pay", "to find typos?"], t, -0.3, 360, 108, (WHITE, ACC), gap=0.06, highlight={"pay", "typos?"})
        word_card(sub, t, 0.3, 820, 1.3, 1.9)
        stamp(sub, t, 1.9, W / 2 + 230, 700, "TYPO", (235, 64, 52), size=64)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Owners read what", "they meant to write"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"meant"})
        rows = [("They meant:", "Order by Dec 15", BLUE2, s1 + 1.2), ("Page says:", "Order by Dec 51", (255, 110, 100), s1 + 2.0)]
        for i, (lab, val, col, at) in enumerate(rows):
            kk = p(t, at, 0.4)
            if kk <= 0: continue
            cw, ch = 880, 200
            c, d = card_base(cw, ch, radius=36, fill=(255, 255, 255, 255))
            d.text((50, 60), lab, font=font(F_XB, 36), fill=(*GREY, 255), anchor="lm")
            d.text((50, 135), val, font=font(F_BLACK, 64), fill=(*INK, 255), anchor="lm")
            d.rounded_rectangle([cw - 60, 40, cw - 36, ch - 40], radius=12, fill=(*col, 255))
            c = with_alpha(c, out_cubic(kk))
            sub.alpha_composite(c, (int(W / 2 - cw / 2 + 60 * (1 - out_cubic(kk))), 480 + i * 240))
        stamp(sub, t, s1 + 2.8, W / 2 + 250, 870, "MISSED", (235, 64, 52), size=52)
        kb = p(t, s1 + 3.8, 0.4)
        pill(sub, W / 2, 1100, "Their eyes autocorrect. Yours don't.", F_BLACK, 42, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="👀")
        draw_text(sub, "That's the whole service.", F_XB, 50, W / 2, 1220, WHITE, alpha=out_cubic(p(t, s1 + 4.6, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Check these 3 first"], t, s2 + 0.1, 270, 86, (WHITE, ACC), gap=0.07, highlight={"3", "first"})
        items = [("💲", "Prices", "Same price on every page?"), ("📅", "Dates", "Order-by days and years"), ("🔗", "Buttons", "Does every link open?")]
        for i, (em, head, body) in enumerate(items):
            kk = p(t, s2 + 0.8 + i * 0.9, 0.45)
            if kk <= 0: continue
            cw, ch = 880, 200
            c, d = card_base(cw, ch, radius=36, fill=(255, 255, 255, 255))
            e = emoji_img(em, 96)
            c.alpha_composite(e, (90 - e.width // 2, ch // 2 - e.height // 2))
            d.text((170, 70), head, font=font(F_BLACK, 54), fill=(*INK, 255), anchor="lm")
            d.text((170, 140), body, font=font(F_SEMI, 38), fill=(*GREY, 255), anchor="lm")
            kc = p(t, s2 + 1.3 + i * 0.9, 0.35)
            if kc > 0:
                d.ellipse([cw - 120, 60, cw - 40, 140], fill=(*FIXG, 255))
                d.text((cw - 80, 100), "✓", font=font(DEJAVU, 52), fill=(255, 255, 255, 255), anchor="mm")
            c = with_alpha(c, out_cubic(kk))
            sub.alpha_composite(c, (int(W / 2 - cw / 2 + 70 * (1 - out_cubic(kk))), 420 + i * 240))
        kb = p(t, s2 + 4.2, 0.4)
        pill(sub, W / 2, 1220, "A wrong price or date confuses buyers", F_BLACK, 40, ACC, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="😕")
        draw_text(sub, "Better you spot it than a buyer.", F_XB, 46, W / 2, 1340, WHITE, alpha=out_cubic(p(t, s2 + 5.0, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 250, 92, (WHITE, ACC), gap=0.07, highlight={"math"})
        offer_card(sub, t, s3 + 0.5, 630, [("5-page typo check", "$30", s3 + 1.0), ("Fix list (PDF)", "incl.", s3 + 1.4)], "$30", ACC, title="Typo check", h=520)
        bar_chart(sub, t, s3 + 2.4, 930, [("Shop 1", 30), ("Shop 2", 30), ("Shop 3", 30)], BLUE2, title="3 shops this week", every=0.5, h=500)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1495, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
