"""Your first proofread: 15 minutes, $0 (2 free tools -> paste into Docs + Ctrl+F old year -> fix list sample)."""
from reel_proof import *

ACC = (175, 145, 255)
GOLD = (255, 214, 92)
bg = Background(top=(24, 14, 56), bottom=(66, 36, 132), blobs=[(110, 70, 220), (175, 145, 255), (60, 30, 120)], seed=1222)

DOC = ["{Free shiping|x} on orders $50+.",
       "Every candle is hand-poured in",
       "small {batchs|x}. Order by Dec 15",
       "for {Chrismas|x} delivery."]


def clock(sub, t, start, dur, cy, minutes, color):
    if t < start: return
    m = minutes * out_cubic(p(t, start, dur))
    a = out_cubic(p(t, start, 0.3))
    place_emoji(sub, "⏱️", W / 2 - 190, cy, 96, alpha=a)
    draw_text(sub, f"{int(m):02d}:00", F_BLACK, 100, W / 2 + 50, cy, color, alpha=a)


def tool_tile(sub, t, start, cx, cy, emoji, name, sub_lab, acc):
    k = p(t, start, 0.45)
    if k <= 0: return
    cw, ch = 400, 420
    c, d = card_base(cw, ch, radius=40, fill=(255, 255, 255, 255))
    e = emoji_img(emoji, 130)
    c.alpha_composite(e, (cw // 2 - e.width // 2, 130 - e.height // 2))
    d.text((cw / 2, 270), name, font=font(F_BLACK, 50), fill=(*INK, 255), anchor="mm")
    d.text((cw / 2, 340), sub_lab, font=font(F_SEMI, 34), fill=(*GREY, 255), anchor="mm")
    d.rounded_rectangle([cw / 2 - 60, 380, cw / 2 + 60, 404], radius=12, fill=(*acc, 255))
    c = with_alpha(c, out_cubic(k))
    s = 0.8 + 0.2 * out_back(k)
    c = c.resize((int(cw * s), int(ch * s)))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first proofread:", "15 minutes, $0"], t, -0.3, 330, 100, (WHITE, ACC), gap=0.06, highlight={"15", "minutes,", "$0"})
        clock(sub, t, 0.3, 2.6, 570, 15, GOLD)
        doc_check(sub, t, 0.5, 700, DOC, [1.2, 1.6, 2.0], h=540)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["You need 2 free tools"], t, s1 + 0.1, 300, 84, (WHITE, ACC), gap=0.07, highlight={"2", "free"})
        tool_tile(sub, t, s1 + 0.8, W / 2 - 215, 680, "📄", "Google Docs", "spell check", ACC)
        tool_tile(sub, t, s1 + 1.4, W / 2 + 215, 680, "🔍", "Ctrl + F", "find old dates", ACC)
        kb = p(t, s1 + 3.0, 0.4)
        pill(sub, W / 2, 1060, "No paid apps needed", F_BLACK, 48, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="✅")
        draw_text(sub, "Pick 1 small shop's website.", F_XB, 50, W / 2, 1190, WHITE, alpha=out_cubic(p(t, s1 + 3.8, 0.4)))
        draw_text(sub, "Check 4 pages: Home, Shop,", F_SEMI, 44, W / 2, 1280, SOFT, alpha=out_cubic(p(t, s1 + 4.4, 0.4)))
        draw_text(sub, "Shipping, About.", F_SEMI, 44, W / 2, 1345, SOFT, alpha=out_cubic(p(t, s1 + 4.4, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    mid = s2 + 4.0
    if s2 <= t < mid:
        sub = new_layer()
        pop_words(sub, ["Step 1: paste the text", "into Google Docs"], t, s2 + 0.1, 250, 76, (WHITE, ACC), gap=0.06, highlight={"paste", "docs"})
        doc_check(sub, t, s2 + 0.5, 440, DOC, [s2 + 1.4, s2 + 1.9, s2 + 2.4], h=540)
        draw_text(sub, "Red squiggle = check that word", F_XB, 48, W / 2, 1100, WHITE, alpha=out_cubic(p(t, s2 + 2.9, 0.4)))
        faded(layer, sub, t, s2, mid)
    if mid <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Step 2: Ctrl+F", "last year"], t, mid + 0.1, 250, 84, (WHITE, ACC), gap=0.07, highlight={"ctrl+f", "last", "year"})
        find_bar(sub, t, mid + 0.4, 440, "2025", [("Our 2025 holiday sale is live!", mid + 1.3), ("New for 2025: gift sets", mid + 1.7), ("© 2025 Pine & Wick", mid + 2.1)], ACC)
        kb = p(t, mid + 2.7, 0.4)
        pill(sub, W / 2, 1060, "Old dates look closed", F_BLACK, 48, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="📅")
        draw_text(sub, "Step 3: click every button", F_XB, 50, W / 2, 1190, WHITE, alpha=out_cubic(p(t, mid + 3.2, 0.4)))
        faded(layer, sub, t, mid, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Turn it into", "a fix list"], t, s3 + 0.1, 260, 92, (WHITE, ACC), gap=0.07, highlight={"fix", "list"})
        fix_table(sub, t, s3 + 0.6, 430, [("Home", "shiping", "shipping", s3 + 1.2), ("Home", "2025 sale", "2026 sale", s3 + 1.7),
                                          ("Shipping", "Chrismas", "Christmas", s3 + 2.2), ("Footer", "© 2025", "© 2026", s3 + 2.7)], ACC)
        kb = p(t, s3 + 3.6, 0.4)
        pill(sub, W / 2, 1400, "That's your free sample", F_BLACK, 48, WHITE, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎁")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
