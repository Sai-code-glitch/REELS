"""Check 1 online shop's homepage tonight: find shops with no Christmas 'order by' date + 3-line DM."""
from reel_shipby import *

ACC = (230, 130, 255)   # orchid
GOLD = (255, 214, 92)
bg = Background(top=(30, 8, 46), bottom=(70, 20, 96), blobs=[(170, 60, 230), (255, 110, 180), (90, 60, 220)], seed=3143)
SITE = dict(url="lunasoaps.co", shop="Luna Soaps", emoji="🧼", color=(210, 230, 255),
            tiles=(("🧼", (232, 240, 255)), ("🌿", (220, 245, 225)), ("🎁", (255, 222, 230))))
DM = [("me", "Hi Ana! Love your soaps!", 0, None),
      ("me", "I couldn't find a last day to order for Christmas on your site.", 0.9, None),
      ("me", "Want a free banner + story for it?", 1.8, None),
      ("them", "Yes please! Ours is Dec 15", 3.4, None)]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "🔎", W / 2, 330 - 14 * math.sin(t * 6), 150 * out_back(k), alpha=k)
        pop_words(sub, ["Check 1 online", "shop's homepage", "tonight"], t, -0.3, 600, 100, (WHITE, ACC), gap=0.05, highlight={"homepage", "tonight"})
        shop_site(sub, t, 1.0, 850, find=("order by", 0.9, False), h=620, **SITE)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Look for 1 line:", "“Order by __", "for Christmas”"], t, s1 + 0.1, 330, 82, (WHITE, ACC), gap=0.07, highlight={"“order", "by", "christmas”"})
        rows = [("🕯️", (250, 214, 165), "oakandwick.shop", True),
                ("🧼", (210, 230, 255), "lunasoaps.co", False),
                ("🧶", (255, 210, 220), "knitbybea.com", False)]
        for i, (e, col, site, has) in enumerate(rows):
            lead_row(sub, t, s1 + 1.2 + i * 0.4, 640 + i * 200, e, col, site, has, s1 + 2.6 + i * 0.6)
        kq = p(t, s1 + 4.9, 0.4)
        pill(sub, W / 2, 1300, "0 results = your lead", F_XB, 52, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📝")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Then send", "3 short lines"], t, s2 + 0.1, 260, 86, (WHITE, ACC), gap=0.07, highlight={"3", "lines"})
        msgs = [(s, txt, s2 + 0.8 + at, ex) for s, txt, at, ex in DM]
        phone_chat(sub, t, s2 + 0.5, W / 2, 400, msgs, header="Luna Soaps", w=820, h=840)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["If they say yes", "(example)"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"yes"})
        offer_card(sub, t, s3 + 0.6, 760, [
            ("Website cutoff banner", "$20", s3 + 1.1),
            ("Story + post graphic", "$20", s3 + 1.7),
        ], "$40", ACC, title="Holiday 'order by' set", h=560)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1110, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.4)))
        kq = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1260, "Message 3 shops, not 300", F_XB, 48, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎯")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
