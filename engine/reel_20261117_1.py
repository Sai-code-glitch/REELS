"""Ask 3 friends for their resume tonight (free practice -> before/after samples for a resume-fix side gig)."""
from reel_resume import *

ACC = (90, 200, 255)    # sky blue
GOLD = (255, 214, 92)
bg = Background(top=(8, 18, 44), bottom=(16, 44, 92), blobs=[(30, 80, 170), (90, 200, 255), (120, 60, 170)], seed=3211)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Ask 3 friends for", "their resume tonight"], t, -0.3, 360, 88, (WHITE, ACC), gap=0.06, highlight={"3", "resume", "tonight"})
        resume_card(sub, t, 0.5, W / 2 - 190, 1100, w=420, good=False, rot=8)
        resume_card(sub, t, 0.75, W / 2 + 190, 1120, w=420, good=False, rot=-6)
        resume_card(sub, t, 1.0, W / 2, 1150, w=440, good=False, rot=1)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["No clients yet?", "Practice for free"], t, s1 + 0.1, 320, 90, (WHITE, ACC), gap=0.07, highlight={"free"})
        checklist(sub, t, s1 + 1.0, ["Real resumes to fix", "Real before/after", "3 portfolio samples"], 620, 150, ACC, size=56, x0=170, every=0.8)
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1120, "Samples > promises", F_XB, 54, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="📁")
        draw_text(sub, "Buyers want to see your work first", F_SEMI, 42, W / 2, 1250, SOFT, alpha=out_cubic(p(t, s1 + 4.8, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Send this text"], t, s2 + 0.1, 270, 90, (WHITE, ACC), gap=0.07, highlight={"text"})
        msgs = [("me", "Hey! I'm learning resume writing. Can I fix yours for free?", s2 + 0.8, "typed"),
                ("them", "Yes please, mine is a mess", s2 + 3.4, None),
                ("me", "Send it over. Back to you in 2 days!", s2 + 4.6, "Delivered")]
        phone_chat(sub, t, s2 + 0.4, W / 2, 380, msgs, header="Sam", sub_label="Friend", w=820, h=880)
        kq = p(t, s2 + 6.0, 0.4)
        pill(sub, W / 2, 1350, "Free now. Paid later.", F_XB, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎯")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Save the before/after"], t, s3 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"before/after"})
        resume_card(sub, t, s3 + 0.5, W / 2 - 215, 760, w=380, good=False, rot=-4, label="BEFORE", label_col=RED2)
        ka = p(t, s3 + 1.4, 0.4)
        place_emoji(sub, "➡️", W / 2, 760, 100 * out_back(ka), alpha=out_cubic(ka))
        resume_card(sub, t, s3 + 1.8, W / 2 + 215, 760, w=380, good=True, rot=4, label="AFTER", label_col=OKG)
        checklist(sub, t, s3 + 3.0, ["Ask: can I show it?", "Hide name + contact"], 1130, 120, ACC, size=50, x0=200, every=0.8, icon="🔒")
        draw_text(sub, "Sample shown is fictional", F_SEMI, 34, W / 2, 1420, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
