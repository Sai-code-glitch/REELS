"""Search this on Google Maps tonight -- find local shops with no holiday hours, offer to set them up."""
from reel_maps import *

ACC = (90, 200, 255)    # sky blue
GOLD = (255, 210, 90)
RED = (255, 90, 100)
bg = Background(top=(6, 14, 40), bottom=(10, 30, 60), blobs=[(40, 120, 255), (60, 200, 255), (120, 80, 255)], seed=2981)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🗺️", W / 2, 470 - 16 * math.sin(t * 5), 210 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Search this on", "Google Maps", "tonight"], t, 0.0, 860, 110, (WHITE, ACC), gap=0.07, highlight={"google", "maps", "tonight"})
        kp = p(t, 1.5, 0.4)
        pill(sub, W / 2, 1150, "Find shops that need you", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🔎")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Thanksgiving is Nov 26.", "Shops forget this:"], t, s1 + 0.1, 300, 78, (WHITE, GOLD), gap=0.08, highlight={"nov", "26.", "forget"})
        search_bar(sub, t, s1 + 0.9, 520, "bakery near me")
        listing(sub, t, s1 + 2.6, 760, "🧁", "Rosa's Bakery", "Bakery", "4.7", False, s1 + 3.4, (255, 170, 200))
        kx = p(t, s1 + 4.4, 0.4)
        pill(sub, W / 2, 1010, "No holiday hours listed", F_XB, 50, (255, 230, 232), (200, 30, 50), alpha=out_cubic(kx), scale=out_back(kx), icon="⚠️")
        kq = p(t, s1 + 5.0, 0.4)
        draw_text(sub, "Customers can't tell if it's open", F_SEMI, 42, W / 2, 1140, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Tap 5 local results.", "Note who's missing hours."], t, s2 + 0.1, 300, 70, (WHITE, ACC), gap=0.07, highlight={"5", "missing", "hours."})
        rows = [("🔧", "Dan's Plumbing", "Plumber", "4.8", True, (255, 214, 92)),
                ("💇", "Lily's Salon", "Hair salon", "4.6", False, (200, 160, 255)),
                ("🍕", "Tony's Pizza", "Pizza", "4.5", False, (255, 150, 110))]
        for i, (ic, nm, kind, st, ok, col) in enumerate(rows):
            listing(sub, t, s2 + 1.0 + i * 0.9, 560 + i * 255, ic, nm, kind, st, ok, s2 + 1.6 + i * 0.9, col)
        kp = p(t, s2 + 4.6, 0.4)
        pill(sub, W / 2, 1350, "2 of 3 = 2 people to message", F_XB, 48, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="📝")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Offer to set them up"], t, s3 + 0.1, 290, 76, (WHITE, GOLD), gap=0.07, highlight={"set", "them", "up"})
        kl = p(t, s3 + 0.6, 0.4)
        draw_text(sub, "Example: $25 per shop × 4 shops", F_XB, 46, W / 2, 420, WHITE, alpha=out_cubic(kl))
        money_counter(sub, t, s3 + 1.0, 100, 700, GOLD, label="example pricing")
        kq = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1110, "The owner gives you the real hours", F_XB, 42, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🤝")
        kr = p(t, s3 + 4.5, 0.4)
        draw_text(sub, "Results depend on your work.", F_SEMI, 40, W / 2, 1250, SOFT, alpha=out_cubic(kr))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
