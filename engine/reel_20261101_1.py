"""Thanksgiving is 25 days away. Bakeries need this form (pre-order form gig)."""
from reel_preorder import *

ACC = (255, 160, 60)    # pumpkin
GOLD = (255, 214, 92)
bg = Background(top=(40, 14, 6), bottom=(86, 34, 12), blobs=[(200, 90, 30), (240, 170, 60), (150, 40, 40)], seed=3051)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Thanksgiving is", "25 days away"], t, -0.3, 440, 112, (WHITE, ACC), gap=0.06, highlight={"25", "days"})
        kp = p(t, 0.7, 0.35)
        pill(sub, W / 2, 650, "Bakeries need this 1 form", F_XB, 54, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="👇")
        gform(sub, t, 1.0, 740, "Thanksgiving Pie Pre-Orders", scale=0.66)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Pie orders pile up", "in their DMs"], t, s1 + 0.1, 300, 80, (WHITE, ACC), gap=0.07, highlight={"DMs"})
        dm_pile(sub, t, s1 + 0.8, 500, [
            ("Maria", "Can I get 2 pumpkin pies?"),
            ("Tom", "Still taking orders??"),
            ("Ana", "Pickup Wed or Tue?"),
            ("Chris", "Wait, how much is pecan?"),
            ("Maria", "Actually make it 3 pies"),
        ], every=0.55)
        kx = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1290, "Orders get lost. Owners stress.", F_XB, 48, WHITE, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="😩")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Build them a free", "Google Form"], t, s2 + 0.1, 280, 84, (WHITE, ACC), gap=0.07, highlight={"Google", "Form"})
        st = [s2 + 0.9 + i * 0.6 for i in range(5)]
        sel = sum(1 for x in st if t >= x) - 1
        gform(sub, t, s2 + 0.5, 420, "Thanksgiving Pie Pre-Orders", steps=st, fill_at=s2 + 4.6, scale=0.9, sel=sel if t < s2 + 4.4 else None)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Every order lands", "in 1 sheet"], t, s3 + 0.1, 280, 84, (WHITE, ACC), gap=0.07, highlight={"1", "sheet"})
        order_sheet(sub, t, s3 + 0.5, 380, every=0.5, rows=ORDERS[:3])
        offer_card(sub, t, s3 + 3.3, 1210, [
            ("Pre-order form", "$40", s3 + 3.7),
            ("Order sheet + link in bio", "$20", s3 + 4.1),
        ], "$60", ACC, title="Holiday pre-order setup", h=540)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1525, SOFT, alpha=out_cubic(p(t, s3 + 5.0, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
