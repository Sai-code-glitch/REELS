"""Your first saved-reply pack: 15 minutes, $0 (4-part reply formula, Google Docs build, paste into Etsy Saved replies)."""
from reel_replies import *

ACC = (90, 230, 190)    # mint
GOLD = (255, 214, 92)
bg = Background(top=(8, 30, 44), bottom=(14, 64, 80), blobs=[(30, 150, 150), (90, 230, 190), (20, 90, 130)], seed=2112)

BLOCKS_HOOK = [("Will it arrive by Dec 24?", "Hi [NAME]! Order by [DATE] for Dec 24 delivery.", 0.9, 1.6)]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "saved-reply pack:", "15 minutes, $0"], t, -0.3, 390, 100, (WHITE, ACC), gap=0.06, highlight={"15", "minutes,", "$0"})
        reply_doc(sub, t, 0.6, 720, BLOCKS_HOOK, h=440)
        k = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1290, "For Etsy shops in December", F_XB, 46, GOLD, INK, alpha=out_cubic(k), scale=out_back(k), icon="🎄")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Every reply =", "4 parts"], t, s1 + 0.1, 270, 92, (WHITE, ACC), gap=0.07, highlight={"4", "parts"})
        items = ["1. Thank them by [NAME]", "2. Answer in 1 line", "3. Add the date or rule", "4. Tell them what's next"]
        checklist(sub, t, s1 + 0.8, items, 560, 135, ACC, size=52, x0=130, every=0.8)
        kb = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1180, "[BRACKETS] = fill in later", F_BLACK, 48, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="✍️")
        draw_text(sub, "One reply works for every buyer", F_XB, 44, W / 2, 1300, WHITE, alpha=out_cubic(p(t, s1 + 5.3, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Write 5 in Google Docs"], t, s2 + 0.1, 250, 76, (WHITE, ACC), gap=0.07, highlight={"5", "Docs"})
        blocks = [
            ("Arrive by Dec 24?", "Hi [NAME]! Order by [DATE] for Dec 24 delivery. I'll send tracking when it ships.", s2 + 0.8, 1.6),
            ("Gift wrap?", "Yes! Add a note at checkout and I'll wrap it for [PRICE].", s2 + 2.8, 1.3),
            ("Where is my order?", "Thanks [NAME]! It shipped [DATE]. Here's your tracking: [LINK]", s2 + 4.5, 1.4),
        ]
        reply_doc(sub, t, s2 + 0.4, 360, blocks, h=1000)
        draw_text(sub, "+ 2 more: custom names, returns", F_XB, 42, W / 2, 1450, WHITE, alpha=out_cubic(p(t, s2 + 6.4, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Paste into Etsy's", "Saved replies"], t, s3 + 0.1, 250, 84, (WHITE, ACC), gap=0.07, highlight={"Saved", "replies"})
        saved_picker(sub, t, s3 + 0.5, 430, "Can you gift wrap it?",
                     [("Arrive by Dec 24?", "📦"), ("Gift wrap?", "🎁"), ("Where is my order?", "🚚")],
                     pick=1, open_at=s3 + 1.6, pick_at=s3 + 3.0,
                     reply="Yes! Add a note at checkout and I'll wrap it for $3.",
                     h=760)
        kq = p(t, s3 + 4.6, 0.4)
        pill(sub, W / 2, 1310, "This doc = your free sample", F_BLACK, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📄")
        draw_text(sub, "Example shop. Results depend on your work.", F_SEMI, 34, W / 2, 1420, SOFT, alpha=out_cubic(p(t, s3 + 5.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
