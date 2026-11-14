"""List a digital product on Etsy for 20 cents (digital listing form, title + tags, fee math)."""
from reel_calendar import *

ACC = (120, 190, 255)   # sky blue
GOLD = (255, 214, 92)
bg = Background(top=(6, 16, 40), bottom=(14, 40, 90), blobs=[(30, 70, 170), (120, 190, 255), (90, 50, 170)], seed=3183)
TEACH = dict(emoji="🍎", title_extra="Teacher Calendar")
PAGE_ACC = (210, 70, 70)
TITLE = "2027 Teacher Calendar Printable PDF, Monthly Planner, US Letter"


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["List a digital", "product on Etsy", "for 20 cents"], t, -0.3, 400, 104, (WHITE, ACC), gap=0.06, highlight={"digital", "20", "cents"})
        kp = p(t, 0.5, 0.4)
        pill(sub, W / 2, 700, "$0.20 listing fee", F_BLACK, 66, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(50, 24), icon="🏷️")
        page_card(sub, t, 1.0, W / 2, 1160, PAGE_ACC, w=400, rot=4, **TEACH)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Set it as digital"], t, s1 + 0.1, 280, 88, (WHITE, ACC), gap=0.07, highlight={"digital"})
        listing_form(sub, t, s1 + 0.5, 400, ACC, [
            ("Type", "Digital files", "💾"),
            ("File", "calendar.pdf", "📄"),
            ("Photos", "5 mockups", "🖼️"),
            ("Price (example)", "$4.00", "💵"),
        ], every=0.8)
        kq = p(t, s1 + 4.3, 0.4)
        pill(sub, W / 2, 1100, "Buyers download it. No shipping.", F_XB, 46, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="⚡")
        draw_text(sub, "Make it once. It can sell again and again.", F_SEMI, 38, W / 2, 1220, SOFT, alpha=out_cubic(p(t, s1 + 5.0, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Title = what people", "actually search"], t, s2 + 0.1, 290, 80, (WHITE, ACC), gap=0.07, highlight={"search"})
        title_box(sub, t, s2 + 0.5, 420, TITLE, 1.8, ACC, size=44)
        draw_text(sub, "+ use all 13 tags", F_XB, 46, W / 2, 870, WHITE, alpha=out_cubic(p(t, s2 + 2.8, 0.4)))
        tag_chips(sub, t, s2 + 3.1, 940, ["2027 calendar", "teacher gift", "printable", "monthly planner",
                                           "classroom", "school year", "pdf calendar"], ACC, every=0.3, size=38)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Fee math on $4", "(example)"], t, s3 + 0.1, 280, 84, (WHITE, ACC), gap=0.07, highlight={"$4"})
        formula_rows(sub, t, s3 + 0.6, 440, [
            ("🏷️", "Listing fee", "−$0.20"),
            ("🧾", "Transaction 6.5%", "−$0.26"),
            ("💳", "Processing 3% + $0.25", "−$0.37"),
        ], ACC, every=0.6, row=130)  # rows
        dollar_counter(sub, t, s3 + 2.6, 3.17, 960, ACC, "you keep per sale", size=190)
        draw_text(sub, "Etsy US rates, mid-2026. Check yours.", F_SEMI, 34, W / 2, 1210, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.4)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1265, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
