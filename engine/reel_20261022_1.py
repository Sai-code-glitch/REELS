"""Black Friday is 5 weeks away: shops need these 3 emails -- sell a 3-email sale pack."""
from reel_email import *

ACC = (255, 140, 90)    # coral orange
GOLD = (255, 214, 92)
RED = (255, 96, 110)
MINT = (90, 220, 170)
bg = Background(top=(26, 10, 36), bottom=(56, 18, 60), blobs=[(255, 110, 80), (200, 60, 160), (255, 180, 80)], seed=2951)


def calendar_strip(sub, t, start, cy):
    """Week strip of late November; Nov 27 lights up red with an empty note."""
    days = [("MON", "23"), ("TUE", "24"), ("WED", "25"), ("THU", "26"), ("FRI", "27")]
    cw, gap = 150, 18
    x0 = W / 2 - (5 * cw + 4 * gap) / 2
    d = ImageDraw.Draw(sub)
    for i, (dn, num) in enumerate(days):
        kk = p(t, start + i * 0.12, 0.35)
        if kk <= 0: continue
        al = int(255 * out_cubic(kk))
        x = x0 + i * (cw + gap)
        hot = num == "27"
        y = cy - 100 + 40 * (1 - out_cubic(kk))
        d.rounded_rectangle([x, y, x + cw, y + 200], radius=26, fill=((*RED, al) if hot else (245, 246, 250, al)))
        d.text((x + cw / 2, y + 50), dn, font=font(F_XB, 32), fill=((255, 255, 255, al) if hot else (110, 116, 130, al)), anchor="mm")
        d.text((x + cw / 2, y + 125), num, font=font(F_BLACK, 70), fill=((255, 255, 255, al) if hot else (*INK, al)), anchor="mm")


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "✉️", W / 2, 470 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k)
        pop_words(sub, ["Black Friday is", "5 weeks away.", "Shops need 3 emails"], t, 0.0, 820, 92, (WHITE, ACC), gap=0.07, highlight={"5", "weeks", "3", "emails"})
        kp = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1150, "A side gig you can sell this week", F_XB, 48, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(40, 22), icon="💼")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Many small shops", "post once and hope"], t, s1 + 0.1, 330, 88, (WHITE, RED), gap=0.08, highlight={"once", "hope"})
        calendar_strip(sub, t, s1 + 0.8, 680)
        kn = p(t, s1 + 2.0, 0.4)
        pill(sub, W / 2, 900, "Email plan: (empty)", F_XB, 50, (245, 246, 250), (150, 154, 166), alpha=out_cubic(kn), scale=out_back(kn), icon="🗒️")
        kx = p(t, s1 + 3.0, 0.35)
        place_emoji(sub, "😬", W / 2, 1080, 130 * out_back(kx), alpha=out_cubic(kx))
        kp = p(t, s1 + 3.8, 0.4)
        pill(sub, W / 2, 1260, "You write the emails for them", F_XB, 50, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="✍️")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["The 3-email pack"], t, s2 + 0.1, 300, 92, (WHITE, ACC), gap=0.08, highlight={"3-email"})
        email_card(sub, t, s2 + 0.6, W / 2, 560, "1  EARLY ACCESS", "Nov 24", "Your list shops first", "Subscribers get the deal 3 days early. Makes them feel like VIPs.", GOLD)
        email_card(sub, t, s2 + 2.2, W / 2, 900, "2  IT'S LIVE", "Nov 27", "The sale is on", "What's on sale, how much off, one big Shop Now button.", ACC)
        email_card(sub, t, s2 + 3.8, W / 2, 1240, "3  LAST CHANCE", "Nov 30", "Ends tonight", "Cyber Monday reminder with a clear deadline.", MINT)
        kq = p(t, s2 + 5.6, 0.4)
        draw_text(sub, "Short, clear, one link each", F_SEMI, 46, W / 2, 1470, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example pricing"], t, s3 + 0.1, 300, 84, (WHITE, GOLD), gap=0.08, highlight={"pricing"})
        k1 = p(t, s3 + 0.6, 0.4)
        pill(sub, W / 2, 470, "3 emails = $150 per shop", F_XB, 56, (245, 246, 250), INK, alpha=out_cubic(k1), scale=out_back(k1), icon="✉️")
        k2 = p(t, s3 + 1.2, 0.4)
        pill(sub, W / 2, 610, "x 4 shops", F_XB, 56, ACC, INK, alpha=out_cubic(k2), scale=out_back(k2), icon="🛍️")
        money_counter(sub, t, s3 + 1.9, 600, 900, GOLD, label="example total")
        kq = p(t, s3 + 4.6, 0.5)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1290, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
