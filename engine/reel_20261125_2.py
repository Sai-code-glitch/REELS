"""Your first Reddit reply: 5 minutes, $0 (4-part reply to a [Hiring] post: their task / 1 sample / price + time / 1 question)."""
from reel_reddit import *

ACC = (180, 140, 255)
GOLD = (255, 220, 120)
bg = Background(top=(18, 12, 44), bottom=(60, 30, 110), blobs=[(110, 60, 200), (180, 140, 255), (40, 20, 90)], seed=1252)

POST = (["Need 3 Instagram captions", "for my candle shop"], ["Budget $30. Need them by Friday.", "Reply with a sample please!"])


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first Reddit reply:", "5 minutes, $0"], t, -0.3, 360, 96, (WHITE, ACC), gap=0.07, highlight={"reddit", "5", "$0"})
        post_card(sub, t, 0.5, 600, POST[0], POST[1])
        draw_text(sub, "(sample post)", F_SEMI, 32, W / 2, 1290, SOFT, alpha=out_cubic(p(t, 1.4, 0.4)))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Don't reply", "like this"], t, s1 + 0.1, 290, 96, (WHITE, ACC), gap=0.07, highlight={"don't"})
        chat_bubble(sub, t, s1 + 0.9, 560, ["I can do this. DM me."], me=False)
        kx = p(t, s1 + 1.8, 0.35)
        place_emoji(sub, "❌", W - 190, 560, 120 * out_back(kx), alpha=out_cubic(kx))
        checklist(sub, t, s1 + 2.6, ["No sample", "No price", "No reason to pick you"], 800, 100, ACC, size=50, every=0.55, icon="🚫")
        kb = p(t, s1 + 4.8, 0.4)
        pill(sub, W / 2, 1240, "Show, don't just say", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="👀")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Use these 4 parts"], t, s2 + 0.1, 250, 88, (WHITE, ACC), gap=0.07, highlight={"4", "parts"})
        parts = [("1 · THEIR TASK", ["3 cozy captions for your candles"], s2 + 0.9),
                 ("2 · ONE SAMPLE", ["Here's 1 now: \"Light it. Breathe.\""], s2 + 2.2),
                 ("3 · PRICE + TIME", ["$30 for 3, sent by Thursday"], s2 + 3.5),
                 ("4 · ONE QUESTION", ["Which scent should I start with?"], s2 + 4.8)]
        reply_box(sub, t, s2 + 0.5, 400, parts, ACC, send_at=s2 + 6.4)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Before you hit send"], t, s3 + 0.1, 270, 86, (WHITE, ACC), gap=0.07, highlight={"send"})
        checklist(sub, t, s3 + 0.8, ["Read the sub's rules", "Contact them the way they ask", "Sample is about THEIR shop", "You never pay to apply"], 470, 110, ACC, size=46, every=0.6)
        offer_card(sub, t, s3 + 3.4, 1110, [("3 Instagram captions", "$30", s3 + 3.9)], "$30", ACC, title="Caption pack", h=430)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1400, SOFT, alpha=out_cubic(p(t, s3 + 5.0, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
