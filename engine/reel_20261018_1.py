"""AI drafts. You edit. Clients pay. (Free AI for freelancers, part 1)."""
from reel_common import *

ACC = (170, 130, 255)   # violet
GOLD = (255, 210, 90)
GREEN = (70, 220, 150)
bg = Background(top=(18, 10, 44), bottom=(40, 14, 66), blobs=[(140, 90, 255), (230, 90, 200), (90, 160, 255)], seed=2911)

PROMPT = ["Write 3 captions for a", "bakery's pumpkin bread.", "Friendly, under 20 words."]
REPLIES = ["1. Warm, spiced, and fresh at 7am 🍞", "2. Fall in a loaf. Grab one today.", "3. Pumpkin season is here. So are we."]
STEPS = [("1", "Paste the client brief", "📋"), ("2", "Ask for 3 rough drafts", "🤖"), ("3", "Rewrite in your voice", "✍️"), ("4", "Fact-check every line", "🔍")]


def chat_ui(t, start, w=820, h=900):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(248, 247, 252, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=40, fill=(236, 232, 248, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(236, 232, 248, 255))
    d.text((40, 52), "Free AI chat", font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
    d.ellipse([w - 70, 38, w - 42, 66], fill=(*GREEN, 255))
    # user bubble
    k = p(t, start, 0.4)
    if k > 0:
        a = int(255 * out_cubic(k))
        d.rounded_rectangle([170, 130, w - 30, 130 + 64 * 3 + 30], radius=30, fill=(*ACC, a))
        for i, ln in enumerate(PROMPT):
            d.text((200, 175 + i * 64), ln, font=font(F_SEMI, 36), fill=(255, 255, 255, a), anchor="lm")
    # typing dots then replies
    t0 = start + 1.0
    if t0 < t < t0 + 0.9:
        for i in range(3):
            yy = 430 + 8 * math.sin(t * 12 + i)
            d.ellipse([50 + i * 34, yy, 72 + i * 34, yy + 22], fill=(150, 150, 170, 255))
    for i, ln in enumerate(REPLIES):
        kk = p(t, t0 + 0.9 + i * 0.45, 0.35)
        if kk <= 0: continue
        a = int(255 * out_cubic(kk)); y = 410 + i * 140
        d.rounded_rectangle([30, y, w - 120, y + 112], radius=28, fill=(230, 230, 238, a))
        d.text((60, y + 56), ln.replace(" 🍞", ""), font=font(F_SEMI, 33), fill=(*INK, a), anchor="lm")
    kd = p(t, t0 + 3.0, 0.4)
    if kd > 0:
        d.text((w / 2, h - 60), "Rough drafts, not final copy", font=font(F_XB, 34), fill=(150, 90, 230, int(255 * out_cubic(kd))), anchor="mm")
    return im


def bars(sub, t, start):
    rows = [("Writing from scratch", 120, (255, 120, 140)), ("AI draft + your edit", 50, GREEN)]
    for i, (lab, mins, col) in enumerate(rows):
        k = p(t, start + i * 0.9, 1.2)
        y = 600 + i * 260
        a = out_cubic(p(t, start + i * 0.9, 0.3))
        draw_text(sub, lab, F_XB, 50, 140, y, WHITE, alpha=a, anchor="lm")
        d = ImageDraw.Draw(sub)
        full = 780 * mins / 120
        d.rounded_rectangle([140, y + 50, 140 + 780, y + 140], radius=45, fill=(255, 255, 255, int(40 * a)))
        if k > 0:
            d.rounded_rectangle([140, y + 50, 140 + max(90, full * out_cubic(k)), y + 140], radius=45, fill=(*col, 255))
            draw_text(sub, f"{int(mins * out_cubic(k))} min", F_BLACK, 50, 140 + max(90, full * out_cubic(k)) - 30, y + 95, INK, anchor="rm")


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = clamp(p(t, 0.0, 0.3) + 0.4)
        place_emoji(sub, "🤖", W / 2, 500 + 10 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=6 * math.sin(t * 5))
        pop_words(sub, ["AI drafts.", "You edit.", "Clients pay."], t, -0.25, 920, 118, (WHITE, ACC), gap=0.07, highlight={"you", "pay."})
        kk = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1320, "The honest way to use free AI", F_SEMI, 44, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✨")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["The slowest part", "is the blank page"], t, s1 + 0.1, 330, 84, (WHITE, GOLD), gap=0.07, highlight={"blank", "page"})
        kd = p(t, s1 + 1.0, 0.45)
        if kd > 0:
            doc = Image.new("RGBA", (700, 560), (0, 0, 0, 0)); dd = ImageDraw.Draw(doc)
            dd.rounded_rectangle([0, 0, 699, 559], radius=34, fill=(255, 255, 255, 255))
            dd.text((50, 70), "Captions_draft.doc", font=font(F_XB, 38), fill=(120, 124, 140, 255), anchor="lm")
            if int(t * 2.2) % 2 == 0:
                dd.rectangle([52, 150, 58, 220], fill=(*INK, 255))
            sub.alpha_composite(with_alpha(doc, out_cubic(kd)), (190, int(560 + 50 * (1 - out_cubic(kd)))))
        kc = p(t, s1 + 2.2, 0.4)
        place_emoji(sub, "⏳", W / 2 + 300, 1080, 130 * out_back(kc), alpha=out_cubic(kc), rot=20 * math.sin(t * 3))
        kk = p(t, s1 + 3.4, 0.4)
        pill(sub, W / 2, 1300, "Let AI fill it. Then you fix it.", F_XB, 48, ACC, WHITE, alpha=out_cubic(kk), scale=out_back(kk), icon="💡")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        if t < s2 + 4.4:
            pop_words(sub, ["Ask for rough drafts"], t, s2 + 0.1, 270, 74, (WHITE, ACC), gap=0.07, highlight={"rough"})
            kc = p(t, s2 + 0.3, 0.45)
            if kc > 0:
                ui = chat_ui(t, s2 + 0.6).resize((738, 810))
                a = out_cubic(kc) * (1 - out_cubic(p(t, s2 + 4.0, 0.4)))
                sub.alpha_composite(with_alpha(ui, a), (171, int(400 + 60 * (1 - out_cubic(kc)))))
        else:
            pop_words(sub, ["The 4-step workflow"], t, s2 + 4.4, 300, 74, (WHITE, ACC), gap=0.07, highlight={"4-step"})
            for i, (n, lab, em) in enumerate(STEPS):
                k = p(t, s2 + 4.7 + i * 0.6, 0.4)
                if k <= 0: continue
                y = 520 + i * 200
                x = 120 + int(60 * (1 - out_cubic(k)))
                row = Image.new("RGBA", (840, 160), (0, 0, 0, 0)); rd = ImageDraw.Draw(row)
                hot = i >= 2
                rd.rounded_rectangle([0, 0, 839, 159], radius=40, fill=(255, 255, 255, 245) if not hot else (*GOLD, 255))
                rd.ellipse([24, 30, 124, 130], fill=(*ACC, 255))
                rd.text((74, 80), n, font=font(F_BLACK, 52), fill=(255, 255, 255, 255), anchor="mm")
                rd.text((150, 80), lab, font=font(F_XB, 46), fill=(*INK, 255), anchor="lm")
                e = emoji_img(em, 70); row.alpha_composite(e, (750, int(80 - e.height / 2)))
                sub.alpha_composite(with_alpha(row, out_cubic(k)), (x, y))
            kk = p(t, s2 + 7.2, 0.3)
            draw_text(sub, "Steps 3 + 4 are what clients pay for", F_SEMI, 40, W / 2, 1360, GOLD, alpha=out_cubic(kk))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Same job. Less time."], t, s3 + 0.1, 330, 80, (WHITE, GREEN), gap=0.07, highlight={"less", "time."})
        bars(sub, t, s3 + 0.8)
        kk = p(t, s3 + 3.6, 0.4)
        pill(sub, W / 2, 1220, "Example: 10 captions for $60", F_XB, 50, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="💰")
        draw_text(sub, "Example timing + pricing. Results depend on your work.", F_MED, 33, W / 2, 1370, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
