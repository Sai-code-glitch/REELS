"""Your first payment link: 5 minutes, $0 -- create a deposit link, send it with the quote."""
from reel_quote import *

ACC = (170, 140, 255)   # violet
GOLD = (255, 214, 92)
bg = Background(top=(18, 10, 44), bottom=(30, 16, 70), blobs=[(130, 80, 255), (200, 120, 255), (80, 120, 255)], seed=2993)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🔗", W / 2, 470 - 16 * math.sin(t * 5), 210 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Your first", "payment link:", "5 minutes, $0"], t, 0.0, 860, 108, (WHITE, ACC), gap=0.07, highlight={"payment", "link:", "$0"})
        kp = p(t, 1.5, 0.4)
        pill(sub, W / 2, 1160, "Get paid before you start", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="💳")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["\"How do I pay you?\""], t, s1 + 0.1, 300, 78, (WHITE, GOLD), gap=0.08, highlight={"pay", "you?\""})
        chat_bubble(sub, t, s1 + 0.9, 500, ["Ok let's do it! How do I pay?"], me=False)
        chat_bubble(sub, t, s1 + 1.8, 660, ["Uh... send it to my", "bank? I'll text the details"], me=True, color=(120, 126, 140))
        kx = p(t, s1 + 3.0, 0.4)
        pill(sub, W / 2, 870, "Messy = clients change their mind", F_XB, 44, (255, 230, 232), (200, 30, 50), alpha=out_cubic(kx), scale=out_back(kx), icon="⚠️")
        kq = p(t, s1 + 4.0, 0.4)
        draw_text(sub, "Send 1 link instead", F_BLACK, 64, W / 2, 1030, ACC, alpha=out_cubic(kq))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["PayPal, Stripe or Square:", "make a payment link"], t, s2 + 0.1, 270, 66, (WHITE, ACC), gap=0.07, highlight={"payment", "link"})
        link_screen(sub, t, s2 + 0.6, 420, ACC, [s2 + 1.2, s2 + 2.4, s2 + 3.4, s2 + 3.8])
        kp = p(t, s2 + 4.8, 0.4)
        pill(sub, W / 2, 1300, "Free to set up. Small fee per payment.", F_XB, 40, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="ℹ️")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Paste it under your quote"], t, s3 + 0.1, 270, 70, (WHITE, GOLD), gap=0.07, highlight={"quote"})
        chat_bubble(sub, t, s3 + 0.6, 470, ["Quote attached! Deposit here:", "pay.link/your-name/deposit"], me=True, color=(110, 80, 230), w=820)
        notification(sub, t, s3 + 1.8, 720, "Payments", "Deposit received: $75", "Logo design - 50% deposit", (90, 200, 140), icon="✅")
        kl = p(t, s3 + 3.0, 0.4)
        draw_text(sub, "Now you start the work", F_BLACK, 62, W / 2, 940, WHITE, alpha=out_cubic(kl))
        kr = p(t, s3 + 3.8, 0.4)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1060, SOFT, alpha=out_cubic(kr))
        kq = p(t, s3 + 4.4, 0.4)
        pill(sub, W / 2, 1200, "1 link, 1 tap, done", F_XB, 48, ACC, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="⚡")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
