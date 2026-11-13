"""Your first Marketplace listing: 10 minutes, $0 (4-fix listing formula + fast reply)."""
from reel_market import *

ACC = (120, 175, 255)   # marketplace blue
GOLD = (255, 214, 92)
bg = Background(top=(8, 14, 44), bottom=(18, 36, 96), blobs=[(40, 90, 230), (120, 175, 255), (150, 70, 200)], seed=3172)
BAD = ("chair", "$120", "Listed 2 days ago · Springfield", ["pm me", "no lowballers"])
GOOD = ("IKEA Poäng armchair, beige, like new", "$45", "Pickup near Oak St · weekdays 5-8pm",
        ["Light wear on 1 arm (photo 3).", "Smoke-free home. Cushion included."])


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first listing", "on Marketplace:", "10 minutes, $0"], t, -0.3, 390, 96, (WHITE, ACC), gap=0.06, highlight={"10", "minutes,", "$0"})
        mp_listing(sub, t, 0.5, 690, "🪑", BAD, GOOD, show_good_only=True, w=700)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Stop posting this"], t, s1 + 0.1, 270, 92, (WHITE, ACC), gap=0.07, highlight={"stop"})
        mp_listing(sub, t, s1 + 0.5, 400, "🪑", BAD, GOOD, flags=[("Dark, 1 photo", 110), ("Guessed price", 470), ("No details", 720)], flag_at=s1 + 1.4, w=760)
        kq = p(t, s1 + 3.6, 0.4)
        pill(sub, W / 2, 1340, "Buyers scroll right past", F_XB, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="👀")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["4 fixes, 10 minutes"], t, s2 + 0.1, 255, 84, (WHITE, ACC), gap=0.07, highlight={"4", "fixes,"})
        checklist(sub, t, s2 + 0.6, ["3 photos in daylight", "Brand + item + condition", "Price from eBay sold", "Pickup area + times"], 375, 82, ACC, size=46, x0=170, every=0.7, icon="✅")
        mp_listing(sub, t, s2 + 0.3, 700, "🪑", BAD, GOOD, swap_at=s2 + 3.6, w=700)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Then reply fast"], t, s3 + 0.1, 260, 90, (WHITE, ACC), gap=0.07, highlight={"fast"})
        phone_chat(sub, t, s3 + 0.5, W / 2, 360, [
            ("them", "Hi, is this still available?", s3 + 0.9, None),
            ("me", "Yes! Pickup near Oak St, weekdays 5-8pm. Today work?", s3 + 1.9, "Sent"),
            ("them", "Perfect, 6pm?", s3 + 3.1, None),
        ], header="Jordan", h=760, sub_label="Marketplace · about your armchair")
        kq = p(t, s3 + 4.2, 0.4)
        pill(sub, W / 2, 1230, "Meet in a busy public place", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🛡️")
        draw_text(sub, "Example listing. Results depend on your item.", F_SEMI, 36, W / 2, 1350, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
